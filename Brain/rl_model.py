
from .model_parts import forward_prop,back_prop,update_params


def model_loop(my_w1,my_b1,my_w2,my_b2,my_y,my_x,learning_rate):
    z1,z2,y_hat = forward_prop(my_w1,my_b1,my_w2,my_b2,my_x)
    Dc_by_Dw2,Dc_by_Db2,Dc_by_Dw1,Dc_by_Db1=back_prop(y_hat,my_y,z2,z1,my_w2,my_x)
    my_w2,my_b2,my_w1,my_b1 = update_params(Dc_by_Dw2,Dc_by_Db2,Dc_by_Dw1,Dc_by_Db1,my_w2,my_b2,my_w1,my_b1,learning_rate)
    return my_w1,my_b1,my_w2,my_b2