from time import time

from algorithm.final_algorithm import final_algorithm
from analysis.draw import draw_discrete_simplex
from utils.discrete_simplex import discrete_simplex

if __name__ == "__main__":
    n_ = 10
    p_hat_ = [2 / n_, 3 / n_, 1. - (2 / n_) - (3 / n_)]
    delta_ = 0.01
    grid_size_ = 40
    margin_ = 0.1

    start_time = time()  # Start time
    region = final_algorithm(n_, p_hat_, delta_, grid_size_, margin_)
    end_time = time()  # End time

    print("Final confidence region:", region)
    for p_ in region:
        print(p_)

    print(f"Time taken to compute: {end_time - start_time:.6f} seconds")
    print("p_hat:", p_hat_)

    simplex_points = discrete_simplex(3, grid_size_)
    draw_discrete_simplex(simplex_points, region, p_hat_)
