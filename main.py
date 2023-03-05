# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 17:45:13 2023

@author: Sakib
"""
# Main program

import os
import sys
import numpy as np
import matplotlib.pyplot as plt


from getData import GetDataClass
from calculator import CalculatorClass
from plotSimulate import PlotAndSimulateClass

get_data_obj = GetDataClass()
calculator_obj = CalculatorClass()
plot_simulate_obj = PlotAndSimulateClass()

    
print('\nWelcome to Multi-function Data Analysis Software\n\nWhich function would you like to perform?')



while True:   
    choice = input(" 1. Data loading functions\n 2. Convert units (g to kg, F to C, cm to m or vice versa)\n 3. Simulate a random dataset\n 4. Exit\n\nPlease choose a function between 1 to 4: ")
    # Load data from file
    if choice == '1': 
        
        data = None
        while True:
            
            load_choice = input("Load a data from below functions \n\n 1. Load data from file\n 2. Load data from files in the same directory\n 3. Exit to main menu\n 4. Exit\n\nEnter your choice between 1 to 4: ")
                        
            if load_choice == '1':
                while True:
                    print("\n\nImportant Notes:\n * This software loads TXT file only\n"r" * File path might looks like 'C:\Users\user\data.txt'","\n"r" * The 'C:\' represents the root directory of the 'C:' drive", "\n"r" * The 'Users\user' is the path to the user's home directory","\n"r" * The 'data.txt' is the name of the file")
                    file_path = input("\nEnter the file path / 'b' to go back: ")
            
                    if file_path == 'b':
                        break
            
                    if os.path.isfile(file_path) and file_path.endswith('.txt'):
                        data = get_data_obj.load_data_from_file(file_path)
                        
                        if data is False:
                            print("\nData loading unsuccessful","\n\nPlease correct the data or enter a different file path")
                            continue
                        
                        if data is not None:
                            print('\nData loading successfull')
                            print('\nLoaded data:\n',np.nan_to_num(data))
                            
                            
                            while True:
                                func_choice = input("\nPlease choose what do you want to do next\n\n 1. Find the mean of the data\n 2. Find the variance of the data\n 3. Find the max value and it's index of the data\n 4. Find the min value and it's index of the data\n 5. Plot the data\n 6. Go back\n 7. Exit\n\nEnter your choice between 1 to 7: ")
                                            
                                if func_choice == '1':
                                    mean = calculator_obj.find_mean(data)
                                    print('\n\nThe Mean of the loaded data is:', mean)
                                    
                                elif func_choice == '2':
                                    variance = calculator_obj.find_variance(data)
                                    print('\n\nThe Variance of the loaded data is:', variance)
                                   
                                elif func_choice == '3':
                                    max_value, max_index = calculator_obj.find_max_value(data)
                                    print('\n\nThe Max value of the loaded data is:', max_value)
                                    print('\nThe Max index of the loaded data is:', max_index)
                                                                
                                elif func_choice == '4':
                                    min_value, min_index = calculator_obj.find_min_value(data)
                                    print('\n\nThe Min value of the loaded data is:', min_value)
                                    print('\nThe Min index of the loaded data is:', min_index)
                                                                
                                elif func_choice == '5':
                                    
                                    while True:
                                        plot_type = input("\nPlease choose what do you want to do next\n\n 1. Normal plotting\n 2. Scatter plotting\n 3. Go back\n 4. Exit\n\nEnter your choice between 1 to 4: ")
                                        
                                        if plot_type == '1':
                                                     
                                            print('\nPlotting from loaded data . . .')
                                            n_data = plot_simulate_obj.plot_data(data,plot_type='1')
                                            if n_data is False:
                                                continue
                                            else:
                                                print('\n\nPlotting successfull')
                                                continue
                                        
                                        elif plot_type == '2':
                                                     
                                            print('\nPlotting from loaded data . . .')
                                            s_data = plot_simulate_obj.plot_data(data,plot_type='2')
                                            
                                            if s_data is False:
                                                continue    
                                            else:    
                                                print('\n\nPlotting successfull')
                                                continue
                                        
                                        elif plot_type == '3':
                                            print('\nGoing back . . .')
                                            break
                                                                              
                                            
                                        elif plot_type == '4':   
                                            print('\n***Thank you***')
                                            sys.exit()    
                                                                
                                        else:
                                            print('\nWrong Input!!!\n\nPlease enter numerical value 1-4')
                                            continue
                                    
                                    
                                elif func_choice == '6':
                                    print('\nGoing back . . .')
                                    break
                                
                                elif func_choice == '7':
                                    print('\n***Thank you***')
                                    sys.exit()
                                            
                                else:
                                    print('\nWrong Input!!!\n\nPlease enter numerical value 1-7')
                                    continue
                                          
                    else:
                        print("\nWrong Input!!!\n\nPossible Errors:\n * The file doesn't exist\n * It's not a .txt file \n * Missing '.txt' at the end of the file path\n\nPlease check the instruction and enter the file path again.")
                        continue
                    break
            
            
            elif load_choice == '2': #Load data from files in the same directory
            
                while True:
                    
                    print("\n\nImportant Notes:\n * This software loads TXT file only\n * Make sure the file is in the same directory\n * Please add '.txt' after the file name\n * File name input might looks like 'data.txt'")
                    file_name = input("\nEnter the file name / 'b' to go back: ")
            
                    if file_name == 'b':
                        break
                    
                    if os.path.isfile(file_name) and file_name.endswith('.txt'):
                        data = get_data_obj.load_data_from_directory(file_name)
                    
                        if data is False:
                            print("\nData loading unsuccessful","\n\nPlease correct the data or enter a different file path")
                            continue
                        
                        if data is not None:
                            print('\nData loading successfull')
                            print('\nLoaded data:\n',np.nan_to_num(data))
                            
                            
                            while True:
                                func_choice = input("\nPlease choose what do you want to do next\n\n 1. Find the mean of the data\n 2. Find the variance of the data\n 3. Find the max value and it's index of the data\n 4. Find the min value and it's index of the data\n 5. Plot the data\n 6. Go back\n 7. Exit\n\nEnter your choice between 1 to 7: ")
                                            
                                if func_choice == '1':
                                    mean = calculator_obj.find_mean(data)
                                    print('\n\nThe Mean of the loaded data is:', mean)
                                    
                                elif func_choice == '2':
                                    variance = calculator_obj.find_variance(data)
                                    print('\n\nThe Variance of the loaded data is:', variance)
                                   
                                elif func_choice == '3':
                                    max_value, max_index = calculator_obj.find_max_value(data)
                                    print('\n\nThe Max value of the loaded data is:', max_value)
                                    print('\nThe Max index of the loaded data is:', max_index)
                                                                
                                elif func_choice == '4':
                                    min_value, min_index = calculator_obj.find_min_value(data)
                                    print('\n\nThe Min value of the loaded data is:', min_value)
                                    print('\nThe Min index of the loaded data is:', min_index)
                                                                
                                elif func_choice == '5':
                                    
                                    while True:
                                        plot_type = input("\nPlease choose what do you want to do next\n\n 1. Normal plotting\n 2. Scatter plotting\n 3. Go back\n 4. Exit\n\nEnter your choice between 1 to 4: ")
                                        
                                        if plot_type == '1':
                                                     
                                            print('\nPlotting from loaded data . . .')
                                            n_data = plot_simulate_obj.plot_data(data,plot_type='1')
                                            if n_data is False:
                                                continue
                                            else:
                                                print('\n\nPlotting successfull')
                                                continue
                                        
                                        elif plot_type == '2':
                                                     
                                            print('\nPlotting from loaded data . . .')
                                            s_data = plot_simulate_obj.plot_data(data,plot_type='2')
                                            
                                            if s_data is False:
                                                continue    
                                            else:    
                                                print('\n\nPlotting successfull')
                                                continue
                                        
                                        elif plot_type == '3':
                                            print('\nGoing back . . .')
                                            break
                                                                              
                                            
                                        elif plot_type == '4':   
                                            print('\n***Thank you***')
                                            sys.exit()    
                                                                
                                        else:
                                            print('\nWrong Input!!!\n\nPlease enter numerical value 1-4')
                                            continue
                                    
                                    
                                elif func_choice == '6':
                                    print('\nGoing back . . .')
                                    break
                                
                                elif func_choice == '7':
                                    print('\n***Thank you***')
                                    sys.exit()
                                            
                                else:
                                    print('\nWrong Input!!!\n\nPlease enter numerical value 1-7')
                                    continue
                                          
                    else:
                        print("\nWrong Input!!!\n\nPossible Errors:\n * The file doesn't exist\n * It's not a .txt file \n * Missing '.txt' at the end of the file name\n\nPlease check the instruction and enter the file name again.")
                        continue
                    break    
                      
           
            elif load_choice == '3':
                print('\nWhich function would you like to perform?')
                break
            
            elif load_choice == '4':
                print('\n***Thank you***')
                sys.exit()
                
                
            else:
                print('\nWrong Input!!!\n\nPlease enter numerical value 1-4')
                continue   
    
       
    elif choice == '2': # Convert units
        while True:
            con_choice = input("\nChoose a conversion / exit to main menu / exit\n\n 1. Grams to kilograms\n 2. Kilograms to grams\n 3. Fahrenheit to Celsius\n 4. Celsius to Fahrenheit\n 5. Centimeters to meters\n 6. Meters to centimeters\n 7. Exit to main menu\n 8. Exit \n\nEnter your choice between 1 to 8: ")
           
            from_unit, to_unit = "", ""

            if con_choice == '1':
                from_unit, to_unit = "g", "kg"
                result = calculator_obj.g_to_kg
            elif con_choice == '2':
                from_unit, to_unit = "kg", "g"
                result = calculator_obj.kg_to_g
            elif con_choice == '3':
                from_unit, to_unit = "F", "C"
                result = calculator_obj.f_to_c
            elif con_choice == '4':
                from_unit, to_unit = "C", "F"
                result = calculator_obj.c_to_f
            elif con_choice == '5':
                from_unit, to_unit = "cm", "m"
                result = calculator_obj.cm_to_m
            elif con_choice == '6':
                from_unit, to_unit = "m", "cm"
                result = calculator_obj.m_to_cm
            elif con_choice == '7':
                print('\nWhich function would you like to perform?')
                break
                
            elif con_choice == '8':
                print('\n***Thank you***')
                sys.exit()    
            else:
                print('\nWrong Input!!!\n\Please enter numerical value 1-8')
                continue
            
            while True:
                value = input("Enter the value to convert / 'e' for exit to main menu: ")
                if value == 'e':
                    break
                
                if not value.replace(".", "").isdigit():
                    print("\nInvalid value!\nWrite numbers or 'e' for exit to main menu")
                    continue
        
                value = float(value)
                print('\n\nConversion done successfully')
                print('\nAnswer:',f"{value} {from_unit} = {result(value)} {to_unit}")
                print('\n\nReturning to previous menu . . .')
                break
        continue                                                       
     
    elif choice == '3': # Simulate data
                   
        while True:
            rows = input("Please enter the row size of the random dataset / 'e' for exit to main menu: ")
            if rows == 'e':
                break
            try:
                rows = int(rows)
                break
            except ValueError:
                print('\nWrong Input for row size !!!\n\nPlease enter an integer value')
                continue
        if rows != 'e':
            while True:
                cols = input("Please enter the column size of the random dataset / 'e' for exit to main menu: ")
                if cols == 'e':
                    break
                try:
                    cols = int(cols)
                    break
                except ValueError:
                    print('\nWrong Input for column size !!!\n\nPlease enter an integer value')
                    continue
                 
        if rows == 'e' or cols == 'e':
            print('\nExiting to main menu ...\n\nWhich function would you like to perform?')
            
        else:
            simulated_data = plot_simulate_obj.simulate_data(rows,cols)
            print ('\n\nSimulating random dataset successfull')
            print('\n\nSimulated data:\n',simulated_data)
            
            
            while True:
                save_plot_choice = input("\nPlease choose what do you want to do next\n\n 1. Save random dataset\n 2. Plot random dataset\n 3. Exit to main menu\n 4. Exit \n\nEnter your choice between 1 to 4: ")
                    
                if  save_plot_choice == '1':
                
                    
                    filename = input("Enter the filename to save / 'b' to go back: ")
                    if filename == 'b':
                        print('\nGoing back . . .')
                        continue
                    if not filename.endswith('.txt'):
                        filename += '.txt'
                    try:
                       
                        plot_simulate_obj.save_data(simulated_data, filename)
                        continue
                    except OSError:
                        print('Error saving file. Please try a different filename or directory.')
                        continue
                
                
                elif save_plot_choice == '2':
                    
                    while True:
                        plot_type = input("\nPlease choose what do you want to do next\n\n 1. Normal plotting\n 2. Scatter plotting\n 3. Go back\n 4. Exit\n\nEnter your choice between 1 to 4: ")
                        
                        if plot_type == '1':
                                     
                            print('\nPlotting random dataset . . .')
                            n_data = plot_simulate_obj.plot_data(simulated_data,plot_type='1')
                            if n_data is False:
                                continue
                            else:
                                print('\n\nPlotting successfull')
                                continue
                        
                        elif plot_type == '2':
                                     
                            print('\nPlotting random dataset . . .')
                            s_data = plot_simulate_obj.plot_data(simulated_data,plot_type='2')
                            
                            if s_data is False:
                                continue    
                            else:    
                                print('\n\nPlotting successfull')
                                continue
                        
                        elif plot_type == '3':
                            print('\nGoing back . . .')
                            break
                                                              
                            
                        elif plot_type == '4':   
                            print('\n***Thank you***')
                            sys.exit()    
                                                
                        else:
                            print('\nWrong Input!!!\n\nPlease enter numerical value 1-4')
                            continue
                    
                elif save_plot_choice == '3':
                    print('\nWhich function would you like to perform?')
                    break
              
                elif save_plot_choice == '4':
                    print('\n***Thank you***')
                    sys.exit()    
                
                else:
                    print('\nWrong Input!!!\n\nPlease enter numerical value 1-4')
                    continue
                  
                 
    elif choice == '4': #Exit
        print('\n***Thank you***')
        sys.exit() 
        
    else: 
        print('\nWrong Input!!!\n\nPlease enter numerical value 1-4\n\nThis software can only perform the functions below')
        continue
