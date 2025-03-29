import pandas as pd
import numpy as np

class DataProcessor:
  # simple just intializing the file path and the data frame
  def __init__(self, file_path: str):
    self.file_path = file_path
    self.df = None
  # read the csv and put it in the self.df DataFrame
  def load_data(self) -> pd.DataFrame:
    self.df = pd.read_csv(self.file_path)
    return self.df

  def clean_data(self) -> pd.DataFrame:
    # make sure data has been loaded
    if self.df is None:
       raise ValueError("Data must be loaded before cleaning")
    # edit the DataFrame to sort for all Tropical Cyclones/Hurricanes
    self.df = self.df[(self.df["Disaster Type"] == "Storm") &
                      (self.df["Disaster Subtype"].str.contains("Tropical cyclone", na=False))
                      ]
    # keep only these columns (this can be changed if we need other columns)
    columns_to_keep = [
        "DisNo.", "Disaster Type", "Disaster Subtype", "ISO", "Event Name",
        "Total Deaths", "Total Affected", "Total Damage ('000 US$)", 
        "Total Damage, Adjusted ('000 US$)", "Entry Date", "Last Update"
    ]
    # make data frame only have the columns we want and return
    self.df = self.df[columns_to_keep]
    return self.df
  def get_features_and_target(self) -> tuple[np.ndarray, np.ndarray]:
    # make sure data is clean and loaded
    if self.df is None:
      raise ValueError("Data must be loaded and cleaned before extracting features and target.")
    # gets certain pieces of the data frame
    features = self.df [["Total Deaths", "Total Affected", "Total Damage ('000 US$)"]].fillna(0).values
    # also get the Total Damage adjusted for inflation
    target = self.df["Total Damage, Adjusted ('000 US$)"]. fillna(0).values
    return features, target


# Example usage:
# processor = DataProcessor("data/naturalDisaster.csv")
# processor.load_data()
# processor.clean_data()
# X, y = processor.get_features_and_target()