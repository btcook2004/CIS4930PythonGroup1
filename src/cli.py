import pandas as pd
from sklearn.model_selection import train_test_split
from data_processor import DataProcessor
from algorithms import WindSpeedPredictor, HurricaneClustering, HurricaneAnomalyDetector
from visualizer import Visualizer 

def display_main_menu():
    print("\nCLIMATE CHANGE IMPACT ANALYZER")
    print("1) Load Data")
    print("2) View Data")
    print("3) Exit")

def display_view_menu():
    print("\nVIEW DATA MENU")
    print("1) List clean .csv data")
    print("2) List wind speed trends")
    print("3) List clustered data")
    print("4) List anomalies")
    print("5) Exit to main menu")

"""
def handle_load_data() prompts the user to enter in a CSV file path and processes the data set
using DataProcessor from our data_processor.py file.
- First, it prompts the user to enter a file path for the CSV.
- It initializes an instance of DataProcessor using the input for file_path.
- Next, it calls load_data from data_processor.py.
- If the data frame is not empty,
   - clean_data() from data_processor.py is called to clean the data set.
   - get_features_and_target() from data_processor.py is called to extract features and target values.
   - Using train_test_split() from data_processor.py, the features and target values are 
   split into training and testing sets.
   - The cleaned data set, features and target values, and the train/test sets are returned.
- If the data set is empty or an incorrect file_path is inputted, 
an error message is displayed and nothing is returned.
"""
def handle_load_data():
    file_path = input("Please enter the file path for your data (.csv): ")
    processor = DataProcessor(file_path)
    processor.load_data()

    if processor.df is not None and not processor.df.empty:
        clean_data = processor.clean_data()
        x, y = processor.get_features_and_target()
        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=2)
        print("\nData loaded successfully!")
        return clean_data, x, y, X_train, X_test, y_train, y_test
    else:
       print("\nFailed to load data. Please check your file path.")
       return None, None, None, None, None, None, None
"""
def handle_view_data(clean_data, x, X_train, X_test, y_train) displays a menu for the user to interact with and see visualizations.
- If clean_data is None, it prompts the user to load a .csv file first.
- Otherwise, enter a loop that prompts the user to choose between four options and exiting back into the main menu.
- 1. Displays the entire cleaned data set with all the rows and columns.
- 2. Trains our WindSpeedPredictor model on the training data and displays a visual for wind speed trends.
- 3. Applies KMeans clustering to the training data and displays the clustered data points.
- 4. Uses our HurricaneAnomalyDetector algorithm on the training data and displays the anomalies.
- 5. Exits back into the main menu.
"""
def handle_view_data(clean_data, x, X_train, X_test, y_train):
    if clean_data is None:
        print("\nPlease load a .csv file first.")
        return

    while True:
        display_view_menu()
        view_choice = input("Enter your choice (1-5): ")

        if view_choice == "1":
            pd.set_option('display.max_rows', None)
            pd.set_option('display.max_columns', None)
            print(clean_data)

        elif view_choice == "2":
            model = WindSpeedPredictor()
            model.fit(X_train, y_train)
            Visualizer.plot_windspeed_trend(x, model.predict(X_test))

        elif view_choice == "3":
            clustering = HurricaneClustering(n_clusters=2)
            clustering.fit(X_train)
            Visualizer.plot_clustered_data(x, clustering.predict(x))

        elif view_choice == "4":
            n_neighbors = min(10, len(X_train) - 1)
            anomaly_detector = HurricaneAnomalyDetector(contamination=0.2)
            anomaly_detector.model.set_params(n_neighbors=n_neighbors)
            anomaly_detector.fit(X_train)
            Visualizer.plot_anomalies(x, anomaly_detector.predict(x))
          
        elif view_choice == "5":
            break

        else:
            print("Invalid choice, try again.")

def main():
  clean_data = None
  x = None 
  y = None 
  X_train = None 
  X_test = None 
  y_train = None 
  y_test = None

  while True:
    display_main_menu()
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
       clean_data, x, y, X_train, X_test, y_train, y_test = handle_load_data()

    elif choice == "2":
       handle_view_data(clean_data, x, X_train, X_test, y_train)

    elif choice == "3":
       print("Exiting...")
       break

    else:
       print("Invalid choice, try again")
    
if __name__ == "__main__":
    main()