# -*- coding: utf-8 -*-
'''
Created on Thu Mar  2 17:54:59 2023

@author: Md Sakib Nawaz
'''

# Main code.

# Numpy, matplotlib.pyplot, OS and sys libraries are imported. 
import os
import sys
import numpy as np
import matplotlib.pyplot as plt


# Classes are imported from the classes code files. 
from getData import GetDataClass
from calculator import CalculatorClass
from plotSimulate import PlotAndSimulateClass

'''
Three objects are instantiated from the classes GetDataClass, CalculatorClass, and 
PlotAndSimulateClass : get_data_obj, calculator_obj, and plot_simulate_obj respectively.
'''
get_data_obj = GetDataClass()
calculator_obj = CalculatorClass()
plot_simulate_obj = PlotAndSimulateClass()


# Display welcome message and menu
print('\nWelcome to Multi-function Data Analysis Software\n\nWhich function would you like to perform?')

# Infinite loop to display menu and receive user input. It will be the main menu.
while True:

    # Display user the menu option and ask for input
    choice = input(" 1. Data array loading functions\n 2. Convert units (g to kg, F to C, cm to m or vice versa)\n 3. Simulate a random dataset array\n 4. Exit\n\nPlease choose a function between 1 to 4: ")
    
    '''
    If user choose '1' a menu will be initiated where the user can load Data from file path or load data from
    files in the same directory as the main code is. Also user can exit to main menu or exit from the software.
    '''
    if choice == '1': 
        
        # A variable 'data' is created with None value
        data = None
        
        # Infinite loop to display load data menu and receive user input.
        while True:
 
            # Display load data menu options and ask for input.     
            load_choice = input("Load a data array from below functions \n\n 1. Load data array from file\n 2. Load data array from files in the same directory\n 3. Exit to main menu\n 4. Exit\n\nEnter your choice between 1 to 4: ")

            # If user chooce '1' then data will load from the file path that the user input.
            if load_choice == '1':
                
                '''
                Infinite loop to receive file path from user. 
                And give user an option to go back when input is 'b'.
                '''
                while True:
         
                    # Display instructions about the file to user.
                    print("\n\nImportant Notes:\n * This software loads only data array TXT file\n * Make sure the data has numerical values only\n * Make sure the data has same number of rows and columns\n"r" * File path might looks like 'C:\Users\user\data.txt'","\n"r" * The 'C:\' represents the root directory of the 'C:' drive", "\n"r" * The 'Users\user' is the path to the user's home directory","\n"r" * The 'data' is the name of the file","\n"r" * The '.txt' is the file type. Don't forget to add after the file name")
          
                    # Receive file path from user.
                    file_path = input("\nEnter the file path / 'b' to go back: ")
           
                    # Allow user to go back to previous menu.
                    if file_path == 'b':
                        break
                    
                    # Check if file exists and is a '.txt' file.
                    if os.path.isfile(file_path) and file_path.endswith('.txt'):
                        
                        # Load data from file.
                        data = get_data_obj.load_data_from_file(file_path)
                        
                        # If data loading is unsuccessful, display error message and continue loop.
                        if data is False:
                            print("\nData loading unsuccessful","\n\nPlease correct the data or enter a different file path")
                            continue
                        
                        # If data is successfully loaded, display success message and loaded data.
                        if data is not None:
                            print('\nData loading successfull')
                            print('\nLoaded data array:\n',np.nan_to_num(data))
                            
                            # Infinite loop to display data functions menu and receive user input.
                            while True:
                                
                                # Display data functions menu options and take user input.
                                func_choice = input("\nPlease choose what do you want to do next\n\n 1. Find the mean of the data array\n 2. Find the variance of the data array\n 3. Find the max value and it's index of the data array\n 4. Find the min value and it's index of the data array\n 5. Plot the data array\n 6. Go back\n 7. Exit\n\nEnter your choice between 1 to 7: ")
                                 
                                # If user inputs '1' then it will calculate the mean of the loaded data and display.
                                if func_choice == '1':
                                    mean = calculator_obj.find_mean(data)
                                    print('\n\nThe Mean of the loaded data array is:', mean)
                                
                                # If user inputs '2' then it will calculate the variance of the loaded data and display.    
                                elif func_choice == '2':
                                    variance = calculator_obj.find_variance(data)
                                    print('\n\nThe Variance of the loaded data array is:', variance)
                                
                                # If user inputs '3' then it will calculate the max value and it's index of the data and display.    
                                elif func_choice == '3':
                                    max_value, max_index = calculator_obj.find_max_value(data)
                                    print('\n\nThe Max value of the loaded data array is:', max_value)
                                    print('\nThe Max index of the loaded data array is:', max_index)
                                
                                # If user inputs '4' then it will calculate the min value and it's index of the data and display.                                
                                elif func_choice == '4':
                                    min_value, min_index = calculator_obj.find_min_value(data)
                                    print('\n\nThe Min value of the loaded data array is:', min_value)
                                    print('\nThe Min index of the loaded data array is:', min_index)
                                
                                # If user inputs '5' then it will display a menu for plotting.     
                                elif func_choice == '5':
                                    
                                    # Infinite loop to display plot menu and receive user input
                                    while True:
                                        
                                        # Display plot menu options and take user input.
                                        plot_type = input("\nPlease choose what do you want to do next\n\n 1. Normal plotting\n 2. Scatter plotting\n 3. Go back\n 4. Exit\n\nEnter your choice between 1 to 4: ")
                                        
                                        # If user inputs '1' then it will plot normal plotting.
                                        if plot_type == '1':
                                                     
                                            print('\nPlotting from loaded data array. . .')
                                            
                                            # Plot data using the plot function for normal plotting.
                                            n_data = plot_simulate_obj.plot_data(data,plot_type='1')
                                            
                                            # Check if the data is suitable for plotting. 
                                            if n_data is False:
                                                continue
                                            else:
                                                print('\n\nPlotting successfull')
                                                continue
                                        
                                        # If user inputs '2' then it will plot scatter plotting.
                                        elif plot_type == '2':
                                                     
                                            print('\nPlotting from loaded data array. . .')
                                            
                                            # Plot data using the plot function for scatter plotting.
                                            s_data = plot_simulate_obj.plot_data(data,plot_type='2')
                                            
                                            # Check if the data is suitable for plotting. 
                                            if s_data is False:
                                                continue    
                                            else:    
                                                print('\n\nPlotting successfull')
                                                continue
                                        
                                        # If user inputs '3' then it will go back to data function menu.
                                        elif plot_type == '3':
                                            print('\nGoing back . . .')
                                            break
                                                                              
                                        # If user inputs '4' then the program ends.    
                                        elif plot_type == '4':   
                                            print('\n\nExiting the software . . .\n\n***Thank you***')
                                            sys.exit()    
                                            
                                        # If user inputs anything else rather than 1-4, it will show error message and take back the user to the plot menu loop.                        
                                        else:
                                            print('\nWrong Input!!!\n\nPlease enter numerical value 1-4')
                                            continue
                                    
                                # If user inputs '6' then it will go back to data load menu.   
                                elif func_choice == '6':
                                    print('\nGoing back . . .')
                                    break
                                
                                # If user inputs '7' then the program ends.
                                elif func_choice == '7':
                                    print('\n\nExiting the software . . .\n\n***Thank you***')
                                    sys.exit()
                                
                                # If user inputs anything else rather than 1-7, it will show error message and take back the user to the data function loop.            
                                else:
                                    print('\nWrong Input!!!\n\nPlease enter numerical value 1-7')
                                    continue
                    
                    # If user inputs wrong file path then it will display  possible errors and ask the user to input the file path again.                   
                    else:
                        print("\nWrong Input!!!\n\nPossible Errors:\n * The file doesn't exist\n * It's not a TXT file \n * Missing '.txt' at the end of the file path\n\nPlease check the instruction and enter the file path again.")
                        continue
                    break
            
            # If user chooce '2' then data will load from the file in the same directory of the main code file.
            elif load_choice == '2': 
                
                '''
                Infinite loop to receive file name. 
                And give user an option to go back when input is 'b'.
                '''
                while True:
                    
                    # Display instructions about the file to user.
                    print("\n\nImportant Notes:\n * This software loads only data array TXT file\n * Make sure the data has numerical values only\n * Make sure the data has same number of rows and columns\n * Make sure the file is in the same directory as the code file\n * File name input might looks like 'data.txt'\n * The 'data' is the name of the file\n * The '.txt' is the file type. Don't forget to add after the file name")
                    
                    # Receive file name from user.
                    file_name = input("\nEnter the file name / 'b' to go back: ")
                    
                    # Allow user to go back to previous menu.
                    if file_name == 'b':
                        break
                    
                    # Check if file exists and is a '.txt' file.
                    if os.path.isfile(file_name) and file_name.endswith('.txt'):
                        
                        # Load data from file.
                        data = get_data_obj.load_data_from_directory(file_name)
                        
                        # If data loading is unsuccessful, display error message and continue loop.
                        if data is False:
                            print("\nData loading unsuccessful","\n\nPlease correct the data or enter a different file path")
                            continue
                        
                        # If data is successfully loaded, display success message and loaded data.
                        if data is not None:
                            print('\nData loading successfull')
                            print('\nLoaded data array:\n',np.nan_to_num(data))
                            
                            # Infinite loop to display data functions menu and receive user input.
                            while True:
                                
                                # Display data functions menu options and take user input.
                                func_choice = input("\nPlease choose what do you want to do next\n\n 1. Find the mean of the data array\n 2. Find the variance of the data array\n 3. Find the max value and it's index of the data array\n 4. Find the min value and it's index of the data array\n 5. Plot the data array\n 6. Go back\n 7. Exit\n\nEnter your choice between 1 to 7: ")
                                
                                # If user inputs '1' then it will calculate the mean of the loaded data and display.
                                if func_choice == '1':
                                    mean = calculator_obj.find_mean(data)
                                    print('\n\nThe Mean of the loaded data array is:', mean)
                                
                                # If user inputs '2' then it will calculate the variance of the loaded data and display.
                                elif func_choice == '2':
                                    variance = calculator_obj.find_variance(data)
                                    print('\n\nThe Variance of the loaded data array is:', variance)
                                
                                # If user inputs '3' then it will calculate the max value and it's index of the data and display.   
                                elif func_choice == '3':
                                    max_value, max_index = calculator_obj.find_max_value(data)
                                    print('\n\nThe Max value of the loaded data array is:', max_value)
                                    print('\nThe Max index of the loaded data array is:', max_index)
                                                                
                                # If user inputs '4' then it will calculate the min value and it's index of the data and display. 
                                elif func_choice == '4':
                                    min_value, min_index = calculator_obj.find_min_value(data)
                                    print('\n\nThe Min value of the loaded data array is:', min_value)
                                    print('\nThe Min index of the loaded data array is:', min_index)
                                
                                # If user inputs '5' then it will display a menu for plotting.     
                                elif func_choice == '5':
                                    
                                    # Infinite loop to display plot menu and receive user input
                                    while True:
                                        
                                        # Display plot menu options and take user input.
                                        plot_type = input("\nPlease choose what do you want to do next\n\n 1. Normal plotting\n 2. Scatter plotting\n 3. Go back\n 4. Exit\n\nEnter your choice between 1 to 4: ")
                                        
                                        # If user inputs '1' then it will plot normal plotting.
                                        if plot_type == '1':
                                                     
                                            print('\nPlotting from loaded data array. . .')
                                            
                                            # Plot data using the plot function for normal plotting..
                                            n_data = plot_simulate_obj.plot_data(data,plot_type='1')
                                            
                                            # Check if the data is suitable for plotting. 
                                            if n_data is False:
                                                continue
                                            else:
                                                print('\n\nPlotting successfull')
                                                continue
                                        
                                        # If user inputs '2' then it will plot scatter plotting.
                                        elif plot_type == '2':
                                                     
                                            print('\nPlotting from loaded data array. . .')
                                            
                                            # Plot data using the plot function for scatter plotting.
                                            s_data = plot_simulate_obj.plot_data(data,plot_type='2')
                                            
                                            # Check if the data is suitable for plotting. 
                                            if s_data is False:
                                                continue    
                                            else:    
                                                print('\n\nPlotting successfull')
                                                continue
                                        
                                        # If user inputs '3' then it will go back to data function menu.
                                        elif plot_type == '3':
                                            print('\nGoing back . . .')
                                            break
                                                                              
                                        # If user inputs '4' then the program ends.   
                                        elif plot_type == '4':   
                                            print('\n\nExiting the software . . .\n\n***Thank you***')
                                            sys.exit()    
                                        
                                        # If user inputs anything else rather than 1-4, it will show error message and take back the user to the plot menu loop.
                                        else:
                                            print('\nWrong Input!!!\n\nPlease enter numerical value 1-4')
                                            continue
                                    
                                # If user inputs '6' then it will go back to data load menu.     
                                elif func_choice == '6':
                                    print('\nGoing back . . .')
                                    break
                                
                                # If user inputs '7' then the program ends.
                                elif func_choice == '7':
                                    print('\n\nExiting the software . . .\n\n***Thank you***')
                                    sys.exit()
                                
                                # If user inputs anything else rather than 1-7, it will show error message and take back the user to the data function loop.                
                                else:
                                    print('\nWrong Input!!!\n\nPlease enter numerical value 1-7')
                                    continue
                    # If user inputs wrong file path then it will display  possible errors and ask the user to input the file path again.                      
                    else:
                        print("\nWrong Input!!!\n\nPossible Errors:\n * The file doesn't exist\n * It's not a TXT file \n * Missing '.txt' at the end of the file name\n\nPlease check the instruction and enter the file name again.")
                        continue
                    break    
                      
            # If user inputs '3' it will show the main menu and exit from load data menu.
            elif load_choice == '3':
                print('\nWhich function would you like to perform?')
                break
            
            # If user inputs '4' then the program ends.
            elif load_choice == '4':
                print('\n\nExiting the software . . .\n\n***Thank you***')
                sys.exit()
                
            
            # If user inputs anything else rather than 1-4, it will show error message and take back the user to the load data menu loop.                    
            else:
                print('\nWrong Input!!!\n\nPlease enter numerical value 1-4')
                continue   
    
   
    # If user choose '2' a Convert units menu will be initiated where the user can convert g to kg, F to C, cm to m or vice versa. 
    elif choice == '2':
        
        # Infinite loop to display Convert units menu.
        while True:
            
            # Display Convert units menu options and asks for input.
            con_choice = input("\nChoose a conversion / exit to main menu / exit\n\n 1. Grams to kilograms\n 2. Kilograms to grams\n 3. Fahrenheit to Celsius\n 4. Celsius to Fahrenheit\n 5. Centimeters to meters\n 6. Meters to centimeters\n 7. Exit to main menu\n 8. Exit \n\nEnter your choice between 1 to 8: ")
            
            # Set the from_unit and to_unit value to blank.
            from_unit, to_unit = "", ""

            '''
            Check the conversion chosen by the user and set the from_unit and to_unit
            variables and result function.
            '''
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
                
            # If user inputs '7' it will show the main menu and exit from Convert units menu.    
            elif con_choice == '7':
                print('\nWhich function would you like to perform?')
                break
            
            # If user inputs '4' then the program ends.    
            elif con_choice == '8':
                print('\n\nExiting the software . . .\n\n***Thank you***')
                sys.exit()    
            
            # If user inputs anything else rather than 1-8, it will show error message and take back the user to the Convert units menu loop.                    
            else:
                print('\nWrong Input!!!\n\nPlease enter numerical value 1-8')
                continue
           
            # Infinite loop to get input from user to convert the value.
            while True:
                # Get the value to be converted from user.
                value = input("Enter the value to convert / 'e' for exit to main menu: ")
                
                # If user inputs 'e' and wants to exit to main menu then break the loop.
                if value == 'e':
                    break
                
                # Check if the entered value is valid or not. If not, then ask for input again.
                if not value.replace(".", "").isdigit():
                    print("\nInvalid value!\nWrite numbers or 'e' for exit to main menu")
                    continue
                
                '''
                value set to be float type.
                Display the result of converted value.
                Go back to convert units menu.
                '''
                value = float(value)
                print('\n\nConversion done successfully')
                print('\nAnswer:',f"{value} {from_unit} = {result(value)} {to_unit}")
                print('\n\nReturning to previous menu . . .')
                break
        continue                                                       
    
    
    # If user choose '3', user will be asked to input row and column size for simulating random dataset.
    elif choice == '3': # Simulate data
        
        # Infinite loop for getting row size           
        while True:
            
            # Ask user for number of rows for simulated data.
            rows = input("Please enter the row size of the random dataset array/ 'e' for exit to main menu: ")
            
            # If user wants to exit to main menu then break the loop.
            if rows == 'e':
                break
            
            # Check if row is intiger.
            try:
                rows = int(rows)
                break
            
            # If user inputs not intiger number then it continues the row loop 
            except ValueError:
                print('\nWrong Input for row size !!!\n\nPlease enter an integer value')
                continue
        
        # Check if row is 'e' or not to go to the next step.
        if rows != 'e':
            
            # Infinite loop for getting column size    
            while True:
                
                # Ask user for number of columns for simulated data.
                cols = input("Please enter the column size of the random dataset array/ 'e' for exit to main menu: ")
                
                # If user wants to exit to main menu then break the loop.
                if cols == 'e':
                    break
                
                # Check if column is intiger.
                try:
                    cols = int(cols)
                    break
                
                # If user inputs not intiger number then it continues the column loop 
                except ValueError:
                    print('\nWrong Input for column size !!!\n\nPlease enter an integer value')
                    continue
        
        # Check if row or column is 'e' and display a message.         
        if rows == 'e' or cols == 'e':
            print('\nExiting to main menu ...\n\nWhich function would you like to perform?')
        
        # If rows and cols both are intiger number then it simulates random dataset array and displays that.    
        else:
            
            # Simulates random data array.
            simulated_data = plot_simulate_obj.simulate_data(rows,cols)
            print ('\n\nSimulating random dataset successfull')
            
            # Display random data as array
            print('\n\nSimulated random dataset array:\n',simulated_data)
            
            # Infinite loop to display saveplot menu.
            while True:
                
                # Diaplay saveplot menu options and ask for input.
                save_plot_choice = input("\nPlease choose what do you want to do next\n\n 1. Save random dataset array\n 2. Plot random dataset array\n 3. Exit to main menu\n 4. Exit \n\nEnter your choice between 1 to 4: ")
                
                # If user inputs '1' then it will ask for the file name and show go back option.
                if  save_plot_choice == '1':
                
                    # Ask for the file name from user.
                    filename = input("Enter the filename to save / 'b' to go back: ")
                    
                    # If user inputs 'b' then it will go back to saveplot menu.
                    if filename == 'b':
                        print('\nGoing back . . .')
                        continue
                    
                    # Check if user inputs '.txt' at the end of the filename otherwise it will add.
                    if not filename.endswith('.txt'):
                        filename += '.txt'
                    
                    
                    # Save the file and show the filename and file location.
                    try:  
                        plot_simulate_obj.save_data(simulated_data, filename)
                        continue
                    
                    # If error occurs then it asks for a different filename or to check the directory access permissions.
                    except OSError:
                        print('Error saving file. Please try a different filename or check the directory access permissions.')
                        continue
                
                # If user inputs '2' then it will display a menu for plotting.  
                elif save_plot_choice == '2':
                    
                    # Infinite loop to display plot menu and receive user input
                    while True:
                        
                        # Display plot menu options and take user input.
                        plot_type = input("\nPlease choose what do you want to do next\n\n 1. Normal plotting\n 2. Scatter plotting\n 3. Go back\n 4. Exit\n\nEnter your choice between 1 to 4: ")
                        
                        # If user inputs '1' then it will plot normal plotting.
                        if plot_type == '1':
                                     
                            print('\nPlotting random dataset array . . .')
                            
                            # Plot data using the plot function for normal plotting.
                            n_data = plot_simulate_obj.plot_data(simulated_data,plot_type='1')
                            
                            # Check if the data is suitable for plotting. 
                            if n_data is False:
                                continue
                            else:
                                print('\n\nPlotting successfull')
                                continue
                        
                        # If user inputs '2' then it will plot scatter plotting.
                        elif plot_type == '2':
                                     
                            print('\nPlotting random dataset array . . .')
                            
                            # Plot data using the plot function for scatter plotting.
                            s_data = plot_simulate_obj.plot_data(simulated_data,plot_type='2')
                            
                            # Check if the data is suitable for plotting.
                            if s_data is False:
                                continue    
                            else:    
                                print('\n\nPlotting successfull')
                                continue
                        
                        # If user inputs '3' then it will go back to saveplot menu.
                        elif plot_type == '3':
                            print('\nGoing back . . .')
                            break
                                                              
                        # If user inputs '4' then the program ends.       
                        elif plot_type == '4':   
                            print('\n\nExiting the software . . .\n\n***Thank you***')
                            sys.exit()    
                        
                        # If user inputs anything else rather than 1-4, it will show error message and take back the user to the plot menu loop.    
                        else:
                            print('\nWrong Input!!!\n\nPlease enter numerical value 1-4')
                            continue
                
                # If user inputs '3' it will show the main menu and exit from saveplot menu.    
                elif save_plot_choice == '3':
                    print('\nWhich function would you like to perform?')
                    break
                
                # If user inputs '4' then the program ends. 
                elif save_plot_choice == '4':
                    print('\n\nExiting the software . . .\n\n***Thank you***')
                    sys.exit()    
                
                # If user inputs anything else rather than 1-4, it will show error message and take back the user to the saveplot menu loop.
                else:
                    print('\nWrong Input!!!\n\nPlease enter numerical value 1-4')
                    continue
                  
    # If user inputs '4' then the program ends or exits from main menu.             
    elif choice == '4':
        print('\n\nExiting the software . . .\n\n***Thank you***')
        sys.exit() 
    
        
    # If user inputs anything else rather than 1-4, it will show error message and take back the user to the main menu loop.
    else: 
        print('\nWrong Input!!!\n\nPlease enter numerical value 1-4\n\nThis software can only perform the functions below')
        continue


'''
This code is written with many helps from youtube, class lectures, w3schools.com, programiz.com, numpy.org,
learnpython.org, geeksforgeeks.org and other sites.

This code is written as a project work for the Python Course at the University of Siegen.

Feel free to use this code.

'''





