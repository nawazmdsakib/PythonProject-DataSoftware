# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 17:53:11 2023

@author: Sakib
"""

import numpy as np
import os

class GetDataClass:

    def load_data_from_file(self,file_path):
        # Load data from file
       try:
           data = np.genfromtxt(file_path)
           return self.validate_data(data)
       except ValueError:
           print("\nError: Not all line has same number of columns !!!")
           return False

    

    def load_data_from_directory(self,file_name):
        # Get the current directory of the script
        current_directory = os.path.dirname(os.path.abspath(__file__))
        
        # Construct the full file path using the current directory and the given file name
        file_path = os.path.join(current_directory, file_name)
                
        try:
            data = np.genfromtxt(file_path)
            return self.validate_data(data)
        except ValueError:
            print("\nError: Not all lines have the same number of columns!!!")
            return False
        
       
        
        
    

    def validate_data(self, data):
        if np.isnan(data).any():
            print("\nError: NaN value found in data !!!")
            return False
        if np.isinf(data).any():
            print("\nError: Infinite value found in data !!!")
            return False
        if not data.any():
            print("\nError: Empty file !!! ")
            return False
        return data

