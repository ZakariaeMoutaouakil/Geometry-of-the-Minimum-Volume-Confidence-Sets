from typing import Tuple

from scipy.stats import norm


def robustness_radius(probability_vector: Tuple[float, ...], sigma: float) -> float:
    """
    Calculate the robustness radius in randomized smoothing.
    :param probability_vector: probability vector
    :param sigma: noise level
    :return: the robustness radius
    """
    # Sort the vector in descending order
    sorted_vector = sorted(probability_vector, reverse=True)
    # Calculate the inverse Gaussian CDF (percent point function, ppf
    inverse_gaussian_cdf = norm.ppf(sorted_vector[0]) - norm.ppf(sorted_vector[1])
    # Calculate the robustness radius
    radius = 0.5 * sigma * inverse_gaussian_cdf

    return radius


if __name__ == "__main__":
    # Example usage
    probability_vec = (0.2, 0.4, 0.5)
    noise_level = 0.05
    result = robustness_radius(probability_vec, noise_level)
    print(f"Robustness radius: {result}")
