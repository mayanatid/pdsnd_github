import time
import pandas as pd
import numpy as np

# This is the code for the bikeshare project

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

month_options = [	'all', 'january', 'fubruary', 'february', 
					'march', 'april', 'may', 'june']

day_options = [	'all', 'monday', 'tuesday', 'wednesday', 
				'thursday', 'friday', 'saturday', 'sunday']

def create_counts_dict(df_column):
	# Used to create a dictionary out df.value_counts()
	# Input: a columns from a pd dataframe
	# Output: a dictionary with categories and counts
	value_count =  df_column.value_counts()
	count_dict = dict(zip(value_count.keys().tolist(), value_count.tolist()))
	return count_dict

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
        user_city = input("Please select a city from the following: chicago, new york city, washington: ").lower()
        if user_city in CITY_DATA.keys():
            print("You have picked {}".format(user_city))
            break
        else:
            print("{} is an invalid city\n".format(user_city))

   # TO DO: get user input for month (all, january, february, ... , june)
    while True: 
    	user_month = input("Please select a month from (all, january, february, ... , june): ").lower()
    	if user_month in month_options:
    		print("You picked {}".format(user_month))
    		break
    	else:
    		print("{} is not a valid month\n".format(user_month))
        


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
    	user_day = input("Please select a day from (all, monday, tuesday, ... sunday): ")
    	if user_day in day_options:
    		print("You picked {}".format(user_day))
    		break
    	else:
    		print("{} is not a valid day\n".format(user_day))



    print('-'*40)
    return user_city, user_month, user_day

def load_data(city, month, day):

    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract start hour
    df['hour'] = df['Start Time'].dt.hour

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    
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
        df = df[df['day_of_week'] == day.title()]
       
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month_index = int(df['month'].mode()) + 1
    popular_month = month_options[month_index]
    print("The most common month is: {}".format(popular_month.title()))


    # TO DO: display the most common day of week
    popular_weekday = df['day_of_week'].mode()
    print("The most common weekday is: {}".format(popular_weekday[0]))


    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()
    print("The most common start hour is: {}".format(popular_hour[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()
    print('The most commonly used start station is: {}'.format(popular_start_station[0]))
    #print(df['Start Station'].value_counts())


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()
    print('The most commonly used end station is: {}'.format(popular_end_station[0]))
    #print(df['End Station'].value_counts())


    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] = list(zip(df['Start Station'], df['End Station']))
    popular_trips = df['Trip'].mode()
    print('The most frequent start station and end station trip is: {}'.format(popular_trips[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: {} seconds'.format(total_travel_time))


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Average travel time: {} seconds'.format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):

    """Displays statistics on bikeshare users."""
    # NOTE: 'washington.csv' does not have birthyear or gender data
    # 'try' statements have been added to catch errors associated with 
    # 'Birth Year' and 'Gender' issues

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #TO DO: Display counts of user types
    try:
    	user_type_dict = create_counts_dict(df['User Type'])
    	print("User type breakdown:")
    	for key, value in user_type_dict.items():
    		print("{}: {}".format(key, value))
    except:
    	print("User type data not available")

    # TO DO: Display counts of gender
    try:
    	gender_dict = create_counts_dict(df['Gender'])
    	print("\nGender breakdown:")
    	for key, value in gender_dict.items():
    		print("{}: {}".format(key, value))
    except:
    	print("\nGender data not available")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
    	earliest_bday = int(df['Birth Year'].min())
    	recent_bday = int(df['Birth Year'].max())
    	common_bday = int(df['Birth Year'].mode())

    	print("\nBirth year statistics:")
    	print("Earliest birth year: {}".format(earliest_bday))
    	print("Most recent birth year: {}".format(recent_bday))
    	print("Most common birth year: {}".format(common_bday))

    except:
    	print("\nBirth year data not available")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(city):
    df = pd.read_csv(CITY_DATA[city])
    i = 0
    while True:
        raw_data_choice = input("Would you like to see individual trip data? Enter yes or no.\n")
        if raw_data_choice.lower() != 'yes':
            break
        else:
            print("printing data....")
            for j in range(5):
                print("{}\n".format(df.iloc[i].to_dict()))
                i += 1


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()