import torch

import utilities.utils as utils


def mse(input_tensor: torch.Tensor, target: torch.Tensor) -> torch.Tensor:
    """TODO: implement this method"""
    #loss = torch.nn.MSELoss()
    #output = loss(input_tensor, target)
    temp= input_tensor-target
    o = torch.pow(temp,2)
    out = torch.mean(o)
    return out
