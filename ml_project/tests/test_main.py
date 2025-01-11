import pytest
import sys
import os

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.main import load_data

def test_load_data():
    """Test that data loading returns expected shapes"""
    X, y = load_data()
    
    # Check feature matrix shape
    assert X.shape == (150, 4)
    
    # Check target vector shape
    assert y.shape == (150,)
    
    # Check feature names
    expected_features = [
        'sepal length (cm)',
        'sepal width (cm)',
        'petal length (cm)',
        'petal width (cm)'
    ]
    assert list(X.columns) == expected_features