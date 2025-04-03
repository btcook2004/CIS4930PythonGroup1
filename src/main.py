import pandas as pd
from data_processor import DataProcessor
from algorithms import WindSpeedPredictor, HurricaneClustering, HurricaneAnomalyDetector
from visualizer import Visualizer 
def main():
  # Load and preprocess data
  file_path = "data/naturalDisaster.csv"
  processor = DataProcessor(file_path)
  processor.load_data()
  clean_data=processor.clean_data()
# prints all the data looks weird though
  pd.set_option('display.max_rows', None)  # Show all rows
  pd.set_option('display.max_columns', None)  # Shows all columns
  print(clean_data)
  X_train, y_train = processor.get_features_and_target()
# prints the first 5 features or targets for testing
  print("Features: ", X_train[:15])
  print("Target:", y_train)

# Temperature prediction

# Clustering



  # Anomaly detection

  #Wind speed stuff
  #test = X_train[:15] if len(X_train) > 15 else X_train
  model = WindSpeedPredictor()

  model.fit(X_train, y_train)
  print("Wind Speed: ", model.predict(X_train))

  clustering = HurricaneClustering(n_clusters=2)
  clustering.fit(X_train)
  print("Clustering: ",clustering.predict(X_train))

  n_neighbors = min(10, len(X_train) - 1)
  anomaly_detector = HurricaneAnomalyDetector(contamination=0.2)
  anomaly_detector.model.set_params(n_neighbors=n_neighbors)
  anomaly_detector.fit(X_train)
  print("Anomalies: ", anomaly_detector.predict(X_train))

  #Anomalies graph
  Visualizer.plot_anomalies(X_train, anomaly_detector.predict(X_train))
  #clustering graph
  Visualizer.plot_clustered_data(X_train, clustering.predict(X_train))
  #Predictions Graph
  Visualizer.plot_windspeed_trend(X_train,model.predict(X_train))



if __name__ == "__main__":
  main()