import matplotlib.pyplot as plt
import numpy as np 
import mplcursors
from typing import List
from matplotlib.colors import ListedColormap
from matplotlib.lines import Line2D

#Visualization type: Line Graph 
class Visualizer: 
  """
  This class uses the data from data_processor.py and algorthims from algorithms.py to visualize the data in 3 different ways ways:
  1. Line Graph: This displays hurricane wind speed over time with predictions of future hurricane wind speeds.
  2. Scatter Plot: This displays the impact of wind speeds on economic damage across different severity clusters.
  3. Bar Graph: This displays wind speed with anomalies (hurricanes with low windspeeds and high damage) highlighted.
  """

  """
  This method creates a line graph that displays hurricane wind speed over time with predictions of future hurricane wind speeds.
   - Takes in the processed data and stores it in to lists of wind speeds, years, and damage.
   - Takes in the predicted winds speeds data using the WindSpeedPredictor class from algorithms.py and stores it in a list.
   - Stores a list of predicted years starting from 2024 incrementing by 1 for each predicted wind speed.
   - Uses matplotlib to create a line graph that displays observed wind speeds and predicted wind speeds.
   - Uses mplcursors to display the damage when hovering over the data points for our interactive asspect.
  """
  @staticmethod
  def plot_windspeed_trend(data: List[List[float]], predictions: List[float]) -> None:
    windSpeeds = [item[0] for item in data]
    years = [item[1] for item in data]
    damage = [item[2] for item in data]
    predictYears = []
    startPredict = 2024
    for _ in predictions:
      startPredict = startPredict + 1
      predictYears.append(startPredict)
    plt.figure(figsize=(10, 6))
    line = plt.plot(years, windSpeeds, label='Observed Wind Speeds', color='blue')
    plt.plot(predictYears, predictions, label='Predicted Wind Speeds', color='red' )
    plt.xlabel('Year')
    plt.ylabel('Wind Speed (kph)')
    plt.title('Hurricane Wind Speed Over Time with Predictions')
    plt.legend()
    plt.grid(True)
    cursor = mplcursors.cursor(line, hover=True)
    @cursor.connect("add")
    def on_hover(sel):
      sel.annotation.set_text(f"Damage: ${damage[int(sel.index)]} ")
    plt.show()

  """
  This method creates a scatter plot that displays the impact of wind speeds on economic damage across different severity clusters.
   - Takes in the processed data and stores it in to lists of wind speeds, years, and damage.
   - Takes the wind speeds, years, and damage data lists and converts them into numpy arrays (so that it can be filtered using mask).
   - Takes in the clustered data using the HurricaneClustering class from algorithms.py and converts it into a numpy array (so that it can be filtered using mask).
   - Creates a mask that is set to True if the damage is not equal to 0, eliminating the hurricanes with no documented damage.
   - Uses the mask on damage, wind speeds, years, and cluster data to filter out the hurricanes with no documented damage.
   - Uses listed colormap to create a color map for the clusters since the default was difficult to see and didn't make sense for our data.
   - Uses matplotlib to create a scatter plot that displays the wind speeds(x) and damage(y) with the clusters color coded (0 as blue and 1 as red).
   - Uses mplcursors to display the year when hovering over the data points for our interactive asspect.
  """
  @staticmethod
  def plot_clustered_data(data: List[List[float]], clusterData: List[float]) -> None:
    windSpeeds = [item[0] for item in data]
    years = [item[1] for item in data]
    damage = [item[2] for item in data]
    plt.figure(figsize=(10, 6))
    windSpeeds = np.array(windSpeeds)
    years = np.array(years)
    damage = np.array(damage)
    clusterData = np.array(clusterData)
    mask = damage != 0
    damage_filtered = damage[mask]
    windSpeeds_filtered = windSpeeds[mask]
    years_filitered = years[mask]
    labels_filtered = clusterData[mask]
    colors= ['blue', 'red']
    cmap = ListedColormap(colors)
    scatter = plt.scatter(damage_filtered, windSpeeds_filtered, c=labels_filtered, cmap=cmap, s=50)
    legend_elements = [
      Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label='Cluster 0'),
      Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label='Cluster 1'),
    ]
    plt.legend(handles=legend_elements, title='Cluster Key')
    plt.xlabel('Damage (USD)')
    plt.ylabel('Wind Speed (kph)')
    plt.title('Hurricane Wind Speed impact on Economic Damage across Different Severity Clusters ')
    plt.grid(True)
    cursor = mplcursors.cursor(scatter, hover=True)
    @cursor.connect("add")
    def on_hover(sel):
      sel.annotation.set_text(f"Year: {int(years_filitered[sel.index])}")
    plt.show()
  
  """
  This method creates a bar graph that displays wind speed with anomalies (hurricanes with low windspeeds and high damage) highlighted.
   - Takes in the processed data and stores it in to lists of wind speeds and damage.
   - Uses the windspeeds length to create a list of indices for the x-axis.
   - Uses matplotlib to create a bar graph that displays the wind speeds over time
   - Stores the indiceis where anomalies are found using the annomalies list from HurricaneAnomalyDetector class from algorithms.py.
   - Stores the anomaly values using the wind speeds list and the indices of the anomalies.
   - Uses matplotlib to change the color of the anomalies to red.
   - Uses mplcursors to display the damage when hovering over the data points for our interactive asspect.
  """
  @staticmethod
  def plot_anomalies(data: List[List[float]], anomalies: List[bool]) -> None:
    windSpeeds = [item[0] for item in data]
    damage = [item[2] for item in data]
    indices = list(range(len(windSpeeds)))
    plt.figure(figsize=(10, 6))
    bars = plt.bar(indices, windSpeeds, color='blue')
    anomaly_indices = [i for i, is_anomaly in enumerate(anomalies) if is_anomaly == -1]
    anomaly_values = [windSpeeds[i] for i in anomaly_indices]
    print(anomaly_indices)
    plt.bar(anomaly_indices, anomaly_values, color='red', label='Anomalies')
    plt.xlabel('Index')
    plt.ylabel('Wind Speed (kph)')
    plt.title('Wind Speed with Anomalies')
    plt.legend()
    cursor = mplcursors.cursor(bars, hover=True)
    @cursor.connect("add")
    def on_hover(sel):
      sel.annotation.set_text(f"Damage: ${damage[sel.index]}")
    plt.show()