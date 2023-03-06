# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 17:54:59 2023

@author: Sakib
"""
import os
import numpy as np
import matplotlib.pyplot as plt

class PlotAndSimulateClass:
  
    def plot_data(self, data, plot_type):
        # Plots data (normal and scatter).
        if plot_type == '1':
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
            
            try:
                plt.scatter(np.arange(len(data)), data)
                plt.xlabel('X  Values')
                plt.ylabel('Y  Values')
                plt.title('X vs Y  Scatter Plot')
                plt.show()
            except ValueError:
                print("\nValue Error: x and y must be the same size !!!\n\nSorry plotting not possible. Try Normal plotting")
                return False
        
    def simulate_data(self, rows, cols):
        """Simulate data with given mean, variance, and size."""
        data = np.random.rand(rows, cols)
        return data
    
    
    def save_data(self, data, filename):
        """Save data to a file with the given filename."""
        with open(filename, 'w') as f:
            for num in data:
                f.write(str(num) + '\n')
        print(f"\nData saved successfully\n\nFile name: {filename}")
        print(f"File location: {os.path.abspath(filename)}")