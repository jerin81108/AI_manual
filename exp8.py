import torch, torch.nn as nn, torchbnn as bnn, matplotlib.pyplot as plt
from sklearn.datasets import load_iris

X, Y = load_iris(return_X_y=True)
x, y = torch.tensor(X).float(), torch.tensor(Y).long()

m = nn.Sequential(bnn.BayesLinear(0, 0.1, 4, 100), nn.ReLU(), bnn.BayesLinear(0, 0.1, 100, 3))
ce, kl, opt = nn.CrossEntropyLoss(), bnn.BKLLoss(reduction='mean', last_layer_only=False), torch.optim.Adam(m.parameters(), lr=0.01)

for _ in range(1000):
    opt.zero_grad(); (ce(m(x), y) + 0.01 * kl(m)).backward(); opt.step()

p = m(x).argmax(1)
print(f"Accuracy: {(p == y).float().mean().item():.2%}")

fig, (a1, a2) = plt.subplots(1, 2)
a1.scatter(X[:, 0], X[:, 1], c=Y); a1.set_title("Actual")
a2.scatter(X[:, 0], X[:, 1], c=p); a2.set_title("Predicted")
plt.show()