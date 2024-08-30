from torch import Tensor, tensor


def get_column(tensor_arg: Tensor, column_index: int) -> Tensor:
    """
    Extract a specific column from a 2D tensor.

    :param tensor_arg: A 2D tensor from which to extract the column.
    :param column_index: The index of the column to extract.
    :return: A 1D tensor containing the specified column.
    """
    if tensor_arg.dim() != 2:
        raise ValueError("The input tensor must be 2-dimensional.")

    if column_index < 0 or column_index >= tensor_arg.size(1):
        raise IndexError("Column index out of range.")

    return tensor_arg[:, column_index]


if __name__ == "__main__":
    # Example usage:
    softmax = tensor([
        [7.6429e-05, 9.3273e-01, 1.4521e-06, 8.3141e-06, 1.8992e-07, 1.1806e-06, 3.7185e-06, 3.0577e-07, 1.4157e-04,
         6.7033e-02],
        [1.0524e-04, 9.8619e-01, 2.7803e-06, 3.9337e-06, 3.5393e-08, 1.0144e-06, 3.0293e-06, 3.7023e-07, 1.2569e-04,
         1.3567e-02],
        [7.3322e-05, 9.9012e-01, 2.0777e-06, 6.7596e-06, 1.4213e-07, 1.1205e-06, 5.7815e-06, 3.5834e-07, 1.3107e-04,
         9.6562e-03]
    ])

    index = 1
    column = get_column(softmax, index)
    print(column)
