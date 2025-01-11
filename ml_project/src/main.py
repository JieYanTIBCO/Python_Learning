import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from sklearn.utils import Bunch
from typing import Tuple, cast
import numpy as np

class IrisBunch(Bunch):
    data: np.ndarray
    target: np.ndarray
    feature_names: list[str]
    target_names: list[str]
    DESCR: str

def load_data() -> Tuple[pd.DataFrame, pd.Series]:
    """Load and preprocess the iris dataset
    
    Returns:
        Tuple containing:
        - X: DataFrame with 150 samples and 4 features:
            * sepal length (cm)
            * sepal width (cm)
            * petal length (cm)
            * petal width (cm)
        - y: Series with target labels (0: setosa, 1: versicolor, 2: virginica)
    """
    # Load the classic Iris dataset
    iris = cast(IrisBunch, load_iris())
    
    # Create DataFrame with feature data
    # 150 samples, 4 features each
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    
    # Create Series with target labels
    # 150 corresponding labels (0, 1, or 2)
    y = pd.Series(iris.target)
    
    # Print first 5 samples
    print("\nFirst 5 samples of Iris dataset:")
    print(X.head())
    print("\nCorresponding labels:")
    print(y.head())
    
    return X, y

def preprocess_data(X, y):
    """Preprocess the data"""
    # Split into train/test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Scale features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    """Train a logistic regression model"""
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """Evaluate model performance"""
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy:.2f}")
    return accuracy

def main():
    """Main execution function"""
    # Load and preprocess data
    X, y = load_data()
    X_train, X_test, y_train, y_test = preprocess_data(X, y)
    
    # Train model
    model = train_model(X_train, y_train)
    
    # Evaluate model
    evaluate_model(model, X_test, y_test)

if __name__ == "__main__":
    main()