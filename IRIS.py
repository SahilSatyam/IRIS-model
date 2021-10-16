import streamlit as st
st.title("Iris Dataset API")

#webpage
sl = st.slider('What is the sepal length?', 4.3, 7.9, 5.1)
sw = st.slider('What is the sepal width?', 4.5, 3.5, 2.2)
pl = st.slider('What is the petal length?', 1.0, 6.9, 5.5)
pw = st.slider('What is the petal width?', 0.1, 2.5, 2.2)

#Model
from sklearn.datasets import load_iris
iris=load_iris()
#iris.keys()
from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier()
model.fit(iris.data,iris.target)
op=model.predict([[sl,sw,pl,pw]])
op=iris.target_names[op[0]]
st.title(f"The flower species is {op}")

