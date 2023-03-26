# PythonProject_DataSoftware

Multi-function Data Analysis Software:


Description:


This software is designed to perform multi-functional data analysis tasks such as loading data array from any file path, loading data array from same directory, validating data, converting units(g to kg, F to C, cm to m or vice versa), simulating a random dataset array. Also finding mean, variance, max value, min value and it's index of the data array. The software is written in Python and utilizes the Os, Sys, NumPy and Matplotlib libraries.

This software has one main code Python file named main.py and 3 Class Python files named getData.py, calculator.py and plotSimulate.p. In getData.py file there is GetDataClass, in calculator.py file there is CalculatorClass and in plotSimulate.p file there is PlotAndSimulateClass.

GetDataClass:
This class contains methods for loading data from files and directories, as well as validating the data. The following methods are available:
* load_data_from_file(self, file_path: loads data from any file path and returns it as a NumPy array
* load_data_from_directory(self, file_name): loads data from all files in the same directory of the main Python code and returns it as a list of NumPy arrays.
* validate_data(self, data): validates the data by checking for NaN values, ensuring all values are numbers and file is not empty

CalculatorClass:
This class contains methods for performing mathematical calculations on data, such as converting units, calculating statistical values, and finding max and min values. The following methods are available:
* g_to_kg(self, weight): converts grams to kilograms.
* kg_to_g(self, weight): converts kilograms to grams.
* f_to_c(self, temperature): converts Fahrenheit to Celsius.
* c_to_f(self, temperature): converts Celsius to Fahrenheit.
* cm_to_m(self, distance): converts centimeters to meters.
* m_to_cm(self, distance): converts meters to centimeters.
* find_mean(self,data): finds the mean of an array of data using NumPy.
* find_variance(self,data): finds the variance of an array of data using NumPy.
* find_max_value(self,data): finds the maximum value and its index in an array of data using NumPy.
* find_min_value(self,data): finds the minimum value and its index in an array of data using NumPy.

PlotAndSimulateClass:
This class contains methods for visualizing data, such as plotting data and simulating random dataset array. And also saving the data into the main directory. The following methods are available:
* plot_data(self, data, plot_type): plots the data in a normal and scatter format.
* def simulate_data(self, rows, cols): simulates a random dataset and returns it as a NumPy array.
* def save_data(self, data, filename): saves the dataset array into the main directory


Workflow:


The user is prompted to select a function from the available options. Depending on the user's choice, additional input may be required. Once the user-defined function is performed, the results are displayed to the user. The user is then get back to the current or previous menu for selecting, what he wants to do next. User can perform another function in the same menu or go back to the previous menu or go back to the main menu or close the software by selecting Exit.


Installation:

 
To get started, you'll need to have Python installed on your computer. You can download Python from the official website: https://www.python.org/downloads/
You'll also need to install the Python packages: os, sys, numpy and matplotlib.pyplot.

Once you have Python and the required packages installed, you can run the code. Make sure other class files such as getData.py, calculator.py and plotSimulate.py are in the same directory.

Load main.py file and RUN!


Examples:


* Welcome note and main menu

Welcome to Multi-function Data Analysis Software

Which function would you like to perform?

 1. Data array loading functions
 2. Convert units (g to kg, F to C, cm to m or vice versa)
 3. Simulate a random dataset array
 4. Exit

Please choose a function between 1 to 4: 


* Load data menu

Load a data array from below functions 

 1. Load data array from file
 2. Load data array from files in the same directory
 3. Exit to main menu
 4. Exit

Enter your choice between 1 to 4: 


* Load data array from file

Important Notes:
 * This software loads only data array TXT file
 * Make sure the data has numerical values only
 * Make sure the data has same number of rows and columns
 * File path might looks like 'C:\Users\user\data.txt' 
 * The 'C:\' represents the root directory of the 'C:' drive 
 * The 'Users\user' is the path to the user's home directory 
 * The 'data' is the name of the file 
 * The '.txt' is the file type. Don't forget to add after the file name


Enter the file path / 'b' to go back: 


* Load data array from files in the same directory

Important Notes:
 * This software loads only data array TXT file
 * Make sure the data has numerical values only
 * Make sure the data has same number of rows and columns
 * Make sure the file is in the same directory as the code file
 * File name input might looks like 'data.txt'
 * The 'data' is the name of the file
 * The '.txt' is the file type. Don't forget to add after the file name


Enter the file name / 'b' to go back: 


* If loading data is unsuccessfull from any file path

Wrong Input!!!

Possible Errors:
 * The file doesn't exist
 * It's not a TXT file 
 * Missing '.txt' at the end of the file path

Please check the instruction and enter the file path again.


* If loading data is unsuccessfull from directory

Wrong Input!!!

Possible Errors:
 * The file doesn't exist
 * It's not a TXT file 
 * Missing '.txt' at the end of the file name

Please check the instruction and enter the file name again.


* After loading data, data functions menu

Data loading successfull

Loaded data array:
 [[ 1.  2.  3.  4.]
 [ 5.  6.  7.  8.]
 [ 9. 10. 11. 12.]]


Please choose what do you want to do next

 1. Find the mean of the data array
 2. Find the variance of the data array
 3. Find the max value and it's index of the data array
 4. Find the min value and it's index of the data array
 5. Plot the data array
 6. Go back
 7. Exit

Enter your choice between 1 to 7: 


* If selected 5 the plot menu will be displayed

Please choose what do you want to do next

 1. Normal plotting
 2. Scatter plotting
 3. Go back
 4. Exit

Enter your choice between 1 to 4: 


* Convert units menu

Choose a conversion / exit to main menu / exit

 1. Grams to kilograms
 2. Kilograms to grams
 3. Fahrenheit to Celsius
 4. Celsius to Fahrenheit
 5. Centimeters to meters
 6. Meters to centimeters
 7. Exit to main menu
 8. Exit 

Enter your choice between 1 to 8: 


* For any conversion

Conversion done successfully

Answer: 10.0 g = 0.01 kg


Returning to previous menu . . .


Choose a conversion / exit to main menu / exit

 1. Grams to kilograms
 2. Kilograms to grams
 3. Fahrenheit to Celsius
 4. Celsius to Fahrenheit
 5. Centimeters to meters
 6. Meters to centimeters
 7. Exit to main menu
 8. Exit 

Enter your choice between 1 to 8: 


* Simulate a random dataset array

Please enter the row size of the random dataset array/ 'e' for exit to main menu: 3

Please enter the column size of the random dataset array/ 'e' for exit to main menu: 3


Simulating random dataset successfull


Simulated random dataset array:
 [[0.19874332 0.53811174 0.0156885 ]
 [0.30360163 0.73483863 0.11134744]
 [0.44919802 0.18202944 0.99993433]]


* Saveplot menu

Please choose what do you want to do next

 1. Save random dataset array
 2. Plot random dataset array
 3. Exit to main menu
 4. Exit 

Enter your choice between 1 to 4: 


* For saving the file

Enter the filename to save / 'b' to go back: test9


* After file is saved

Data saved successfully

File name: test9.txt
File location: C:\Users\Sakib\Documents\GitHub\PythonProject-DataSoftware\test9.txt


* Exit

Exiting the software . . .

***Thank you***


License:


This code is licensed under the MIT License.


Contact:


If you have any questions or comments about this code, 
please feel free to contact me at nawazmdsakib@gmail.com .


