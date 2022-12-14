# -*- coding: utf-8 -*-
"""Tp1_Arbres de décision_SarahYAICI_MohamedZIANE_KatiaALLACHE

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qKGDgr7LDuB1nx92XzIxMazjgdppPE9k
"""

import pandas as pd
from sklearn import tree
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV

data = pd.read_csv('car.csv')

data.head()

data['class_value'].replace(['unacc','acc','good','vgood'], ['0','1','2','3'],inplace=True)
data['buying'].replace(['low','med','high','vhigh'], ['0','1','2','3'], inplace=True)
data['maint'].replace(['low','med','high','vhigh'], ['0','1','2','3'], inplace=True)
data['porte'].replace(['5more'], ['5'], inplace=True)
data['pers'].replace(['more'], ['5'], inplace=True)
data['lug_boot'].replace(['small','med','big'], ['0','1','2'], inplace=True)
data['safety'].replace(['low','med','high'], ['0','1','2'], inplace=True)

data

x = data.drop(['class_value'],axis=1)

x.shape

y = data['class_value']

y.shape

print(y)

from sklearn.model_selection import train_test_split 
x_train,  x_test,  y_train,  y_test  =  train_test_split(x,  y,  train_size=0.7, random_state=0)

clf = tree.DecisionTreeClassifier() 
clf.fit(x_train, y_train)

tree.plot_tree(clf, filled=True)

clf.predict(x_test)

clf.score(x_test, y_test)

max_depth = np.arange(1,100,10)
min_sample_leaf_range = np.arange(1,100,10)

param = {'min_samples_leaf': min_sample_leaf_range,
         'max_depth':max_depth}

grid = GridSearchCV(tree.DecisionTreeClassifier(),param)

grid.fit(x_train,y_train)

grid.best_estimator_

grid.best_params_

grid.best_score_

x_train,  x_test,  y_train,  y_test  =  train_test_split(x,  y,  train_size=0.05, random_state=0)

clf = tree.DecisionTreeClassifier() 
clf.fit(x_train, y_train)
tree.plot_tree(clf, filled=True)

clf.predict(x_test)

clf.score(x_test, y_test)

max_depth = np.arange(1,100,10)
min_sample_leaf_range = np.arange(1,100,10)

param = {'min_samples_leaf': min_sample_leaf_range,
         'max_depth':max_depth}

grid = GridSearchCV(tree.DecisionTreeClassifier(),param)
grid.fit(x_train,y_train)

grid.best_estimator_
grid.best_params_

grid.best_score_

from sklearn import tree 
 
x = data.drop(['class_value'],axis=1)
y = data['class_value']
clf = tree.DecisionTreeRegressor() 
clf = clf.fit(x, y) 
clf.predict(x_test)

import numpy as np 
import matplotlib.pyplot as plt 
 
from sklearn.tree import DecisionTreeRegressor 
 
# Créer les données d'apprentissage 
np.random.seed(0) 
x = np.sort(5 * np.random.rand(80, 1), axis=0) 
y = np.sin(x).ravel()
fig = plt.figure(figsize=(12, 4)) 
fig.add_subplot(121) 
plt.plot(x, y) 
plt.title("Signal sinusoïdal pur") 
 
# On ajoute un bruit aléatoire tous les 5 échantillons 
y[::5] += 3 * (0.5 - np.random.rand(16)) 
fig.add_subplot(122) 
plt.plot(x, y) 
plt.title("Signal sinusoïdal bruité")

# Apprendre le modèle 
reg = DecisionTreeRegressor(max_depth=100) 
reg.fit(x, y) 
 
# Prédiction sur la même plage de valeurs 
X_test = np.arange(0.0, 5.0, 0.01)[:, np.newaxis] 
y_pred = reg.predict(X_test) 
 
# Affichage des résultats 
plt.figure() 
plt.scatter(X, y, c="darkorange", label="Exemples d'apprentissage") 
plt.plot(X_test, y_pred, color="cornflowerblue", label="Prédiction", 
linewidth=2) 
plt.xlabel("x") 
plt.ylabel("y") 
plt.title("Régression par un arbre de décision") 
plt.legend() 
plt.show()