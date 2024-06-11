from time import time
from typing import Tuple, List

from algorithm.final_algorithm import final_algorithm
from algorithm.margin import find_min_vector_by_function, calculate_margin
from analysis.draw import draw_discrete_simplex
from utils.discrete_simplex import discrete_simplex


def second_largest(numbers: List[float]) -> float:
    first, second = float('-inf'), float('-inf')
    for number in numbers:
        if number > first:
            first, second = number, first
        elif first > number > second:
            second = number
    return second


def seconds_to_minutes(seconds: float) -> Tuple[int, float]:
    # Calculate the minutes
    minutes = int(seconds // 60)
    # Calculate the leftover seconds
    leftover_seconds = seconds % 60
    return minutes, leftover_seconds


if __name__ == "__main__":
    n_ = 30
    p_hat_ = [(n_ - 2) / n_, 1 / n_, 1 / n_]
    # p_hat_ = [150 / n_, 300 / n_, 1. - (150 / n_) - (300 / n_)]
    delta_ = 0.05
    grid_size_ = 100
    margin_ = 0.1

    start_time = time()  # Start time
    region = final_algorithm(n_, p_hat_, delta_, grid_size_, margin_)
    end_time = time()  # End time

    print("Final confidence region:")
    for p_ in region:
        print(p_)

    time_taken = end_time - start_time
    if time_taken > 60:
        minutes_taken, seconds_taken = seconds_to_minutes(time_taken)
        print(f"Time taken: {minutes_taken:.0f} minutes and {seconds_taken:.6f} seconds")
    else:
        print(f"Time taken: {time_taken:.6f} seconds")

    print("p_hat:", p_hat_)

    simplex_points = discrete_simplex(3, grid_size_)
    draw_discrete_simplex(simplex_points, region, p_hat_)

    smallest_margin_vector, smallest_margin = find_min_vector_by_function(region, func=calculate_margin)
    print(f"Vector with smallest margin: {smallest_margin_vector}")
    print(f"Margin: {smallest_margin}")

    second_largest_value = max([second_largest(vector) for vector in region])
    print(f"Second largest value: {second_largest_value}")
