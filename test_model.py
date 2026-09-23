from Brain.rl_model import model_loop
from Brain.model_parts import init_params,forward_prop
import torch

w1,b1,w2,b2 = init_params()

x = torch.randn(1,2)
y = torch.randn(1,2)

print("initial y:",forward_prop(w1,b1,w2,b2,x)[-1])

for _ in range(100):
    w1,b1,w2,b2 = model_loop(w1,b1,w2,b2,y,x,learning_rate=0.03)

print("trained y:",forward_prop(w1,b1,w2,b2,x)[-1])