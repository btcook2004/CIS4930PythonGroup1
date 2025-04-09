import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from data_processor import DataProcessor
from algorithms import WindSpeedPredictor, HurricaneClustering, HurricaneAnomalyDetector
from visualizer import Visualizer 
# from src.algorithms import CustomTemperaturePredictor, custom_clustering, detect_anomalies
# from src.visualizer import Visualizer

def main():
  # ...

  # #Load and preprocess data
  # ...

  # if args.action == "predict":
  #   ...
  # elif args.action == "cluster":
  #   ...
  # elif args.action == "anomalies":
  #   ...

  clean_data = None

  while True:
    print("\nCLIMATE CHANGE IMPACT ANALYZER")
    print("1) Load Data")
    print("2) View Data")
    print("3) Exit")
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
      file_path = input("Please enter in the file path for your data (.csv): ")
      processor = DataProcessor(file_path)
      processor.load_data()
      
      if processor.df is not None and not processor.df.empty:
         clean_data=processor.clean_data()
         x, y = processor.get_features_and_target()
         X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=2)
         print("\nData loaded successfully!")
      else:
         print("\nFailed to load data. Please check your file path.")

      
    elif choice == "2":
      if clean_data is None:
         print("\n Please load a .csv file in first.")
         continue

      while True:
         print("\nVIEW DATA MENU")
         print("1) List clean .csv data")
         print("2) List wind speed trends")
         print("3) List clustered data")
         print("4) List anomalies")
         print("5) Exit to main menu")
         view_choice = input("Enter your choice (1-5): ")

         if view_choice == "1":
            pd.set_option('display.max_rows', None)
            pd.set_option('display.max_columns', None)
            print(clean_data)

         elif view_choice == "2":
            model = WindSpeedPredictor()
            model.fit(X_train, y_train)
            predictions = model.predict(X_test)
            Visualizer.plot_windspeed_trend(X_test, predictions) 

         elif view_choice == "3":
            clustering = HurricaneClustering(n_clusters=2)
            clustering.fit(X_train)
            Visualizer.plot_clustered_data(X_test, clustering.predict(X_test))

         elif view_choice == "4":
            n_neighbors = min(10, len(X_train) - 1)
            anomaly_detector = HurricaneAnomalyDetector(contamination=0.2)
            anomaly_detector.model.set_params(n_neighbors=n_neighbors)
            anomaly_detector.fit(X_train)
            Visualizer.plot_anomalies(X_train, anomaly_detector.predict(X_test))
          
         elif view_choice == "5":
            break
         
         else:
            print("Invalid choice")

    elif choice == "3":
      print("Exiting...")
      break

    else:
      print("Invalid choice, try again")
    
                

if __name__ == "__main__":
        main()