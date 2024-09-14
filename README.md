# Current_tennis_rankings
A python proejct that gets the current top 20 tennis players, both male and femalre (ATP & WTA). The script collects the data, performs a simple data cleaning of the data and ensures the data is in the same format every time,
and finally it appends it to two different sqlite tables (one for ATP and one for WTA). 

## needed packages
For the code to work you need to install the following packages:
Pandas and BeautifulSoup, for the tests to work you also need to install unittest.mock

## Using the program
To use the program simply download this github folder to your computer and run the "main.py" file, by using modules the main file will execute all the steps and the full pipeline is run. When complete the tables in the folder will be appended
with the current data. Since the tennis rankings are not updated daily one could using the scheduler on windows for example set the "main.py" to run on a weekly basis (when the rankings are updated) and always stay up to date with the 
current tennis rankings.


This project was done as a school project and further improvements could be made.
