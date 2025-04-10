from sklearn.base import BaseEstimator, RegressorMixin, ClusterMixin, OutlierMixin
from sklearn.cluster import KMeans
from sklearn.neighbors import LocalOutlierFactor
from sklearn.linear_model import LinearRegression
import numpy as np

'''
The WindSpeedPredictor is a custom wind speed predictor using linear regression.
- Initializes a LinearRegression model.
- Provides the methods to train the LinearRegression model and make predictions
'''
class WindSpeedPredictor(BaseEstimator, RegressorMixin):
    '''
    Initializes the WindSpeedPredictor class by initializing the LinearRegression model
    '''
    def __init__(self):
        self.model = LinearRegression()

    '''
    Fits the Linear Regression model to the training data.

    Parameters:
    - X: np.array, features from the data processor
    - y: np.array, target from the data processor

    '''
    def fit(self, X, y):
        # trains the linear regression model with features X and target y
        self.model.fit(X, y)
        return self
    
    '''
    Predicts target values using our trained model.

    Parameters:
    - X: np.array, features from the data processor so it can make predictions

    Returns:
    - a np.array to make predictions on new data called X
    '''
    def predict(self, X):
        return self.model.predict(X)
'''
This class creates a custom clustering model for our data using KMeans.
'''    
class HurricaneClustering(BaseEstimator, ClusterMixin):
    '''
    Intializes the Hurricane Clustering Class

    Parameters:
    - n_clusters: int, defaults to 2
    '''
    def __init__(self, n_clusters=2):
        self.n_clusters = n_clusters    # number of clusters
        self.model = KMeans(n_clusters=self.n_clusters) # initializes KMeans
        print(f"Self Model = {self.n_clusters}")

    '''
    Fits the KMeans model to the data
    
    Parameters:
    - X: np.array, all the data we need from the data processor
    - y: not used for the clustering algorithm
    '''
    def fit(self, X, y=None):
        self.model.fit(X)
        return self
    
    '''
    Predicts the clusters for the new data points.

    Parameters:
    - X: np.array: data to assign to clusters
    
    Returns:
    - the cluster labels for each data point represented as
        (0,1,2,...)
    '''
    def predict(self, X):
        return self.model.predict(X)
'''
Hurricane Anomaly Detector detects anomalies using Local Outlier Factor
- Detects anomalies based on features like wind speed and damage
- Provides methods to fir the model and predict anomalies in the data

Local Outlier Factor detects anomalies based on the neighbors of a data point.
So storms that have low wind speeds and high damages or storms that have high wind speed
and low damages compared to their neighbors.
'''
class HurricaneAnomalyDetector(BaseEstimator, OutlierMixin):
    '''
    Intializes the HurricaneAnomalyDetector

    Parameters:
    - contamination: float, default is 0.1 which is the
    expected amount of our dataset that will have anomalies
    '''
    def __init__(self, contamination=0.1):
        self.contamination = contamination
        self.model = LocalOutlierFactor(contamination=self.contamination)

    '''
    Fits the model to the hurricane data in a similar way as clustering
    '''
    def fit(self, X, y=None):
        self.model.fit(X)
        return self
    
    '''
    Predicts anomalies based on the data using Local Outlier Factor
    which compares a data points data to that of its neightbors data
    to find anomalies.

    Parameters:
    - X: np.array, input data to evaluate for the anomalies

    Returns:
    - An array where anomalies are stored as -1 and 1 indicates a normal data point.

    '''
    def predict(self, X):
        return self.model.fit_predict(X)