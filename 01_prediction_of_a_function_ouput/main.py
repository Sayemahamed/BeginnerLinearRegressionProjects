import torch  # type :ignore
import torch.nn as nn
import torch.optim as optim
import numpy as np
# import matplotlib.pyplot as plt

X = np.array(object=[x for x in range(1000)])
X = X.reshape(-1, 1)
y = 46 + 2 * X.flatten()

# plt.scatter(X, y, label="Initial data")
# plt.title("Pre PyTorch")
# plt.xlabel("X")
# plt.ylabel("y")
# plt.legend()
# plt.show()

X_tensor = torch.tensor(X_normalized, dtype=torch.float32)

y_tensor = torch.tensor(y_normalized, dtype=torch.float32)


class LinearRegression(nn.Module):
    """
    this is a pytorch implementation of linear regression

    Args:
        nn (_type_): _description_
    """

    def __init__(self, in_features=1, out_features=1):
        super(LinearRegression, self).__init__()
        self.linear = nn.Linear(in_features, out_features)

    def forward(self, x):
        out = self.linear(x).flatten()
        return out


trained_model = LinearRegression(in_features=1, out_features=1)

criterion = nn.MSELoss()
optimizer = optim.SGD(trained_model.parameters(), lr=0.1)  # type: ignore


Epochs = 20
for epoch in range(Epochs):
    optimizer.zero_grad()
    y_pred = trained_model(X_tensor)
    loss = criterion(y_pred, y_tensor)
    loss.backward()
    optimizer.step()
    if epoch % 2 == 0:
        print(f"Epoch: {epoch}, Loss: {loss.item()}")


new_x = 121
new_x_normalized = (new_x - x_mean) / x_std
new_x_tensor: torch.Tensor = torch.tensor(new_x_normalized, dtype=torch.float32).view(
    -1, 1
)

trained_model.eval()
with torch.no_grad():
    new_y = trained_model(new_x_tensor)
    new_y = new_y.item() * y_std + y_mean
    print(new_y)
