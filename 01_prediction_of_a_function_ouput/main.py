"""
This file contains a PyTorch model that takes an integer input and predicts the result.
"""
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

x= np.load("data.npz")["input"]
y= np.load("data.npz")["output"]

x_train: torch.Tensor = torch.tensor(data=x[:-1000], dtype=torch.float32)
y_train: torch.Tensor = torch.tensor(data=y[:-1000], dtype=torch.float32)
x_test: torch.Tensor = torch.tensor(data=x[-1000:], dtype=torch.float32)
y_test: torch.Tensor = torch.tensor(data=y[-1000:], dtype=torch.float32)
