
If you are developing here are the dependencies 
pip install keyboard wheel pyttsx3 serial bs4 selenium python-tk nltk webdriver-manager pyserial pyinstaller

to create .exe file
pyinstaller --onefile --windowed --icon=web.ico main.py
pyinstaller --hidden-import=pyttsx3.drivers song_dl.py