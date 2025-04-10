import unittest
from mock import patch, MagicMock
from src.visualizer import Visualizer  # Adjust the import path as necessary

"""
Tests the plot_clustered_data method in the Visualizer class to ensure that it:
- Correctly calls plt.scatter() (mock_scatter.assert_called())
- Correctly calls mplcursors.show() (mock_show.assert_called_once())
- Correctly calls mplcursors.cursor() (mock_cursor_instance.connect.assert_called())
"""
class TestPlottingMethods(unittest.TestCase):
    def setUp(self):
        self.data = [
            [100, 2020, 50000],
            [120, 2021, 100000],
            [150, 2022, 200000]
        ]
        self.clusterData = [0, 1, 0] 
        
    @patch("matplotlib.pyplot.show")
    @patch("matplotlib.pyplot.scatter")
    @patch("mplcursors.cursor")
    def test_plot_clustered_data(self, mock_cursor, mock_scatter, mock_show):
        mock_cursor_instance = MagicMock()
        mock_cursor.return_value = mock_cursor_instance
        Visualizer.plot_clustered_data(self.data, self.clusterData)
        mock_scatter.assert_called()
        mock_show.assert_called_once()
        mock_cursor_instance.connect.assert_called()

if __name__ == '__main__':
    unittest.main()
