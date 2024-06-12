from typing import Tuple

from scipy.stats import norm
from statsmodels.stats.proportion import proportion_confint


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
    probability_vec = (0.004975124378109453, 0.23880597014925373, 0.7562189054726368)
    noise_level = 0.12
    result = robustness_radius(probability_vec, noise_level)
    print(f"Robustness radius: {result}")
    counts = [0, 2, 48]
    alpha = 0.001
    p1 = proportion_confint(counts[-1], sum(counts), alpha=2 * alpha, method="beta")[0]
    rad = noise_level * norm.ppf(p1)
    print("Clopper Pearson radius:", rad)
    print("True p1           :", counts[-1] / sum(counts))
    print("Clopper Pearson p1:", p1)
    print("My p1             :", probability_vec[-1])
