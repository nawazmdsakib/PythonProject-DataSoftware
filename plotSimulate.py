# -*- coding: utf-8 -*-
'''
Created on Thu Mar  2 17:54:59 2023

@author: Md Sakib Nawaz
'''

# Class code.

# Numpy, matplotlib.pyplot and OS libraries are imported. 
import os
import numpy as np
import matplotlib.pyplot as plt


'''
A class definition with 3 functions which will plot data,
simulate data and save the data into the main code directory.
'''

class PlotAndSimulateClass:
  
    # A function which will plot data from the file or the simulated data.
    def plot_data(self, data, plot_type):
        '''
        This checks if the plot_type argument is '1' or '2'. if '1', it will 
        create a normal plot and if '2' it will create a scatter plot.
        '''
        if plot_type == '1':
            
            '''
            This tries to create a normal plot using the data argument.If it 
            encounters a ValueError, it will print an error message and return False.
            '''
            try:
                plt.plot(data)
                plt.xlabel('X  Values')
                plt.ylabel('Y  Values')
                plt.title('X vs Y  Normal Plot')
                plt.show()
            except ValueError:
                print("\nValue Error !!!\n\nSorry plotting not possible. Try Scatter plotting")
                return False

        elif plot_type == '2':
            '''
            This tries to create a scatter plot using the data argument. If it 
            encounters a ValueError, it will print an error message and return False.
            '''
            try:
                plt.scatter(np.arange(len(data)), data)
                plt.xlabel('X  Values')
                plt.ylabel('Y  Values')
                plt.title('X vs Y  Scatter Plot')
                plt.show()
            except ValueError:
                print("\nValue Error: x and y must be the same size !!!\n\nSorry plotting not possible. Try Normal plotting")
                return False

    # A function which will simulate random data array.   
    def simulate_data(self, rows, cols):

        # This generates a 2D array of random numbers using NumPy and returns it.
        data = np.random.rand(rows, cols)
        return data
    

    # A function which will save the simulated random data array as txt file in the main code directory.
    def save_data(self, data, filename):
        
        '''
        This opens a file with the given filename and writes each element of the data array
        to a new line in the file. It then prints a success message, file name and the file location.
        '''
        with open(filename, 'w') as f:
            for num in data:
                f.write(str(num) + '\n')
        print(f"\nData saved successfully\n\nFile name: {filename}")
        print(f"File location: {os.path.abspath(filename)}")