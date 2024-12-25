import json
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

from utils import stem, tokenize, bag_of_words
from model import NeuralNet

with open("./intents.json", "r") as file:
    intents = json.load(file)
    
all_words = []
tags = []
xy = []

for intent in intents["intents"]:
    tag = intent["tag"]
    patterns = intent["patterns"]
    tags.append(tag)
    
    for pattern in patterns:
        w = tokenize(pattern)
        all_words.extend(w)
        xy.append((w, tag))
        
ignore_words = ["!", "?", ".", ","]

all_words = [stem(w) for w in all_words if w not in ignore_words]
all_words = sorted(set(all_words))

tags = sorted(set(tags))

X_train = []
y_train = []

for (pattern_sentence, tag) in xy:
    bag = bag_of_words(pattern_sentence, all_words)
    X_train.append(bag)
    
    label = tags.index(tag)
    y_train.append(label)
    
X_train = torch.tensor(X_train)
y_train = torch.tensor(y_train)

class ChatDataset(Dataset):
    def __init__(self):
        self.n_samples = len(X_train)
        self.x_data = X_train
        self.y_data = y_train
        
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]
    
    def __len__(self):
        return self.n_samples
    
# hyperparameters
batch_size = 8
hidden_size = 8
output_size = len(tags)
input_size = len(X_train[0])
learning_rate = 0.001
num_epochs = 1000

# setup device agnostic code
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

dataset = ChatDataset()
train_loader = DataLoader(dataset=dataset, batch_size=8, shuffle=True)

model = NeuralNet(input_size, hidden_size, output_size)

# criterion and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

# training loop
for epoch in range(num_epochs):
    for (words, labels) in train_loader:
        words = words.to(device)
        labels = labels.to(device)
        
        # forward propagation
        outputs = model(words)
        
        # error
        loss = criterion(outputs, labels)
        
        # reset gradients
        optimizer.zero_grad()
        
        # backward propagation
        loss.backward()
        
        # update weights
        optimizer.step()
        
    if (epoch + 1) % 20 == 0:
        print(f"epoch {epoch+1}/{num_epochs}, loss={loss.item()}")
        
print(f"final loss, loss={loss.item()}")

data = {
    "model_state": model.state_dict(),
    "input_size": input_size,
    "output_size": output_size,
    "hidden_size": hidden_size,
    "all_words": all_words,
    "tags": tags
}

FILE = "data.pth"
torch.save(data, FILE)

print(f"training complete. file saved to {FILE} for inference.")