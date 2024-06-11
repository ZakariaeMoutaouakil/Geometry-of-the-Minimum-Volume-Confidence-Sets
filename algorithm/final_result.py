from typing import List, Tuple

from algorithm.final_algorithm import final_algorithm
from algorithm.margin import find_min_vector_by_function, calculate_margin
from algorithm.robustness_radius import robustness_radius


def final_result(n: int, p_hat: List[float], delta: float, grid_size: int,
                 precision: float = 0., debug: bool = False) -> Tuple[float, float]:
    """
    Calculate the final result.

    Args:
    n (int): The common denominator.
    p (List[float]): The vector p.
    p_hat (List[float]): The vector p_hat.
    delta (float): The threshold value.

    Returns:
    Tuple[float, float]: The smallest margin and smallest radius.
    """
    confidence_region = final_algorithm(n, p_hat, delta, grid_size, precision, debug=False)
    margin_vector, smallest_margin = find_min_vector_by_function(confidence_region, calculate_margin)
    radius_vector, smallest_radius = find_min_vector_by_function(confidence_region, robustness_radius)
    if debug:
        print("Margin vector:", margin_vector)
        print("Radius vector:", radius_vector)
    return smallest_margin, smallest_radius


if __name__ == "__main__":
    # Example usage
    n_ = 30
    p_hat_ = [(n_ - 2) / n_, 1 / n_, 1 / n_]
    print("p_hat:", p_hat_)
    delta_ = 0.05
    grid_size_ = 100
    precision_ = 0.1

    margin, radius = final_result(n_, p_hat_, delta_, grid_size_, precision_, debug=True)
    print(f"Smallest margin: {margin}")
    print(f"Smallest radius: {radius}")

    n_ = 30
    p_hat_ = [x / n_ for x in [15, 10, 5]]
    print("p_hat:", p_hat_)
    delta_ = 0.05
    grid_size_ = 100
    precision_ = 0.001

    margin, radius = final_result(n_, p_hat_, delta_, grid_size_, precision_, debug=True)
    print(f"Smallest margin: {margin}")
    print(f"Smallest radius: {radius}")
