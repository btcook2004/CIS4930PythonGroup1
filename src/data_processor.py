import pandas as pd
import numpy as np

class DataProcessor:
  '''
  def __init__(self, file_path:str) intitalizes the file path as the user input
  and then initializes the data frame
  '''
  def __init__(self, file_path: str):
    self.file_path = file_path
    self.df = None
  '''
  def load_data(self) -> pd.DataFrame loads data from a csv into
  a DataFrame from pandas.
  - First it tries to read the file at the path specificed by self.file_path
  - If the file isn't found, it prints the error message.
  - If any other kind of exception happens it prints a generic error.
  - On a success, it stores the DataFrame in self.df and returns it.
  '''
  def load_data(self) -> pd.DataFrame:
    try:
      # Attempt to read the csv
      self.df = pd.read_csv(self.file_path)
    except FileNotFoundError:
      # If the file isn't found
      print(f"File not found: {self.file_path}")
    except Exception as e:
      # Handles any other errors that occur when loading
      print(f"Error loading file: {self.file_path}")
    return self.df
  '''
  This method cleans the loaded DataFrame by:
  - Checking if the data was loaded. If not it raises an error.
  - Filters the DataFrame to only include tropical cyclones and hurricanes
  - Keeps only the relevant columns from the csv
  - Removes rows where the "Magnitude" is missing or a zero
  - Lastly it returns the DataFrame
  '''
  def clean_data(self) -> pd.DataFrame:
    # make sure data has been loaded
    if self.df is None:
       raise ValueError("Data must be loaded before cleaning")
    # filter the DataFrame to sort for all Tropical Cyclones/Hurricanes
    self.df = self.df[(self.df["Disaster Type"] == "Storm") &
                      (self.df["Disaster Subtype"].str.contains("Tropical cyclone", na=False))
                      ]
    # keep the columns that are useful from the csv
    columns_to_keep = [
        "DisNo.", "Disaster Type", "Start Year", "Disaster Subtype", "ISO", "Event Name", "Magnitude", "Magnitude Scale",
        "Total Deaths", "Total Affected", "Total Damage ('000 US$)", 
        "Total Damage, Adjusted ('000 US$)"
    ]
    # make the DataFrame set to the columns_to_keep
    self.df = self.df[columns_to_keep]
    # removes the rows for Magnitude where it is NaN or zero
    self.df = self.df[self.df["Magnitude"].notna() & (self.df["Magnitude"] != 0)]
    
    return self.df
  '''
  def get_features_and_target(self) extracts the features and traget variables from the DataFrame
  - It first checks if the data has been loaded and cleaned
  - The features are: Magnitude, Start Year, and Total Damage, Adjusted ('000 US$)
  - The target is Magnitude
  - Any missing values in the features and target where replaced with a zero
  - Returns the tuple that has both the features and the target as numPy arrays
  '''
  def get_features_and_target(self) -> tuple[np.ndarray, np.ndarray]:
    # make sure data is clean and loaded
    if self.df is None:
      raise ValueError("Data must be loaded and cleaned before extracting features and target.")
    
    # Get the features we want from the data and fill missing values with 0 and turn into a numPy array
    features = self.df [["Magnitude", "Start Year", "Total Damage, Adjusted ('000 US$)"]].fillna(0).values

    # Get the target variable and set missing values to zero while also making it a numPy array
    target = self.df["Magnitude"]. fillna(0).values
    return features, target