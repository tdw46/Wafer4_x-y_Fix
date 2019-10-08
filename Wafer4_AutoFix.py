import pandas as pd  # To use matrices
import os  # To check directories
import time  # To add some delays for readability

# To open a file dialog so the user can select the files of interest
import tkinter
from tkinter import filedialog
from tkinter import messagebox

print("----------------------------------------------------------------------")
print("\n\nFIXES incorrect x-y locations in selected Labview/Labjack output files")
print("from Wafer-4 given MANUALLY FIXED wafer_vctrl_sweep.csv file as input.\n\n")

print("Data must be in the following format in the manually fixed vctrl_sweep file:")
print("... | Y | X | Y(Real) | X(Real) | ...\n\n")
print("----------------------------------------------------------------------")

# time.sleep(1.5)  # Allows the user time to read the message above.
# ------------------------------------------------------------------------------
print("\nSELECT MANUALLY FIXED Vctrl_Sweep FILE: ")
# time.sleep(1)  # Another delay for readability

# Allow User to pick file that contains manually fixed X-Y data
tkinter.Tk().withdraw()  # Close the root window
messagebox.showinfo("MESSAGE", "SELECT MANUALLY FIXED Vctrl_Sweep FILE:")
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

#print(dfVctrl.loc[:, :'X'])  # slice from the beginning to 'Y'

print("\nSuccessfully created master table of True X-Y values for each PartID!")
print("----------------------------------------------------------------------")
# time.sleep(1.5)

# ------------------------------------------------------------------------------
print("\nSELECT Q MEASUREMENT FILE TO FIX: ")
messagebox.showinfo("MESSAGE", "SELECT Q MEASUREMENT FILE TO FIX:")
# time.sleep(1)
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
IDs = pd.DataFrame(dfQ, columns=[' Chip ID'])  # NOTE the blank space
# print(dfQ.columns)  #prints all column headers. Useful to find hidden blank spaces
time.sleep(.5)
print(IDs)
s = IDs.size
print("\nSuccessfully extracted", s, "Chip ID's!")

time.sleep(.5)
columns = ['X(Real)', 'Y(Real)']  # Initialize headers for dataframe
insert = pd.DataFrame(index=dfQ.index, columns=columns)  # dataframe with same index as dfQ
insert = insert.fillna(0)  # with 0s rather than NaNs
print("...\nMatching Measured Q ID's to Master Table...")
for x in range(0, s):
    curID = IDs.loc[x, ' Chip ID']  # temp to store a single ID for matching
    matchID = XY_data['Part ID'] == curID  # find match in XY_data (bool)
    matches = XY_data[matchID]
    # print(matches.head())  # DEBUG Print matches, to make duplicates evident
    # print(matches.index[0])  # DEBUG

    # Update dfQ with real X and Y values based on dfVcntrl XY_values
    for y in range(0, matches['Part ID'].size):
        # Add X(Real) and Y(Real) in the order they appear
        # Add data to a new dataframe, "insert," which will have X(Real) and Y(Real) values to insert between existing columns in dfQ
        if matches['Part ID'].size > 1:
            insert.loc[x,'X(Real)'] = 'Check xVal'  # x is the the current index in dfQ we are fixing
            insert.loc[x,'Y(Real)'] = 'Check yVal'
            # print(matches.index[y])  # DEBUG
            # print(insert)  # DEBUG
        else:
            xVal = matches.loc[matches.index == matches.index[y]]['X(Real)'].values
            yVal = matches.loc[matches.index == matches.index[y]]['Y(Real)'].values
            insert.loc[x,'X(Real)'] = xVal[0]  # used index = [0] here to get ints
            insert.loc[x,'Y(Real)'] = yVal[0]
            # print(matches.index[y])  # DEBUG
            # print(insert)  # DEBUG
# print(dfQ.loc[:, :' Y'])
# print(insert)

dfQ_New = pd.concat([dfQ.loc[:, :' Y'], insert, dfQ.loc[:, ' Q half-width':]], axis=1)
print("\n\n Q-MEASUREMENT DATA SUCCESSFULLY FIXED!")
time.sleep(1)  # For readability
print("\n", dfQ_New.loc[:,' X':' Q half-width'])

# Allow User to pick file that needs X-Y data to be FIXED
tkinter.Tk().withdraw()  # Close the root window
messagebox.showinfo("MESSAGE", "SELECT DIRECTORY TO SAVE FIXED Q MEASUREMENT FILE:")
input3 = filedialog.asksaveasfilename()
dfQ_New.to_csv(input3)

'''
-------------TEST CODE----------------

'''
