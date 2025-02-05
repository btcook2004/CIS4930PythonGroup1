import matpotlib.pyplot as plt
import seaborn as sns
from typing import List, Tuple

class Visualizer:
  @staticmethod
  def plot_temperature_trend(years: List[int], temperatures: List[float], predictions: List[float]) -> None:
    plt.figure(figsize = (*, *))
    plt.plot(years, temperatures, label='Actual')
    plt.plot(years, predictions, label='Predicted')
    plt.xlabel('Year')
    plt.yLabel('Temperature (normalized)')
    plt.title('Temperature Trend Over Time')
    plt.legend()
    plt.show()

    @staticmethod
    def plot_clustered_data(data: List[Tuple[float, float]], labels: List[int]) -> None:
      ...

    @staticmethod
    def plot_anomalies(time_series: List[float], anomalies: List[bool]) -> None:
      ...
    

