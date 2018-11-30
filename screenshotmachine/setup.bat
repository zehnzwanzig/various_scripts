mkdir "C:\screenshots"
mkdir "C:\screenshots\screenshots"
move "screenshot.py" "C:\screenshots"
move "start.bat" "C:\screenshots"
SchTasks /Create /SC DAILY /TN Screenshot /TR C:\screenshots\start.bat /ST 12:00