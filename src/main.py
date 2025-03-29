import pandas as pd
from data_processor import DataProcessor

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
  x, y = processor.get_features_and_target()
# prints the first 5 features or targets for testing
  print("Features: ", x[:5])
  print("Target:", y[:5])

  # Temperature prediction


  # Clustering


  # Anomaly detection


if __name__ == "__main__":
  main()