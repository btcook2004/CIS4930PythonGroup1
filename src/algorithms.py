# import numpy as np
# from sklearn.base import BaseEstimator, RegressorMixin
# from typing import Tuple

# class CustomTemperaturePredictor(BaseEstimator, RegressorMixin):
#   def __init__(self, learning_rate: float = 0.01, n_iterations: int = 1000):
#     ...
#   def fit(self, X: np.ndarray, y: np.ndarray) -> 'CustomTemperaturePredictor':
#     ...
#   def predict(self, X: np.ndarray) -> np.ndarray:
#     ...
#   def detect_anomalies(time_series: np.ndarray, window_size: int = 10, threshold: float = 2.0) -> np.ndarray:
#     """Detect anomalies in time series data."""
#     ..."

from sklearn.base import BaseEstimator, RegressorMixin, ClusterMixin, OutlierMixin
from sklearn.cluster import KMeans
from sklearn.neighbors import LocalOutlierFactor
from sklearn.linear_model import LinearRegression
import numpy as np

class WindSpeedPredictor(BaseEstimator, RegressorMixin):
    # def __init__(self, method='mean'):
    def __init__(self):
        self.model = LinearRegression()


    def fit(self, X, y):
        self.model.fit(X, y)
        return self
    
    # def predict(self, X):
    #     """Predicts wind speed based on the learned average."""
    #     return np.full((X.shape[0],), self.wind_speed_avg)

    def predict(self, X):
        return self.model.predict(X)
    
class HurricaneClustering(BaseEstimator, ClusterMixin):
    def __init__(self, n_clusters=3):
        self.n_clusters = n_clusters
        self.model = KMeans(n_clusters=self.n_clusters)

    def fit(self, X, y=None):
        """Finds clusters in hurricane data."""
        self.model.fit(X)
        return self
    
    def predict(self, X):
        """Assigns clusters to new data points."""
        return self.model.predict(X)
    
class HurricaneAnomalyDetector(BaseEstimator, OutlierMixin):
    # Anomalies are detect by wind speed and total damage
    def __init__(self, contamination=0.1):
        self.contamination = contamination
        self.model = LocalOutlierFactor(contamination=self.contamination)

    def fit(self, X, y=None):
        """Fits the anomaly detector on hurrricane data."""
        self.model.fit(X)
        return self
    
    def predict(self, X):
        """Predicts anomalies (-1 means anomaly, 1 means normal)."""
        return self.model.fit_predict(X)
    

# # Example usage
# X_train = np.array([[1], [2], [3]])
# y_train = np.array([80, 85, 90])
# model = WindSpeedPredictor()
# model.fit(X_train, y_train)
# print(model.predict([[4], [5]]))

# X_cluster = np.array([[80, 950], [100, 940], [120, 930]])
# clustering = HurricaneClustering(n_clusters=2)
# clustering.fit(X_cluster)
# print(clustering.predict([[110, 935]]))

# X_anomaly = np.array([[80], [85], [90], [200]])
# anomaly_detector = HurricaneAnomalyDetector(contamination=0.2)
# anomaly_detector.fit(X_anomaly)
# print(anomaly_detector.predict(X_anomaly))

