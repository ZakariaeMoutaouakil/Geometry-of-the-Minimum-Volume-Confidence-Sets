from typing import List

import matplotlib.pyplot as plt

from utils.discrete_simplex import discrete_simplex


def draw_discrete_simplex(simplex: List[List[float]],
                          highlight_points: List[List[float]],
                          red_point: List[float]) -> None:
    """
    Draw the discrete simplex for k = 3, focusing on the first two coordinates.

    Args:
    simplex (List[List[float]]): List of points in the simplex.
    highlight_points (List[List[float]]): Points to be colored orange.
    red_point (List[float]): A point to be marked red.
    """
    # Extract coordinates for plotting
    x_coords = [point[0] for point in simplex]
    y_coords = [point[1] for point in simplex]

    # Highlight points
    highlight_x_coords = [point[0] for point in highlight_points]
    highlight_y_coords = [point[1] for point in highlight_points]

    # Red point coordinates
    red_x_coord = red_point[0]
    red_y_coord = red_point[1]

    # Plotting the simplex
    plt.scatter(x_coords, y_coords, c='blue', marker='o', label='Simplex Points')
    plt.scatter(highlight_x_coords, highlight_y_coords, c='orange', marker='o', label='Highlighted Points')
    plt.scatter(red_x_coord, red_y_coord, c='red', marker='o', label='Red Point')
    plt.xlabel('First coordinate')
    plt.ylabel('Second coordinate')
    plt.title('Discrete Simplex for k=3')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    k = 3
    n_ = 10
    simplex_points = discrete_simplex(k, n_)
    # Example usage with some points to highlight
    points = [
        [0.1, 0.2, 0.7],
        [0.3, 0.3, 0.4]
    ]
    center = [0.2, 0.3, 0.5]
    draw_discrete_simplex(simplex_points, points, center)
