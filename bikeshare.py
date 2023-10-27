import time
import pandas as pd
import numpy as np
"""
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
    """
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def user_input():
    """
    User input city, month, and day to assess.
    Returns:
        (str) city - city to analyze
        (str) month - month to filter by or 'Any' for no month filter
        (str) day - day of week to filter by or 'Any' for no day filter
    """
    print('Ready to assess city bikeshare data?\n')
    # user input city (Chicago, New York City, Washington).
    while True:
      city = input("Filter by New York City, Chicago or Washington?\n").lower()
      if city not in ('new york city', 'chicago', 'washington'):
        print("Please re-enter city\n")
        continue
      else:
        break
    # user input month (January, February, March, April, May, June or Any)
    while True:
      month = input("Filter by January, February, March, April, May, June\n or enter Any if you have no preference?\n").lower()
      if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'any'):
        print("Please re-enter a month or Any if none preferred\n")
        continue
      else:
        break
    # user input day of week (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Any)
    while True:
      day = input("\nFilter by day of week: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday\n or enter Any if you have no preference?\n").lower()
      if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'any'):
        print("Please enter day of week or Any if none preferred")
        continue
      else:
        break
    return city, month, day
def what(city, month, day):
    """
    Load data for the specified city and filter by month and day, if applicable.
    Args:
        (str) city - city to analyze
        (str) month - month to filter by or 'Any' to apply no month filter
        (str) day - day of week to filter by or 'Any' to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # loading data file
    df = pd.read_csv(CITY_DATA[city])
    # converting Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extractngi month and day of week from Start Time
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by month
    if month != 'any':
   	# indexing months
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    	# filter by month
        df = df[df['month'] == month]
        # filter by day of week
    if day != 'any':
        # filter by day of week
        df = df[df['day_of_week'] == day.title()]
    return df
def when(df):
    """most frequent travel times statistics"""
    print('\nMost frequent travel times...')
    start_time = time.time()
    # most frequent month
    frequent_month = df['month'].mode()[0]
    if frequent_month == 1:
        frequent_month == "January"
    elif frequent_month == 2:
        frequent_month == "February"
    elif frequent_month == 3:
        frequent_month == "March"
    elif frequent_month == 4:
        frequent_month == "April"
    elif frequent_month == 5:
        frequent_month == "May"
    elif frequent_month == 6:
        frequent_month == "June"
    print('   - most frequent month =', frequent_month)
    # most frequent day of week
    frequent_day = df['day_of_week'].mode()[0]
    print('   - most frequent day of week =', frequent_day)
    # most frequent start hour
    df['hour'] = df['Start Time'].dt.hour
    frequent_hour = df['hour'].mode()[0]
    if frequent_hour < 12:
        print('   - most frequent start hour =', frequent_hour, ' AM')
    elif frequent_hour >= 12:
        if frequent_hour > 12:
            frequent_hour -=12
            print('   - most frequent start hour =', frequent_hour, ' PM')        
def where(df):
    """most popular stations and trip"""
    print('\nMost popular stations and trip...')
    start_time = time.time()
    # most frequently used origin station
    origin_station = df['Start Station'].value_counts().idxmax()
    print('   - most used origin station =', origin_station)
    # most frequently used destination station
    destination_station = df['End Station'].value_counts().idxmax()
    print('   - most used destination station =', destination_station)
    # most frequent trip station combination
    trip_stations = df.groupby(['Start Station', 'End Station']).count()
    #frequent_trip = trip_stations.nlargest(1, 'count'), keep = 'first')
    print('   - most frequent trip station combination =\n', trip_stations)
def how_long(df):
    """total and average trip durations"""
    print('\nTrip duration stats...')
    start_time = time.time()
    # total trip time
    total_trip_time = sum(df['Trip Duration'])/3600
    total_trip_time = round(total_trip_time)
    print('   - cummulative user trip duration =', total_trip_time, " hours")
    # average trip time
    avg_trip_time = df['Trip Duration'].mean()/60
    avg_trip_time = round(avg_trip_time,1)
    print('   - average trip duration =', avg_trip_time, " minutes")
def who(df):
    """bikeshare user stats"""
    print('\nBikeshare user stats...')
    start_time = time.time()
    # bikeshare user types
    user_types = df['User Type'].value_counts()
    print('   - bikeshare user types =\n', user_types)
    # bikeshare user gender
    try:
      gender_types = df['Gender'].value_counts()
      print('   - bikeshare user genders =\n', gender_types)
    except KeyError:
      print("   >>> bikeshare user gender data unavailable for selected month <<<")
    # earliest, most recent, and most frequent year of birth
    try:
      earliest_year = df['Birth Year'].min()
      earliest_year = int(earliest_year)
      print('   - oldest bikeshare user birth year =', earliest_year)
    except KeyError:
      print("   >>> oldest bikeshare user birth year unavailable for selected month <<<")
    try:
      most_recent_year = df['Birth Year'].max()
      most_recent_year = int(most_recent_year)
      print('   - youngest bikeshare user birth year =', most_recent_year)
    except KeyError:
      print("   >>> youngest bikeshare user birth year unavailable for selected month <<<")
    try:
      most_common_year = df['Birth Year'].value_counts().idxmax()
      most_common_year = int(most_common_year)
      print('   - most common bikeshare user birth year =', most_common_year)
    except KeyError:
      print("   >>> most common bikeshare user birth year unavailable for selected month <<<")
def show(df):
    """print lines of bikeshare data"""
    show_data = input("\nWould you like to see 5 rows of data? yes or no.\n")
    start_show = 0
    show_length = 5
    end_show = start_show + show_length
    while True:
        if show_data.lower() == 'no':
            break
        elif show_data.lower() == 'yes':
            print("\n5 rows of bikeshare data.\n")
            print(df[start_show:end_show])
            start_show = start_show + show_length
            end_show = end_show + show_length
            show_data = input("\nShow 5 more lines of data? yes or no.\n")
            if show_data.lower() == 'no':
                break        
def main():
    while True:
        city, month, day = user_input()
        df = what(city, month, day)
        when(df)
        where(df)
        how_long(df)
        who(df)
        show(df)
        restart = input('\nRestart? yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
	main()
