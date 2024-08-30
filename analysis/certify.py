import ast
from time import time
from typing import List, Tuple, Dict

import pandas as pd

from algorithm.all_s_double_stars import calculate_all_s_double_stars
from algorithm.confidence_region import confidence_region
from analysis.smallest_subset import smallest_subset
from utils.discrete_simplex import discrete_simplex
from utils.factorial_list import factorial_list

preprocessed_file_path = '../data/preprocessed_data.tsv'

# Define the data types for each column
dtype_dict = {
    'idx': int,
    'label': int,
    'predict': int,
    'radius': float,
    'correct': int,
    'time': str
}

# Read the preprocessed TSV data into a DataFrame with specified dtypes
df = pd.read_csv(preprocessed_file_path, sep='\t', dtype=dtype_dict, converters={'counts': ast.literal_eval})

# Display the DataFrame with correct types
# print(df)
# print(df.dtypes)
num_partitions = 3
counts = df.iloc[0]['counts']
print("counts:", counts)
n = sum(counts)
factorials = factorial_list(n)
grid = 201
observations = discrete_simplex(k=num_partitions, n=n, normalize=False)
probabilities = discrete_simplex(k=num_partitions, n=grid, normalize=True)
sigma = 0.12
alpha = 0.001
s_double_stars = calculate_all_s_double_stars(
    probabilities=probabilities, observations=observations, factorials=factorials, alpha=alpha
)
# Dictionary to cache results and time of final_result function
final_result_cache: Dict[Tuple[int, ...], Tuple[Tuple[float, float], float]] = {}
elapsed_time, cached_time = 0., 0.
for i in range(len(df)):
    print("old:", df.iloc[i])
    counts: List[int] = df.iloc[i]['counts']
    prediction = counts.index(max(counts))
    print("counts:", counts)
    print("prediction:", prediction)
    observation = sorted(smallest_subset(vector=sorted(counts), num_partitions=num_partitions))
    reduced_counts = [int(x) for x in observation]
    reduced_counts_tuple = tuple(reduced_counts)
    print("reduced_counts:", reduced_counts)

    if reduced_counts_tuple in final_result_cache:
        (smallest_margin, smallest_radius), cached_time = final_result_cache[reduced_counts_tuple]
    else:
        start_time = time()
        result = confidence_region(x=reduced_counts_tuple, all_s_double_stars=s_double_stars, alpha=alpha, sigma=sigma)
        smallest_margin, smallest_radius = result['smallest_margin'], result['smallest_radius']
        print("Radius minimizer:", result['radius_vector'])
        print("Margin minimizer:", result['margin_vector'])
        end_time = time()
        elapsed_time = end_time - start_time
        print("time:", elapsed_time)
        # Cache the result and time
        final_result_cache[reduced_counts_tuple] = ((smallest_margin, smallest_radius), elapsed_time)

    print("smallest_margin:", smallest_margin)
    print("smallest_radius:", smallest_radius)

    if smallest_margin > 0.:
        df.loc[df.index[i], 'radius'] = sigma * smallest_radius
        df.loc[df.index[i], 'correct'] = int(prediction == df.iloc[i]['label'])
    else:
        df.loc[df.index[i], 'radius'] = 0.
        prediction = -1
        df.loc[df.index[i], 'correct'] = 0

    df.loc[df.index[i], 'predict'] = prediction
    if reduced_counts_tuple not in final_result_cache:
        df.loc[df.index[i], 'time'] = f"{elapsed_time:.6f}"
    else:
        df.loc[df.index[i], 'time'] = f"{cached_time:.6f}"
    print("time:", df.iloc[i]['time'])
    print("new:", df.iloc[i])

# Remove the last three columns
df_modified = df.iloc[:, :-2]  # This slices out all rows and all columns except the last two

# Save to TSV file
df_modified.to_csv('../data/modified_data_50.tsv', sep='\t',
                   index=False)  # Set index=False if you don't want to save the index as a separate column
