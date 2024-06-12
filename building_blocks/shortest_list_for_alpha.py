from time import time
from typing import Tuple


def shortest_list_for_alpha(x_probabilities: Tuple[Tuple[Tuple[int, ...], float], ...], alpha: float) \
        -> Tuple[Tuple[int, ...], ...]:
    """
    Find the shortest list of consecutive elements such that the sum of their second coordinates is greater than 1 -
    alpha.

    Args: p_hat_probabilities (List[Tuple[List[float], float]]): A list of tuples containing a list of floats and a
    float, sorted in descending order of the float. alpha (float): The threshold value.

    Returns:
    List[List[float]]: The shortest list of first coordinates whose sum of second coordinates is greater than 1 - alpha.
    """
    cumulative_sum = 0.
    result = []

    for x, prob in x_probabilities:
        cumulative_sum += prob
        result.append(tuple(x))
        if cumulative_sum >= 1 - alpha:
            break

    return tuple(result)


if __name__ == "__main__":
    # Example usage:
    x_probas = (
        ((3, 2, 1), 0.05),
        ((1, 2, 3), 0.9),
        ((2, 1, 3), 0.05)
    )
    risk = 0.05

    start_time = time()  # Start time
    final_result = shortest_list_for_alpha(x_probas, risk)
    end_time = time()  # End time

    print("Final result:", final_result)

    print(f"Time taken to compute: {end_time - start_time:.6f} seconds")
