from typing import Tuple, Callable


def find_min_vector_by_function(vectors: Tuple[Tuple[float, ...], ...], func: Callable[[Tuple[float, ...]], float]) \
        -> Tuple[Tuple[float, ...], float]:
    """
    Find the vector with the minimum value as determined by a given function.
    :param vectors: list of vectors
    :param func: a callable that takes a vector and returns a float
    :return: the vector with the minimum value as determined by the function and the minimum value
    """
    min_vector = min(vectors, key=func)
    min_value = func(min_vector)

    return min_vector, min_value


def calculate_margin(vector: Tuple[float, ...]) -> float:
    """
    Calculate the margin of a vector.
    :param vector: probability vector.
    :return: the margin.
    """
    sorted_vector = sorted(vector, reverse=True)
    return sorted_vector[0] - sorted_vector[1]


if __name__ == "__main__":
    # Example usage
    probability_vectors = (
        (0.2, 0.3, 0.5),
        (0.4, 0.4, 0.2),
        (0.1, 0.1, 0.8),
        (0.25, 0.25, 0.25, 0.25)
    )

    vec, margin = find_min_vector_by_function(probability_vectors, calculate_margin)
    print(f"Vector with smallest margin: {vec}")
    print(f"Margin: {margin}")
