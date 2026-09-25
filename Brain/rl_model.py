from Brain.model_parts import forward_prop,backward_prop,update_params
import torch
from torch import Tensor

def init_params()->tuple[Tensor,Tensor,Tensor,Tensor,Tensor,Tensor]:
    w1 = torch.randn(16,10)
    b1 = torch.randn(16,1)
    w2 = torch.randn(16,16)
    b2 = torch.randn(16,1)
    w3 = torch.randn(3,16)
    b3 = torch.randn(3,1)
    
    return w1,b1,w2,b2,w3,b3

def model_loop(w1:Tensor,b1:Tensor,w2:Tensor,b2:Tensor,w3:Tensor,b3:Tensor,x:Tensor,y:Tensor,learning_rate:float):
    yhat,a2,z2,a1,z1 = forward_prop(w1,b1,w2,b2,w3,b3,x)
    dw1,db1,dw2,db2,dw3,db3 = backward_prop(yhat,y,a2,w3,z2,a1,w2,z1,x)
    w1,b1,w2,b2,w3,b3 = update_params(w1,b1,w2,b2,w3,b3,dw1,db1,dw2,db2,dw3,db3,learning_rate)
    return w1,b1,w2,b2,w3,b3,yhat