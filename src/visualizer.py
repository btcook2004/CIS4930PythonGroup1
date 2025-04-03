import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns
import numpy as np 
from typing import List, Tuple

#Visualization type: Line Graph 
class Visualizer: #NEEDS TO ACTUALLY PREDICT FUTURE
  @staticmethod
  def plot_windspeed_trend(data: List[List[float]], predictions: List[float]) -> None:
    windSpeeds = [item[0] for item in data]
    years = [item[1] for item in data]
    plt.figure(figsize=(8, 6))
    plt.plot(years, windSpeeds, label='Observed Wind Speeds', color='blue')
    plt.plot(years, predictions, label='Predicted Wind Speeds', color='red', linestyle='--')
    plt.xlabel('Year')
    plt.ylabel('Wind Speed (kph)')
    plt.title('Wind Speed Trends Over Time')
    plt.legend()
    plt.grid(True)
    plt.show()

#Visualization Type: Scatter Plot
  @staticmethod
  def plot_clustered_data(data: List[List[float]], labels: List[float]) -> None:
    y = [item[0] for item in data]
    x = [item[1] for item in data]
    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(x, y, c=labels, cmap='viridis', edgecolor='k')
    plt.xlabel('Year')
    plt.ylabel('Wind Speed (kph)')
    plt.title('Clustered Data Visualization')
    plt.colorbar(scatter, label='Cluster Label')
    plt.grid(True)
    plt.show()

#Visualization Type: Bar Graph
  @staticmethod
  def plot_anomalies(data: List[List[float]], anomalies: List[bool]) -> None:
    windSpeeds = [item[0] for item in data]
    years = [item[1] for item in data]
    indices = list(range(len(windSpeeds)))
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(indices, windSpeeds, color='blue')
    anomaly_indices = [i for i, is_anomaly in enumerate(anomalies) if is_anomaly == -1]
    anomaly_values = [windSpeeds[i] for i in anomaly_indices]
    ax.bar(anomaly_indices, anomaly_values, color='red', label='Anomalies')
    ax.set_xlabel('Index')
    ax.set_ylabel('Wind Speed (kph)')
    ax.set_title('Wind Speed with Anomalies')
    ax.legend()
    plt.show()

    # windSpeeds = [item[0] for item in data]
    # years = [item[1] for item in data]
    # indices = list(range(len(years)))
    # fig, ax = plt.subplots(figsize=(8, 6))
    # ax.bar(years, windSpeeds, color='blue')
    # anomaly_indices = [i for i, is_anomaly in enumerate(anomalies) if is_anomaly == -1]
    # anomaly_values = [windSpeeds[i] for i in anomaly_indices]
    # selectedYears = [years[i] for i in anomaly_indices] 
    # print(selectedYears) 
    # ax.bar(selectedYears, anomaly_values, color='red', label='Anomalies')
    # ax.set_xlabel('Index')
    # ax.set_ylabel('Wind Speed (kph)')
    # ax.set_title('Wind Speed Predictions with Anomalies')
    # ax.legend()
    # plt.show()
    
# if __name__ == "__main__":
#   #trend vs predicted test
#   years = [2000, 2001, 2002, 2003, 2004, 2005]
#   temperatures = [14.1, 14.3, 14.5, 14.6, 14.8, 15.0]
#   predictions = [14.2, 14.4, 14.6, 14.7, 14.9, 15.1] 
#   Visualizer.plot_temperature_trend(years, temperatures, predictions)

# #cluster test
# data = [(1, 2), (2, 3), (3, 4), (10, 10), (11, 12), (12, 13)]
# labels = [0, 0, 0, 1, 1, 1] 
# Visualizer.plot_clustered_data(data, labels)

#   #anomalies test
#   time_series = [10, 12, 13, 15, 50, 13, 12, 11, 10, 50, 12, 13, 14, 15, 16]
#   anomalies = [False, False, False, False, True, False, False, False, False, True, False, False, False, False, False]
#   Visualizer.plot_anomalies(time_series, anomalies)