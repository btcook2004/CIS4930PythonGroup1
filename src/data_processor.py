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
  # since out data doesn't have category of hurricane we use the magnitude of the storm
  # which is wind speed in kph to determine category
  # if there is no wind speed given the storm is classified as a depression
  def hurricane_cat(magnitude):
    if 63 <= magnitude < 119:
      return "Tropical Storm"
    elif 119 <= magnitude < 154:
      return "Category 1"
    elif 154 <= magnitude < 178:
      return "Category 2"
    elif 178 <= magnitude < 209:
      return "Category 3"
    elif 209 <= magnitude < 252:
      return "Category 4"
    elif magnitude >= 252:
      return "Category 5"
    else:
      return "Depression"
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
        "DisNo.", "Disaster Type", "Start Year", "Disaster Subtype", "ISO", "Event Name", "Magnitude", "Magnitude Scale",
        "Total Deaths", "Total Affected", "Total Damage ('000 US$)", 
        "Total Damage, Adjusted ('000 US$)"
    ]
    # make data frame only have the columns we want and return
    self.df = self.df[columns_to_keep]
    self.df = self.df[self.df["Magnitude"].notna() & (self.df["Magnitude"] != 0)]
    # adds a Category of Storm section to the csv
    self.df['Hurricane Category'] = self.df['Magnitude'].apply(DataProcessor.hurricane_cat)
    return self.df
  def get_features_and_target(self) -> tuple[np.ndarray, np.ndarray]:
    # make sure data is clean and loaded
    if self.df is None:
      raise ValueError("Data must be loaded and cleaned before extracting features and target.")
    # gets certain pieces of the data frame
    features = self.df [['Magnitude', 'Start Year', "Total Damage ('000 US$)"]].fillna(0).values
    # also get the Total Damage adjusted for inflation
    target = self.df["Magnitude"]. fillna(0).values
    return features, target
# Example usage:
# processor = DataProcessor("data/naturalDisaster.csv")
# processor.load_data()
# processor.clean_data()
# X, y = processor.get_features_and_target()