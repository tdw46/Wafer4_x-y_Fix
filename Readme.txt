----------------------------------------------------------------------
PRE-REQUISITES:

MUST RUN 'pip install -r requirements.txt' in the cmd prompt before running this python script.

Note: You can list all installed packages and store them in a requirements file by running: 
'pip freeze > requirements.txt'

----------------------------------------------------------------------
ABOUT:

FIXES incorrect x-y locations in selected Labview/Labjack output files
from Wafer-4 given MANUALLY FIXED wafer_vctrl_sweep.csv file as input.


Data must be in the following format in the manually fixed vctrl_sweep file:
... | Y | X | Y(Real) | X(Real) | ...


Files that you want to fix MUST be copied to your local machine before running
this script. It does not have permission to access network drives.

----------------------------------------------------------------------
NOTES:

MAKE SURE TO READ PROMPTS IN THE CMD as the Python script is running.

Files MUST BE SELECTED IN THE PROPER ORDER for the script to work.

----------------------------------------------------------------------