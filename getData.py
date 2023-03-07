# -*- coding: utf-8 -*-
'''
Created on Thu Mar  2 17:53:11 2023

@author: Md Sakib Nawaz
'''

# Class code.

# Numpy and OS libraries are imported. 
import numpy as np
import os

'''
A class definition with 3 functions which will load data 
from file in the same directory of the main code or 
any file path. And also validate data type inside the file.
'''
class GetDataClass:
    
    # A function which will load data from any file path provided by the user.
    def load_data_from_file(self, file_path):
        ''' 
        Data is loaded from the specified file using numpy.genfromtxt with 'try'
        otherwise exception is caught if there is an error in loading the data.
        '''
        try:
            data = np.genfromtxt(file_path)
           
            # The loaded data is validated. 
            return self.validate_data(data)
        
        except ValueError: 
            print("\nError: Not all lines have the same number of columns!!!")
            return False

    # A function which will load data from file in the same directory where the main code is loaded.
    def load_data_from_directory(self, file_name):

        # The current directory of the script is obtained. 
        current_directory = os.path.dirname(os.path.abspath(__file__))
        

        # The full file path is constructed using the current directory and the given file name.
        file_path = os.path.join(current_directory, file_name)
                
        try:
            ''' 
            Data is loaded from the specified file using numpy.genfromtxt with 'try'
            otherwise exception is caught if there is an error in loading the data.
            '''
            data = np.genfromtxt(file_path)
        
            # The loaded data is validated. 
            return self.validate_data(data)
        
        except ValueError:
            print("\nError: Not all lines have the same number of columns!!!")
            return False
        
    
    '''
    A function to validate the data that were loaded from the file.
    This will ckeck if the data is Nan,all numbers, infinity or file is empty.
    If data is Nan or infinity or file empty, it will return False.
    '''
    def validate_data(self, data):

        # Check if there are any NaN values in the data. 
        if np.isnan(data).any():
            print("\nError: NaN value found in data!!!")
            return False

        # Check if there are any infinite values in the data. 
        if np.isinf(data).any():
            print("\nError: Infinite value found in data!!!")
            return False

        # Check if the file is empty. 
        if not data.any():
            print("\nError: Empty file!!!")
            return False

        # Return the validated data if all checks pass. 
        return data

