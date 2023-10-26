Creating modifications to the _bikeshare.py_ code for evaluating bikeshare data sets for Chicago, New York City and Washington.

Applicable Files:
- _bikeshare.py_
  + python code for evaluating limited BikeShare data sets for Chicago, New York City and Washington (DC)
  + actively editing this python code in this share
- BikeShare city data files
  + _chicago.csv_, _new_york_city.csv_, _washington.csv_
  + input to the _bikeshare.py_ code
  + not being edited in this share.
  + identified in the _.gitignore_ file

Project Objectives;
#1 Popular times of travel
- most common month
- most common day of week
- most common hour of day
#2 Popular stations and trip
- most common start station
- most common end station
-most common trip from start to end
#3 Trip duration
- total travel time
- average travel time
#4 User info
- counts of each user type
- counts of each gender (only available for NYC and Chicago)
-earliest, most recent, most common year of birth (only available for NYC and Chicago)
Datasets:
Randomly selected data for the first six months of 2017 are provided for all three cities.
All three of the data files contain the same core six (6) columns:
- Start Time (e.g., 2017-01-01 00:07:57)
- End Time (e.g., 2017-01-01 00:20:53)
- Trip Duration (in seconds - e.g., 776)
- Start Station (e.g., Broadway & Barry Ave)
- End Station (e.g., Sedgwick St & North Ave)
- User Type (Subscriber or Customer)
The Chicago and New York City files also have the following two columns:
- Gender
- Birth Year

User Input/Options:
- Filter by city: New York City, Chicago or Washington
- Filter by month: January, February, March, April, May, June or
Any, if no preference
- Filter by day of week: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Any if no preference