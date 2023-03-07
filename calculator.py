# -*- coding: utf-8 -*-
'''
Created on Thu Mar  2 17:53:45 2023

@author: Md Sakib Nawaz
'''

# Class code.

# Numpy library is imported. 
import numpy as np


class CalculatorClass:
    

    # This function converts grams to kilograms.
    def g_to_kg(self, weight):
        return weight / 1000
    

    # This function converts kilograms to grams.
    def kg_to_g(self, weight):
        return weight * 1000
    

    # This function converts Fahrenheit to Celsius.
    def f_to_c(self, temperature):
        return (temperature - 32) * 5/9
    

    # This function converts Celsius to Fahrenheit.
    def c_to_f(self, temperature):
        return (temperature * 9/5) + 32
    

    # This function converts centimeters to meters.
    def cm_to_m(self, distance):
        return distance / 100
    

    # This function converts meters to centimeters.
    def m_to_cm(self, distance):
        return distance * 100


    # This function finds the mean of an array of data using NumPy.
    def find_mean(self,data):
        return np.mean(data)
    

    # This function finds the variance of an array of data using NumPy.
    def find_variance(self,data):
        return np.var(data)
    

    # This function finds the maximum value and its index in an array of data using NumPy.
    def find_max_value(self,data):
        max_value = np.max(data)
        max_index = np.argmax(data)
        return max_value, max_index
    

    # This function finds the minimum value and its index in an array of data using NumPy.
    def find_min_value(self,data):
        min_value = np.min(data)
        min_index = np.argmin(data)
        return min_value, min_index
