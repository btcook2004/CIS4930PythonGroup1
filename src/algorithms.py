from sklearn.base import BaseEstimator, RegressorMixin, ClusterMixin, OutlierMixin
from sklearn.cluster import KMeans
from sklearn.neighbors import LocalOutlierFactor
from sklearn.linear_model import LinearRegression
import numpy as np

class WindSpeedPredictor(BaseEstimator, RegressorMixin):
    def __init__(self):
        self.model = LinearRegression()

    def fit(self, X, y):
        self.model.fit(X, y)
        return self
    
    def predict(self, X):
        return self.model.predict(X)
    
class HurricaneClustering(BaseEstimator, ClusterMixin):
    def __init__(self, n_clusters=2):
        self.n_clusters = n_clusters
        self.model = KMeans(n_clusters=self.n_clusters)
        print(f"Self Model = {self.n_clusters}")

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