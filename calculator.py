# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 17:53:45 2023

@author: Sakib
"""

import numpy as np

class CalculatorClass:
    
    def g_to_kg(self, weight):
        return weight / 1000
    
    def kg_to_g(self, weight):
        return weight * 1000
    
    def f_to_c(self, temperature):
        return (temperature - 32) * 5/9
    
    def c_to_f(self, temperature):
        return (temperature * 9/5) + 32
    
    def cm_to_m(self, distance):
        return distance / 100
    
    def m_to_cm(self, distance):
        return distance * 100



    def find_mean(self,data):
        # Finds the mean of a data array.
        return np.mean(data)
    

    def find_variance(self,data):
        # Finds the variance of a data array.
        return np.var(data)
    

    def find_max_value(self,data):
        # Finds the max value and its index in a data array.
        max_value = np.max(data)
        max_index = np.argmax(data)
        return max_value, max_index
    
 
    def find_min_value(self,data):
        # Finds the min value and its index in a data array.
        min_value = np.min(data)
        min_index = np.argmin(data)
        return min_value, min_index