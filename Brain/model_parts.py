import torch
import warnings


warnings.filterwarnings("ignore")

Tensor = torch.Tensor

device = "cuda" if torch.cuda.is_available() else "cpu"

print("using",device)

def relu(my_z1:Tensor)->Tensor:
    return torch.max(my_z1,torch.zeros_like(my_z1))


def init_params()->tuple[Tensor,Tensor,Tensor,Tensor]:
    w1 = torch.rand(2,1)
    b1 = torch.rand(2,2)
    w2 = torch.rand(1,2)
    b2 = torch.rand(1,2)
    return w1,b1,w2,b2

def forward_prop(my_w1:Tensor,my_b1:Tensor,my_w2:Tensor,my_b2:Tensor,my_x:Tensor)->tuple[Tensor,Tensor,Tensor]:
    z1 = my_w1.mm(my_x)+my_b1
    z2 = relu(z1)
    y_hat = my_w2.mm(z2)+my_b2
    return z1,z2,y_hat

def derv_relu(my_z1:Tensor)->Tensor:
    return (my_z1 > 0).float()

def del_c_del_b2(my_yhat:Tensor,my_y:Tensor)->Tensor:
    return (2/len(my_yhat))*(torch.sum(my_yhat-my_y))

def del_c_del_w2(my_Dc_by_Db2:Tensor,my_z2)->Tensor:
    return my_Dc_by_Db2*(my_z2)

def del_c_del_b1(my_Dc_by_Db2:Tensor,my_w2:Tensor,my_derv_relu:Tensor)->Tensor:
    return (my_Dc_by_Db2*(my_w2))*my_derv_relu

def del_c_del_w1(my_DC_by_Db1:Tensor,my_x:Tensor):
    return my_DC_by_Db1.mm(my_x.T)

def update_params(my_Dc_by_Dw2:Tensor,my_Dc_by_Db2:Tensor,my_Dc_by_Dw1:Tensor,my_Dc_by_Db1:Tensor,
                 my_w2:Tensor,my_b2:Tensor,my_w1:Tensor,my_b1:Tensor,learning_rate:float)->tuple[Tensor,Tensor,Tensor,Tensor]:
    return (my_w2-learning_rate*my_Dc_by_Dw2),(my_b2-learning_rate*my_Dc_by_Db2),(my_w1-learning_rate*my_Dc_by_Dw1),(my_b1-learning_rate*my_Dc_by_Db1)


def back_prop(my_yhat,my_y,my_z2,my_z1,my_w2,my_x):
    calc_Dc_by_Db2 = del_c_del_b2(my_yhat,my_y)
    calc_Dc_by_Dw2 = del_c_del_w2(calc_Dc_by_Db2,my_z2)
    relu_derv = derv_relu(my_z1)
    calc_Dc_by_Db1 = del_c_del_b1(calc_Dc_by_Db2,my_w2,relu_derv)
    calc_Dc_by_Dw1 = del_c_del_w1(calc_Dc_by_Db1,my_x)
    
    return calc_Dc_by_Dw2,calc_Dc_by_Db2,calc_Dc_by_Dw1,calc_Dc_by_Db1