from Brain.rl_model import model_loop
from Brain.model_parts import init_params
import torch

w1,b1,w2,b2 = init_params()

x = torch.tensor([[1,2.]])
y = torch.tensor([[3,4.]])


epochs = 100
for epoch in range(epochs):
    w1,b1,w2,b2 = model_loop(w1,b1,w2,b2,y,x,learning_rate=0.1)
