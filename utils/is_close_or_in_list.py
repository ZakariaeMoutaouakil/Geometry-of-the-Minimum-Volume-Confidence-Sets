from typing import List


def is_close_or_in_list(p_hat: float, s_double_star: List[float], margin: float = 0.) -> bool:
    """
    Check if the value is in the list or close to an element in the list within the specified margin.

    Args:
    p_hat (float): The value to check.
    s_double_star (List[float]): The list of float values.
    margin (float): The allowed margin for closeness. Default is 0.

    Returns:
    bool: True if the value is in the list or close to any element in the list within the margin, False otherwise.
    """
    for element in s_double_star:
        if abs(p_hat - element) <= margin:
            return True
    return False


if __name__ == "__main__":
    # Example usage:
    value = 5.
    values_list = [5.0, 10.0, 15.0]
    error = 0.

    result = is_close_or_in_list(value, values_list, error)
    print(f"Is the value {value} in the list {values_list} or close to any element within the margin {error}? {result}")
