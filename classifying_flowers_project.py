# -*- coding: utf-8 -*-
"""Classifying_Flowers_Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ckuR-0Dfq3cabvn8obFUJ2aDw3jK_ad1
"""

import pandas as pd

path = "/content/drive/MyDrive/Data/Iris.csv"
df = pd.read_csv(path)
df.head()

df.isnull().sum()

flower_mapping = {'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2}
df["Species"] = df["Species"].map(flower_mapping)

df.head()

"""**Spliting Values**"""

from sklearn.model_selection import train_test_split

X = df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']].values
Y = df['Species'].values
x_train, x_test, y_train, y_test = train_test_split(X, Y)

"""**Loading Model from sklearn**"""

from sklearn.linear_model import LogisticRegression

"""**Logisitc Regression**"""

model = LogisticRegression()

model.fit(x_train,y_train)

model.score(x_test,y_test)

"""**K Nearest Neighbors (KNN)**"""

from sklearn.neighbors import KNeighborsClassifier

model_2 = KNeighborsClassifier()

model_2.fit(x_train, y_train)

model_2.score(x_test, y_test)