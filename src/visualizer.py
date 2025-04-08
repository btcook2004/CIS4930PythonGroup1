import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns
import numpy as np 
import mplcursors
from typing import List, Tuple

#Visualization type: Line Graph 
class Visualizer: 
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
    plt.figure(figsize=(8, 6))
    line = plt.plot(years, windSpeeds, label='Observed Wind Speeds', color='blue')
    plt.plot(predictYears, predictions, label='Predicted Wind Speeds', color='red' )
    plt.xlabel('Year')
    plt.ylabel('Wind Speed (kph)')
    plt.title('Wind Speed Trends Over Time')
    plt.legend()
    plt.grid(True)
    cursor = mplcursors.cursor(line, hover=True)
    @cursor.connect("add")
    def on_hover(sel):
      sel.annotation.set_text(f"Damage: ${damage[int(sel.index)]} ")
    plt.show()

#Visualization Type: Scatter Plot
  @staticmethod
  def plot_clustered_data(data: List[List[float]], labels: List[float]) -> None:
    windSpeeds = [item[0] for item in data]
    years = [item[1] for item in data]
    damage = [item[2] for item in data]
    plt.figure(figsize=(10, 6))
    windSpeeds = np.array(windSpeeds)
    years = np.array(years)
    damage = np.array(damage)
    labels = np.array(labels)
    mask = damage != 0
    damage_filtered = damage[mask]
    windSpeeds_filtered = windSpeeds[mask]
    years_filitered = years[mask]
    labels_filtered = labels[mask]
    scatter = plt.scatter(damage_filtered, windSpeeds_filtered, c=labels_filtered)
    plt.xlabel('Damage (USD)')
    plt.ylabel('Wind Speed (kph)')
    plt.title('Clustered Data Visualization')
    plt.colorbar(scatter, label='Cluster Label')
    plt.grid(True)
    cursor = mplcursors.cursor(scatter, hover=True)
    @cursor.connect("add")
    def on_hover(sel):
      sel.annotation.set_text(f"Year: {years_filitered[sel.index]}")
    plt.show()
  

#Visualization Type: Bar Graph
  @staticmethod
  def plot_anomalies(data: List[List[float]], anomalies: List[bool]) -> None:
    windSpeeds = [item[0] for item in data]
    years = [item[1] for item in data]
    damage = [item[2] for item in data]
    indices = list(range(len(windSpeeds)))
    fig, ax = plt.subplots(figsize=(8, 6))
    bars = ax.bar(indices, windSpeeds, color='blue')
    anomaly_indices = [i for i, is_anomaly in enumerate(anomalies) if is_anomaly == -1]
    anomaly_values = [windSpeeds[i] for i in anomaly_indices]
    ax.bar(anomaly_indices, anomaly_values, color='red', label='Anomalies')
    ax.set_xlabel('Index')
    ax.set_ylabel('Wind Speed (kph)')
    ax.set_title('Wind Speed with Anomalies')
    ax.legend()
    cursor = mplcursors.cursor(bars, hover=True)
    @cursor.connect("add")
    def on_hover(sel):
      sel.annotation.set_text(f"Damage: ${damage[sel.index]}")
    plt.show()