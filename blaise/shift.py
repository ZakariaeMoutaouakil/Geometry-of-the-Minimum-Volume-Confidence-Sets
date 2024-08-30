from math import sqrt, log

import torch


def shift(Z: torch.Tensor, alpha: float) -> float:
    """
    Calculate the shift function from the given formula.

    :param Z: A 1D tensor representing the input vector.
    :param alpha: A float representing the alpha value.
    :return: A float representing the shift value.
    """
    if Z.dim() != 1:
        raise ValueError("The input tensor must be 1-dimensional.")

    n = Z.size(0)

    # Calculate the sample mean
    mean_Z = torch.mean(Z).item()

    # Calculate the sample variance
    variance_Z = torch.var(Z, unbiased=True).item()

    # Calculate Sn(Z)
    Sn_Z = (1 / (n * (n - 1))) * torch.sum((Z.unsqueeze(0) - Z.unsqueeze(1)) ** 2).item()

    # Calculate the first term under the square root
    term1 = sqrt((2 * Sn_Z * log(2 / alpha)) / n)

    # Calculate the second term
    term2 = (7 * log(2 / alpha)) / (3 * (n - 1))

    # Calculate the shift value
    shift_value = term1 + term2

    return shift_value


if __name__ == "__main__":
    # Example usage:
    Z_ = torch.tensor([0.1, 0.2, 0.3, 0.4, 0.5])
    alpha_ = 0.05
    result = shift(Z_, alpha_)
    print(result)
