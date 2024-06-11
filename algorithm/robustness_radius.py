from typing import List
from scipy.stats import norm


def robustness_radius(vector: List[float]) -> float:
    """
    Calculate the robustness radius in randomized smoothing.
    :param vector: probability vector
    :return: the robustness radius
    """
    # Sort the vector in descending order
    sorted_vector = sorted(vector, reverse=True)
    # Calculate the inverse Gaussian CDF (percent point function, ppf
    inverse_gaussian_cdf = norm.ppf(sorted_vector[0]) - norm.ppf(sorted_vector[1])
    # Calculate the robustness radius
    radius = 0.5 * inverse_gaussian_cdf

    return radius


if __name__ == "__main__":
    # Example usage
    probability_vector = [0.2, 0.4, 0.5]
    result = robustness_radius(probability_vector)
    print(f"Robustness radius: {result}")
