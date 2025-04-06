import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns
import numpy as np 
from typing import List, Tuple

#Visualization type: Line Graph 
class Visualizer: #NEEDS TO ACTUALLY PREDICT FUTURE
  @staticmethod
  def plot_windspeed_trend(data: List[List[float]], predictions: List[float]) -> None:
    print("Testing poop")
    windSpeeds = [item[0] for item in data]
    years = [item[1] for item in data]
    predictYears = []
    startPredict = 2024
    for _ in predictions:
      startPredict = startPredict + 1
      predictYears.append(startPredict)
    plt.figure(figsize=(10, 6))
    plt.plot(years, windSpeeds, label='Observed Wind Speeds', color='blue')
    plt.plot(predictYears, predictions, label='Predicted Wind Speeds', color='red', linestyle='--')
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