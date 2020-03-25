---
layout: post
title: "Research Notes2: Model Persistence Issue in Machine Learning"
date: 2020-03-24 18:16
comments: true
categories: 科研
---

## Introduction

Today I met this problem and had to slow down my work to rerun some of my models to make sure everything works as expected when I tried to train the machine learning model. The problem is that when I trained the neural network, I forgot to save the preprocessing results like the `MinMaxScaler()` I used, so this caused a huge problem that I had to retrain everything to make sure the model works correctly. 

## Deploy Machine Learning Models

Although this is not an error, it is a big pitfall in your typical training of machine learning. The typical machine learning course tends to focus on the algorithm and mathematical reasoning behind the model, it does not tell you how to deploy the model. This is reasonable because actually nowadays, there are no golden rules about how to deploy machine learning models.

Deploying a machine learning model is still at its stone ages. The problem is even harder to solve if you take the software dependency issues into consideration. For example, after you trained a good machine learning model, how could you provide it to the public? Assuming there are $$10^6$$ users who want to use your service, how could you optimize the codes to reduce the latency and computing workload? How to help the user input the correct format of their own data? Is there any method to deal with vicious intention users?

Actually, if we want to go deeper into the ideas of deploying your machine learning model, it will go to the area of computer systems which is rapidly changing and actively researched areas of computer science. Taking one example, I learned one course in UW-Madison that is taught by Prof. Shivaram Venkataraman in Fall 2018, [CS 744 Big Data Systems - UW Madison, Fall 2018](http://pages.cs.wisc.edu/~shivaram/cs744-fa18/), you can find an entire section goes to how to deploy machine learning models online, e.g. [Ray: A Distributed Framework for Emerging AI Applications](http://pages.cs.wisc.edu/~shivaram/cs744-readings/ray-arxiv.pdf).

![Deploy Machine Learning Models in CS 744](/images/MinMaxScaler/cs744.png)

Check out the articles interested to you.

## Model Persistence

So go back to this article, I want to talk about model persistence and how to make sure you have gotten everything you needed. Generally, it is about tips to help you save the training results successfully.

So three things I think we need to store are:

> Preprocessing Results 

> Neural Network Results

> Training logs

#### Preprocessing Results 

For preprocessing results, I think we can use `pickle` and `joblib` to save models.

Below is a code demos from [3.4. Model persistence](https://scikit-learn.org/stable/modules/model_persistence.html)

```python

from sklearn import svm
from sklearn import datasets
clf = svm.SVC()
X, y= datasets.load_iris(return_X_y=True)
clf.fit(X, y)

# Using Pickle
import pickle
s = pickle.dumps(clf)
clf2 = pickle.loads(s)
clf2.predict(X[0:1])

```

Another example about using `joblib`

```python

from joblib import dump, load
# Save Model
dump(clf, 'filename.joblib')

# Load Saved Model
clf = load('filename.joblib') 

```

####  Neural Network Results

This part is typical, there are two key things you need to keep in mind, one is the structure of your neural network, another one is the weights of your neural network. Structure is usually stored in `json` format since it is a layered data structure and weight is usually stored in `h5` format since it is pure number and typically is large. 

Code demos of saving models and commented last section is about how to load saved models

```python

# construct the argument parser and parse the arguments this will be needed for saving results in a different folder
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--savedResults", type=str, required=True,
help="path to save results of both model and weights")

# create results file when needed
if not os.path.exists(args["savedResults"]):
    os.makedirs(args["savedResults"])

# serialize model to JSON
model_json = model.to_json()
with open(args["savedResults"] + "/model_structure.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights(args["savedResults"]+"/model_weights.h5")
print("Saved model to disk")

# In case needs to reload the model

"""
# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")
"""

```

#### Training logs

Following the same logic in saving neural network training results, we will use the following code to save training logs.

```python

# construct the argument parser and parse the arguments this will be needed for saving results in a different folder
ap = argparse.ArgumentParser()
ap.add_argument("-l", "--trainingLog", type=str, required=True,help="path to save training logs and metrics curves")

if not os.path.exists(args["trainingLog"]):
    os.makedirs(args["trainingLog"])

# train the model
print("[INFO] training model...")
history = model.fit(X_train, y_train_scaled, validation_data=(X_test, y_test_scaled), epochs=300, batch_size=64)

# Plot the training Processing
# https://keras.io/visualization/
# list all data in history
print(history.history.keys())

# Plot training & validation loss values
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper right')
plt.savefig(args["trainingLog"]+"/loss.png", dpi=150)
plt.close()

```