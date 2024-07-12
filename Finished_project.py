import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    invalid = 0
    valid_inputs = ['chicago', 'new york', 'washington']
    while invalid == 0:
        city = str(input("Which city would you like to collect data for? Washington, Chicago, New York: "))
        if city.lower() in valid_inputs:
            print("Valid input")
            city = city.lower()
            invalid = 1
        else:
            print("Invalid input, please answer the question again")
            invalid = 0


    # get user input for month (all, january, february, ... , june)
    months_valid = 0
    months_list = ['all', 'january', 'feburary', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    while months_valid == 0:
        month = str(input("Select the month that you would like to gather data for: Eg. March "))
        if month.lower() in months_list:
            print("Valid input!")
            month = month.lower()
            months_valid = 1
        else:
            print("Invalid input, please answer the question again")
            months_valid = 0
    # get user input for day of week (all, monday, tuesday, ... sunday)
    dow_valid = 0
    dow_list = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while dow_valid == 0:
        day = str(input("Select the day of week that you would like to gather data for: Eg. Sunday "))
        if day.lower() in dow_list:
            print("Valid input!")
            day = day.lower()
            dow_valid = 1
        else:
            print("Invalid input, please select the right day")


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    try:
        df = pd.read_csv(CITY_DATA[city])
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.weekday
        m_list = ['all', 'january', 'feburary', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        d_list = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    
        if month not in m_list[0]:
            month = m_list.index(month) + 1
            df = df[df['month'] == month]
        elif day not in d_list[0]:
            df = df[df['day_of_week'] == day.title()]
    except KeyError:
        print("There are no values for the given filters")
        exit()

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    df['hour'] = df['Start Time'].dt.hour
    
    # display the most common month
    try:
        
        print("The most common month for Travel is", df['month'].mode()[0],"th Month")


    # display the most common day of week
        print("The most common day of the week for Travel is", df['day_of_week'].mode()[0],"th day of the week")
    

    # display the most common start hour
        print("The most common start hour for Travel is", df['hour'].mode()[0])
    except KeyError and IndexError:
        print("Unable to load data for common month, hours or week")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    try:
        S_E = df['Start Station'] + ' and ' + df['End Station']
        x = df['End Station'].mode()[0]
        y = df['Start Station'].mode()[0]
        
        
        print('\nCalculating The Most Popular Stations and Trip...\n')
        start_time = time.time()

    # display most commonly used start station
        print("Most commonly used start station was: ", y)


    # display most commonly used end station
        print("Most commonly used end station was: ", x)
    
    # display most frequent combination of start station and end station trip
        print("Most frequent combination of the start and end station for the trip was: ", S_E.mode()[0])


        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    except KeyError and IndexError:
        print("Unable to load statistical data for this filter")


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("The total time in this filter is: ", df["Trip Duration"].sum())

    # display mean travel time
    print("The mean travel time for the trip was: ", df["Trip Duration"].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts for user types is: ", user_types)

    # Display counts of
        
    try:
        gender = df['Gender'].value_counts()
        print("Counts for gender are: ", gender)
        birth = df['Birth Year']
        birth_recent = birth.max()
        birth_common = birth.mode()[0]
        birth_earliest = birth.min()
        print("The earliest year of birth is: ", birth_earliest)
        print("The most recent year of birth is: ", birth_recent)
        print("The most common year of birth is: ", birth_common)
    except KeyError and IndexError:
        
        print("There are no more values regarding user type")
        

    # Display earliest, most recent, and most common year of birth

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    

def display_data(df):
    display = 0
    start_loc = 0
    while display == 0:
        x = str(input("Would you like to see raw data?: (y/n) "))
        if x.lower() == 'y':
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
            display = 0
        elif x.lower() == 'n':
            print("Processed has stopped, Thank you!")
            display = 1
        else:
            print("invalid input")
            display = 0
            
def main():
    try:
        
        while True:
            city, month, day = get_filters()
            df = load_data(city, month, day)

            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            display_data(df)

            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break
    except KeyError:
        print("Error loading the data, filters unavailable")

if __name__ == "__main__":
	main()