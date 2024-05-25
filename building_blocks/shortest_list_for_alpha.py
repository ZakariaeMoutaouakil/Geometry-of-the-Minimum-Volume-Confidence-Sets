from time import time
from typing import List, Tuple


def shortest_list_for_alpha(p_hat_probabilities: List[Tuple[List[float], float]], alpha: float) -> List[List[float]]:
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

    for p_hat, prob in p_hat_probabilities:
        cumulative_sum += prob
        result.append(p_hat)
        if cumulative_sum > 1 - alpha:
            break

    return result


if __name__ == "__main__":
    # Example usage:
    p_hat_probas = [
        ([0.3, 0.3, 0.4], 0.5),
        ([0.1, 0.2, 0.7], 0.3),
        ([0.2, 0.3, 0.5], 0.15),
        ([0.4, 0.4, 0.2], 0.05)
    ]
    risk = 0.1

    start_time = time()  # Start time
    final_result = shortest_list_for_alpha(p_hat_probas, risk)
    end_time = time()  # End time

    for p in final_result:
        print(p)

    print(f"Time taken to compute: {end_time - start_time:.6f} seconds")
