import unittest
import os
import shutil
import pandas as pd
import numpy as np
from src.data_processor import DataProcessor

class TestDataProcessor(unittest.TestCase):
    '''
    Sets up testing with the csv we want and stores it into a temp csv for testing
    '''
    def setUp(self):
        # get the actual data
        self.original = "data/naturalDisaster.csv"

        # creating a temp csv that is a copy of the original
        self.temp = "test.csv"
        shutil.copy(self.original, self.temp)

        self.processor = DataProcessor(file_path=self.temp)
    '''
    Deletes the temp csv that is created for testing purposes
    '''
    def tearDown(self):
        # clean up the test file after running
        if os.path.exists(self.temp):
            os.remove(self.temp)
    '''
    Test that we load all rows of the csv we need.
    '''
    def test_load_data(self):
        df = self.processor.load_data()

        self.assertEqual(df.shape[0], 1342) # Expects all of the rows in csv
    '''
    Tests that clean data grabs the correct columns and there are no zero or NaN values
    '''
    def test_clean_data(self):
        self.processor.load_data()  # Load data
        df_clean = self.processor.clean_data() # clean the data

        expected_columns = ["DisNo.", "Disaster Type", "Start Year", "Disaster Subtype", "ISO", "Event Name", "Magnitude", "Magnitude Scale",
            "Total Deaths", "Total Affected", "Total Damage ('000 US$)", "Total Damage, Adjusted ('000 US$)"]
        
        # Assert that we have all the columns we want in the data file
        self.assertTrue(all(col in df_clean.columns for col in expected_columns))
        self.assertFalse(df_clean["Magnitude"].isna().any()) # No NaN values
        self.assertFalse((df_clean["Magnitude"] == 0).any()) # Make sure it has no zeros
    '''
    Test that get features and target gets a numpy array that has the right length
    for features and target and that neither is missing values
    '''
    def test_get_features_and_targets(self):
        self.processor.load_data()
        self.processor.clean_data()

        features, target = self.processor.get_features_and_target()

        # Check that features and target return a numpy array
        self.assertIsInstance(features, np.ndarray)
        self.assertIsInstance(target, np.ndarray)

        # Check we get 3 columns for features
        self.assertEqual(features.shape[1], 3)
        
        # Check target for the same amount of magnitudes as features
        self.assertEqual(features.shape[0],target.shape[0])

        # Check for missing values in both
        self.assertFalse(np.any(np.isnan(features)))
        self.assertFalse(np.any(np.isnan(target)))
    '''
    Tests error checking of clean data to see if it 
    raises an error if we don't load the data
    '''
    def test_clean_data_load(self):
        processor = DataProcessor(file_path=self.temp)

        # Clean the data without loading which should cause an error
        with self.assertRaises(ValueError):
            processor.clean_data()
    '''
    Test get features and target without loading or cleaning the data
    '''
    def test_get_features_and_target_load_clean(self):
        processor = DataProcessor(file_path=self.temp)

        with self.assertRaises(ValueError):
            processor.get_features_and_target()
if __name__ == '__main__':
    unittest.main()