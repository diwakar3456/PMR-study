@echo off
:: Activate the conda environment
call conda activate pmrstudy

:: Run the Python script
python C:\Users\aaron\OneDrive\Documents\PMR-study\software\dispaly_gui.py

:: Optionally, deactivate the conda environment after running the script
conda deactivate

:: Keep the window open to see the output
pause
