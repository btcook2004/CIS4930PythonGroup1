import unittest
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from src.algorithms import WindSpeedPredictor  
"""
Tests the WindSpeedPredictor class to ensure that it:
- Correctly initializes a LinearRegression model
- Correctly fits the model to the training data
- Correctly generates predictions by ensureing the number of predictions matches the number of test samples
- Correctly returns predictions as a numpy array by ensuring predictions are of type np.array
"""
class TestWindSpeedPredictor(unittest.TestCase):
    def setUp(self):
        X = np.array([[10, 30], [20, 60], [30, 90], [40, 120], [50, 150]])
        y = np.array([100, 200, 300, 400, 500])
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model = WindSpeedPredictor()
        
    def test_model_initialization(self):
        self.assertIsInstance(self.model.model, LinearRegression)
    
    def test_fit_method(self):
        self.model.fit(self.X_train, self.y_train)
        # Check if the inner LinearRegression model has been fitted
        self.assertTrue(hasattr(self.model.model, 'coef_'))

    def test_predict_method(self):
        self.model.fit(self.X_train, self.y_train)
        predictions = self.model.predict(self.X_test)
        self.assertEqual(predictions.shape[0], self.X_test.shape[0])
    
    def test_predict_output_type(self):
        self.model.fit(self.X_train, self.y_train)
        predictions = self.model.predict(self.X_test)
        self.assertIsInstance(predictions, np.ndarray) 

if __name__ == '__main__':
    unittest.main()
