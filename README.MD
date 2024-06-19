This terminal application uses Pandas, CSV files, a batch file, and a python script to store health information about the user. I personally use this.

Instructions:

1. Run the command in terminal after clone: "python -m venv .venv "
2. Activate the virtual environement with: "./.venv/Scripts/Activate.ps1"
3. Download the required dependencies: "pip install -r requirements.txt"
4. Go to your task scheduler on windows and schedule the batch file to run at whatever interval you want

To set up on task scheduler:

1. Give it a good name
2. Make the trigger whatever time you want, this will be when the script fires
3. Make the action "Start a program" and browse/select the "runningTrackingScript.bat"
4. In add arguments, add the current working directory of this script for example: "C:\Users\Jack Branston\Desktop\healthMonitor"

Enjoy :)