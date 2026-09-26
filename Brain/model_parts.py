import torch
import warnings
from torch import Tensor
from Brain.derivatives import delC_delb1,delC_delb2,delC_delb3,delC_delw1,delC_delw2,delC_delw3

warnings.filterwarnings("ignore")



def relu(my_z:Tensor)->Tensor:
    return torch.max(my_z,torch.zeros_like(my_z))


def softmax(Z:Tensor)->Tensor:
    exp_z = torch.exp(Z)
    return exp_z / torch.sum(exp_z)

def forward_prop(my_w1:Tensor,my_b1:Tensor,my_w2:Tensor,
    my_b2:Tensor,my_w3:Tensor,my_b3:Tensor,my_x:Tensor
    )->tuple[Tensor,Tensor,Tensor,Tensor,Tensor]:
  
    z1 = my_w1.mm(my_x)+my_b1
    a1 = relu(z1)
    z2 = my_w2.mm(a1)+my_b2
    a2 = relu(z2)
    z3 = my_w3.mm(a2)+my_b3
    y_hat = softmax(z3)
    return y_hat,a2,z2,a1,z1

def update_params(my_w1:Tensor,my_b1:Tensor,my_w2:Tensor,my_b2:Tensor,
    my_w3:Tensor,my_b3:Tensor,my_Dw1:Tensor,my_Db1:Tensor,my_Dw2:Tensor,
    my_Db2:Tensor,my_Dw3:Tensor,my_Db3:Tensor,learning_rate:float
    )->tuple[Tensor,Tensor,Tensor,Tensor,Tensor,Tensor]:
    
    my_w1 = my_w1 - learning_rate*my_Dw1
    my_b1 = my_b1 - learning_rate*my_Db1
    my_w2 = my_w2 - learning_rate*my_Dw2
    my_b2 = my_b2 - learning_rate*my_Db2
    my_w3 = my_w3 - learning_rate*my_Dw3
    my_b3 = my_b3 - learning_rate*my_Db3
    
    return my_w1,my_b1,my_w2,my_b2,my_w3,my_b3

def backward_prop(yhat:Tensor,y:Tensor,A2:Tensor,W3:Tensor,Z2:Tensor,
    A1:Tensor,W2:Tensor,Z1:Tensor,X:Tensor
    )->tuple[Tensor,Tensor,Tensor,Tensor,Tensor,Tensor]:
    
    Db3 = delC_delb3(yhat,y)
    Dw3 = delC_delw3(Db3,A2)
    Db2 = delC_delb2(Db3,W3,Z2)
    Dw2 = delC_delw2(Db2,A1)
    Db1 = delC_delb1(Db2,W2,Z1)
    Dw1 = delC_delw1(Db1,X)
    
    return Dw1,Db1,Dw2,Db2,Dw3,Db3


def cross_entropy(my_yhat:Tensor,my_y:Tensor):
    return -1*torch.sum(
        my_y*torch.log(my_yhat)
    )