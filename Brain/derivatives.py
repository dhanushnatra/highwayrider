import torch

Tensor = torch.Tensor

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
