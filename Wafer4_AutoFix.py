import pandas as pd  # To use matrices
import os  # To check directories
import time  # To add some delays for readability

# To open a file dialog so the user can select the files of interest
import tkinter
from tkinter import filedialog

print("\nFIXES incorrect x-y locations in selected Labview/Labjack output files")
print("from Wafer-4 given MANUALLY FIXED wafer_vctrl_sweep.csv file as input.\n\n")

print("Data must be in the following format in the manually fixed vctrl_sweep file:")
print("... | Y | X | Y(Real) | X(Real) | ...\n\n")

print("Files that you want to fix MUST be copied to your local machine before running")
print("this script. It does not have permission to access network drives.")
print("----------------------------------------------------------------------")

time.sleep(1.5)  # Allows the user time to read the message above.
# ------------------------------------------------------------------------------
print("\nSELECT MANUALLY FIXED Vctrl_Sweep FILE: ")
time.sleep(1)  # Another delay for readability

# Allow User to pick file that contains manually fixed X-Y data
tkinter.Tk().withdraw()  # Close the root window
input1 = filedialog.askopenfilename()
print("\nYou selected file:\n", input1, "\n")
input1 = str(input1)

# Check to see if directory/file exists
assert os.path.exists(input1), "File does not exist at, "+str(input1)

# Import data below and store in df
print("\nImporting Excel Workbook...")
dfVctrl = pd.read_excel(input1)
dfVctrl.values
print(dfVctrl)  # This DataFrame (df) contains the entire excel workbook
print("\n\nWorkbook Successfully Imported")
time.sleep(.5)
print("...")

# Locate Real X and Y values and store them for further use
time.sleep(.5)
print("Locating partID and real x and y values from manually corrected file")
time.sleep(1)
print('...')
XY_data = pd.DataFrame(dfVctrl, columns=['Part ID', 'Y', 'X', 'Y(Real)', 'X(Real)'])
XY_data = XY_data.drop_duplicates()  # Removes dupliacte rows from excel sheet
print("\n", XY_data)

# print(XY_data.size()) want to check size of matrix here

print("\nSuccessfully created master table of True X-Y values for each PartID!")
print("----------------------------------------------------------------------")
time.sleep(1.5)

# ------------------------------------------------------------------------------
print("\nSELECT Q MEASUREMENT FILE TO FIX: ")
time.sleep(1)
# Allow User to pick file that needs X-Y data to be FIXED
tkinter.Tk().withdraw()  # Close the root window
input2 = filedialog.askopenfilename()
print("\nYou selected file:\n", input2, "\n")
input2 = str(input2)

# Check to see if directory/file exists
assert os.path.exists(input2), "File does not exist at, "+str(input2)

# Import data below and store in df
print("\nImporting Excel Workbook...")
time.sleep(1)
# You can check encoding of file with notepad++
dfQ = pd.read_csv(input2, encoding="ansi")
dfQ.values
print(dfQ)  # This DataFrame (dfQ) contains the entire excel workbook
print("\n\nWorkbook Successfully Imported")
time.sleep(.5)
print("...")

# Search Q measurements CSV for "Chip ID" and matches it to corresponding
# "PartID" in the master table created from manually fixed file.
print("Matching PartID's to update proper X-Y values")
time.sleep(.5)
print("...")
IDs = pd.DataFrame(dfQ, columns=[' Chip ID'])
# IDs = dfQ["Chip ID"]
time.sleep(.5)
print(IDs)
s = IDs.size
print("\nSuccessfully extracted", s, "Chip ID's!")

# for x in range (0, s)

'''
-------------TEST CODE----------------

'''
