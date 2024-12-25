import torch
import torch.nn as nn

class NeuralNet(torch.nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.linear_1 = torch.nn.Linear(input_size, hidden_size)
        self.linear_2 = torch.nn.Linear(hidden_size, hidden_size)
        self.linear_3 = torch.nn.Linear(hidden_size, num_classes)
        self.relu = torch.nn.ReLU()
        
    def forward(self, x):
        out = self.linear_1(x)
        out = self.relu(out)
        out = self.linear_2(out)
        out = self.relu(out)
        out = self.linear_3(out)
        
        return out