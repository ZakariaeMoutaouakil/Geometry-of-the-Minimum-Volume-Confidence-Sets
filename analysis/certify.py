import ast
from time import time
from typing import List, Tuple, Dict

import pandas as pd

from algorithm.final_result import final_result
from analysis.smallest_subset import smallest_subset

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
sigma = 0.12
alpha = 0.001
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
        smallest_margin, smallest_radius = final_result(x=reduced_counts, delta=alpha, grid_size=111, precision=0.005,
                                                        debug=True)
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
# raw_vectors: List[List[int]] = df['counts'].to_list()
# for i in range(len(raw_vectors)):
#     print(raw_vectors[i])
#
# vectors = get_unique_vectors(vectors=raw_vectors)
# vectors = [sorted(vector) for vector in vectors]
# indices = unique_vector_indices(raw_vectors=raw_vectors, unique_vectors=vectors)
#
# print("length of vectors:", len(vectors))
# p1s: List[float] = []
# num_partitions = 3
# for vec in vectors:
#     print("vec:", vec)
#     observation = [vec[len(vec) - 1]]
#     rest = vec[:len(vec) - 1]
#     # print("rest:", rest)
#     i = smallest_subset(vector=rest, num_partitions=num_partitions - 1, debug=False)
#     # print("i:", i)
#     # print(i == len(rest) - num_partitions + 1)
#     second_class = vec[:i]
#     observation.append(sum(second_class))
#     # print("second_class:", second_class)
#     third_classes = vec[i:len(vec) - 1]
#     # print("third_classes:", third_classes)
#     observation.append(sum(third_classes))
#     observation = sorted(observation)
#     print("observation:", observation)
#     # partitions_ = partition_iterator(num_partitions=num_partitions-1, third_classes)
#     p1 = final_result(alpha=0.05, x=observation)
#     print("p1:", p1)
#     p1s.append(p1)
# for i in range(len(df)):
#     print(type(df.iloc[i]['counts'][0]))
