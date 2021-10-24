import numpy as np 
import pandas as pd 
import plotly.express as px
import enlighten
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from scipy.spatial import distance


## let's try use pytorch 

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch.utils.data as data

import torchvision.transforms as transforms
import torchvision.datasets as datasets

from sklearn import metrics
from sklearn import decomposition
from sklearn import manifold
from torch.autograd import Variable
import matplotlib.pyplot as plt
import numpy as np

import copy
import random
import time

demand=pd.read_csv('./../generated_demand/demand_100000.csv')
demand['time_for_walk']=pd.to_datetime(demand['time_for_walk'])
demand['hour']=demand['time_for_walk'].map(lambda x: x.hour)
demand['day']=demand['time_for_walk'].map(lambda x: x.day)
data_=demand.groupby(['id_busStop','hour']).index.count().reset_index().loc[:,['id_busStop','hour','index']]

X=data_.to_numpy()[:,:2]
d = dict([(y,x) for x,y in enumerate(sorted(set(X[:,0])))])
X[:,0]=[d[x] for x in X[:,0]]
Y=data_.to_numpy()[:,2]
X_train, X_test, Y_train, Y_test = train_test_split(X.astype(float), Y.astype(float),random_state=0)
x_train = torch.FloatTensor(X_train)
y_train = torch.FloatTensor(Y_train)
x_test = torch.FloatTensor(X_test)
y_test = torch.FloatTensor(Y_test)
# Now in the format they want 
train_data=[]
for i in range(x_train.shape[0]):
    train_data.append((x_train[i],y_train[i]))

#test data
test_data=[]
for i in range(x_test.shape[0]):
    test_data.append((x_test[i],y_test[i]))

# view data
# Creating figure
fig = plt.figure(figsize = (10, 7))
ax = plt.axes(projection ="3d")
 
# Creating plot
ax.scatter3D(x_train.data.numpy()[:,0], x_train.data.numpy()[:,1], y_train.data.numpy(), color = "green")
plt.title("simple 3D scatter plot")
 
# show plot
plt.show()