# -*- coding: utf-8 -*-
"""Vehicle Detection SVC.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-E72xR_qlm79SjQOuOjaYvhjAPLWW6Sx
"""

import pandas as pd
df=pd.read_csv('/content/vehicle dataset KNN.txt')
print(df.shape)
print(df.sum())

print('Before:')
#A list with all missing values
missing_values_formats=['?']
df=pd.read_csv("/content/vehicle dataset KNN.txt", na_values=missing_values_formats)
pd.set_option('display.max_rows', None)
print(df)

df.drop(['id'],1,inplace=True)
print("after dropping data:")
print(df)
print(df.shape)

df.fillna(df.mean(),inplace=True)
print(df)
print(df.shape)

#Slicing
X_features_input=df.iloc[:,:9]
print(X_features_input)

y_label_output=df.iloc[:,9].values
print(y_label_output)

#labels
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test= train_test_split(X_features_input, y_label_output, test_size=0.20,random_state=5)
#imported the algorithm
from sklearn.svm import SVC
svclassifier= SVC(kernel='linear')
svclassifier.fit(X_train,y_train)

#Prediction
y_pred=svclassifier.predict(X_test)

#Accuracy
from sklearn.metrics import accuracy_score
print('Accuracy_Score:', accuracy_score(y_pred,y_test))

