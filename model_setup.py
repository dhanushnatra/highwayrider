from Brain.rl_model import init_params,forward_prop
from torch import Tensor
from typing import TypedDict
import joblib
import os
import torch


model_path = "highway_rider.pth"

class ModelWeights(TypedDict):
    w1:Tensor
    b1:Tensor
    w2:Tensor
    b2:Tensor
    w3:Tensor
    b3:Tensor


w1,b1,w2,b2,w3,b3 = init_params()


def predict(x)->int:
    y_hat = torch.argmax(forward_prop(w1,b1,w2,b2,w3,b3,x)[0])
    print(y_hat)
    return int(y_hat)
    

def save_model():
    
    model_weights = ModelWeights()
    model_weights['w1'] = w1
    model_weights['b1'] = b1
    model_weights['w2'] = w2
    model_weights['b2'] = b2
    model_weights['w3'] = w3
    model_weights['b3'] = b3
    
    joblib.dump(
        model_weights,"self_highway_driver.pth"
    )

def load_model():
    if os.path.exists(model_path):
        model_weights:ModelWeights = joblib.load(model_path)
        return model_weights['w1'],model_weights['b1'],model_weights['w2'],model_weights['b2'],model_weights['w3'],model_weights['b3']
    else:
        return init_params()