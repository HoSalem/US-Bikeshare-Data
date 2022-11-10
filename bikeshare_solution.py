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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:  
        city = input ('Please, choose the name of the city you want to explore: Chicago, New York, or Washington?\n').lower()
        if city in ['chicago', 'new york', 'washington']:
            break
        else:
             print ('Invalid city name,  Please choose a city form the available options.')
            
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input ('Which month would like to choose to filter the data? all (for no month filter), january, february, march, april, may. or june? Please enter the full name of the month.\n').lower()
        if month in ['all','january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print('Invalid input, please notice that data are only available for the first half of the year.\n')
   # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which day would like to choose to filter the data? all (for no day filter), monday, tuesday, ... sunday.\n').lower()
        if day in ['all','monday', 'tuesday', 'wednesday', 'thursday','friday']:
            break
        else:
              print('invalid input, please enter the full name of the day not an abbreviation ')    
         

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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['week_day'] = df['Start Time'].dt.weekday_name
    
   

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['week_day'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most common month :', common_month)

    # TO DO: display the most common day of week
    common_day = df['week_day'].mode()[0]
    print('Most common day of the week :', common_day)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most common start hour:', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station= df['Start Station'].mode()[0]
    print('Most commonly used start station:', start_station)


    # TO DO: display most commonly used end station
    end_station= df['End Station'].mode()[0]
    print('Most commonly used end station:', end_station)


    # TO DO: display most frequent combination of start station and end station trip
    station_combination = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('Most frequent combination of start station and end station trip:', station_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time= df['Trip Duration'].sum()
    print ('Total Travel Time: ', total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time= df['Trip Duration'].mean()
    print ('Mean Travel Time: ', mean_travel_time)
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender 
    if 'Gender' not in df:
        print('Gender Data not available for this city.\n')
        
    else:
        gender= df['Gender'].value_counts()
        print(gender)
   
   
   
        
   # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df:
        print('Birth Day Data not available for this city.\n') 
        
    else:
        print('Earliest year of birth:', int(df['Birth Year'].min()))
        print('Most recent year of birth:', int(df['Birth Year'].max()))
        print('Most common year of birth:', int(df['Birth Year'].mode()[0]))
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        # Ask the user if they want to see 5 lines of raw data and keep displaying the next 5 lines upon request.
        userinput= input('Would you like to see 5 lines of the raw data? Enter yes or no.\n')
        x=0 
        while userinput == 'yes':
            print(df.iloc[x:x+5])
            x+=5  
            userinput = input ('Would you like to see the next 5 lines? Enter yes or no.\n')
            
            
        else:
             restart = input('\nWould you like to restart? Enter yes or no.\n')
             if restart.lower() != 'yes':
                break
       


if __name__ == "__main__":
	main()