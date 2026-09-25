from Brain.rl_model import init_params,forward_prop
from torch import Tensor
from typing import TypedDict
import joblib
import os
import torch


model_path = "./highway_rider.pth"

class ModelWeights(TypedDict):
    w1:Tensor
    b1:Tensor
    w2:Tensor
    b2:Tensor
    w3:Tensor
    b3:Tensor


def convert_to_int(y_hat:Tensor)->int:
    return int(torch.argmax(y_hat)) 

def predict(w1,b1,w2,b2,w3,b3,x)->int:
    y_hat = torch.argmax(forward_prop(w1,b1,w2,b2,w3,b3,x)[0])
    return int(y_hat)

def save_model(w1,b1,w2,b2,w3,b3):
    
    model_weights = ModelWeights()
    model_weights['w1'] = w1
    model_weights['b1'] = b1
    model_weights['w2'] = w2
    model_weights['b2'] = b2
    model_weights['w3'] = w3
    model_weights['b3'] = b3
    
    joblib.dump(
        model_weights,model_path
    )

def load_model():
    if os.path.exists(model_path):
        model_weights:ModelWeights = joblib.load(model_path)
        
        return model_weights['w1'],model_weights['b1'],model_weights['w2'],model_weights['b2'],model_weights['w3'],model_weights['b3']
    else:
        print("weights init")
        return init_params()