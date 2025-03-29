import pandas as pd
import numpy as np

class DataProcessor:
  def __init__(self, file_path: str):
    """Initialize DataProcessor with file path."""
    self.file_path = file_path
    self.data = None
    self.features = None
    self.target = None
    self.load_data()
    self.clean_data()
    self.get_features_and_target()
    ...
  def load_data(self) -> pd.DataFrame:
    """Load climate data from CSV file."""
    try:
      self.data = pd.read_csv(self.file_path)
      print(f"Data loaded successfully from {self.file_path}")
    except FileNotFoundError:
      print(f"File not found: {self.file_path}")
      raise
    except pd.errors.EmptyDataError:
      print("No data found in the file.")
      raise
    except pd.errors.ParserError:
      print("Error parsing the data.")
      raise
    except Exception as e:
      print(f"An error occurred: {e}")
      raise
    return self.data
    ...
  def clean_data(self) -> pd.DataFrame:
    """Remove rows with missing values and normalize temperature data."""
    if self.data is None:
      print("Data not loaded. Cannot clean data.")
      return
    # Remove rows with missing values
    self.data.dropna(inplace=True)
    # Normalize temperature data
    self.data['temperature'] = (self.data['temperature'] - self.data['temperature'].mean()) / self.data['temperature'].std()
    # Convert year and month to categorical data
    self.data['year'] = self.data['year'].astype('category')
    self.data['month'] = self.data['month'].astype('category')
    # Remove unnecessary columns
    self.data.drop(columns=['unnecessary_column1', 'unnecessary_column2'], inplace=True, errors='ignore')
    # Rename columns for consistency
    self.data.rename(columns={'temperature': 'temp', 'year': 'yr', 'month': 'mth'}, inplace=True)
    # Reset index
    self.data.reset_index(drop=True, inplace=True)
    print("Data cleaned successfully.")
    return self.data
    ...
  def get_features_and_target(self) -> Tuple[np.ndarray, np.ndarray]:
    """Split data into features (year, month) and target (temperatore)."""
    ...
    