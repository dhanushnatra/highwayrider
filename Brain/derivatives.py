import torch

Tensor = torch.Tensor

def derv_relu(my_z:Tensor)->Tensor:
    return (my_z > 0).float()

def delC_delb3(yhat:Tensor,y:Tensor):
    return yhat-y

def delC_delw3(Db3:Tensor,A2:Tensor):
    return Db3.mm(A2.T)

def delC_delb2(Db3:Tensor,W3:Tensor,Z2:Tensor):
    Da2 = W3.T.mm(Db3)
    
    return Da2*derv_relu(Z2)

def delC_delw2(Db2:Tensor,A1:Tensor):
    return Db2.mm(A1.T)

def delC_delb1(Db2:Tensor,W2:Tensor,Z1:Tensor):
    Da1 = W2.T.mm(Db2)
    
    return Da1*derv_relu(Z1)

def delC_delw1(dB1:Tensor,X:Tensor):
    return dB1.mm(X.T)