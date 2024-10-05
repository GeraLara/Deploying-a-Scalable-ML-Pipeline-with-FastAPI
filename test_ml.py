import pytest
# TODO: add necessary import
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from ml.model import train_model

# TODO: implement the first test. Change the function name and input as needed
def test_one():
    """
    # Testing to see if the dataset size of the training and test are the expected size. 
    """
    X = pd.DataFrame(np.random.rand(100, 5))
    y = pd.Series(np.random.randint(0, 2, size = 100))

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 30)

    assert X_train.shape[0] == int(0.8 * X.shape[0])  # Test train size
    assert X_test.shape[0] == int(0.2 * X.shape[0])   # Test test size

    pass

def train_model(X_train, y_train):
    
    model = RandomForestClassifier(n_estimators = 100, random_state = 30)
    model.fit(X_train, y_train)

    return model

# TODO: implement the second test. Change the function name and input as needed
def test_two():
    """
    # Testing to see if the ML function returns the expected type
    """
    X = pd.DataFrame(np.random.rand(100, 5))
    y = pd.Series(np.random.randint(0, 2, size = 100))

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 30)

    model = train_model(X_train, y_train)
    assert isinstance(model, RandomForestClassifier)

    pass

def inference(model, X_test):
    return model.predict(X_test)

# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    # Testing to see if the inference returns a array
    """
    X = pd.DataFrame(np.random.rand(100, 5))
    y = pd.Series(np.random.randint(0, 2, size = 100))
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 30)

    model = train_model(X_train, y_train)
    prediction = inference(model, X_test)
    assert isinstance(prediction, np.ndarray)

    pass
