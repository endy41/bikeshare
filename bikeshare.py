# -*- coding: utf-8 -*-

import csv, pprint, datetime, time
import pandas as pd


## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'


def get_city(firstRequest=True):
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        Optional (bool) firstRequest is True for first call, if it is not first it should be False it affects prompt.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    if firstRequest:
        city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')
    else:
        city = input('\nPlease enter correct city name, I couldn''t support: Chicago, New York, or Washington?\n')
        
    file_name = ''
    # TODO: handle raw input and complete function
    if city.lower() == 'chicago':
        file_name = chicago
    elif city.lower() == 'new york':
        file_name = new_york_city
    elif city.lower() == 'washington':
        file_name = washington
    else:
        get_city(False)
    
    return file_name

def get_time_period(firstRequest=True):
    '''Asks the user for a time period and returns the specified filter.

    Args:
        Optional (bool) firstRequest is True for first call, if it is not first it should be False it affects prompt.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n')
    # TODO: handle raw input and complete function
    if time_period.lower() == 'month':
        file_name = time_period
    elif time_period.lower() == 'day':
        file_name = time_period
    elif time_period.lower() == 'not at all':
        file_name = time_period
    elif time_period.lower() == 'none':
        file_name = time_period
    else:
        get_time_period(False)
        
    return time_period

def get_month(firstRequest=True):
    '''Asks the user for a month and returns the specified month.

    Args:
        Optional (bool) firstRequest is True for first call, if it is not first it should be False it affects prompt.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
        (str) Month that user want to statistics for.
    '''
    month_value=0
    if firstRequest:
        month = input('\nWhich month? January, February, March, April, May, or June?\n')
    else:
        month = input('\nPlease enter correct values! January, February, March, April, May, or June?\n')
    # TODO: handle raw input and complete function
    if month.lower() == 'january':
        month_value = 1
    elif month.lower() == 'february':
        month_value = 2
    elif month.lower() == 'march':
        month_value = 3
    elif month.lower() == 'april':
        month_value = 4
    elif month.lower() == 'may':
        month_value = 5
    elif month.lower() == 'june':
        month_value = 6
    elif month.lower() == 'july':
        month_value = 7
    elif month.lower() == 'august':
        month_value = 8
    elif month.lower() == 'september':
        month_value = 9
    elif month.lower() == 'october':
        month_value = 10
    elif month.lower() == 'november':
        month_value = 11
    elif month.lower() == 'december':
        month_value = 12
    else:
        get_month(False)
        
    return month_value


def get_day(month, firstRequest=True):
    '''Asks the user for a day and returns the specified day.

    Args:
        Optional (bool) firstRequest is True for first call, if it is not first it should be False it affects prompt.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
        (str) day of the Month that user want to statistics for.
    '''
    day = input('\nWhich day? Please type your response as an integer.\n')
    # TODO: handle raw input and complete function
    if day>30:
        get_day(month,False)

    return day

def popular_month(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular month for start time?
    
    Args:
        city_file: (Str) city_file for city file name.
        time_period: (Str) time_period for time period inputs like month, day, not at all or none.
    returns:
        (Str) calculated most polular month.
    '''
    # TODO: complete function
    month_count_list = {}
        
    for row in city_file:
        start_month = pd.to_datetime(row['Start Time']).month
        if start_month in month_count_list:
            month_count_list[start_month] = month_count_list[start_month]+1
        else:
            month_count_list[start_month]=1

    '''
        dictionary max value for a dictionary can be found like this
    '''
    return max(month_count_list.keys(), key=lambda k: month_count_list[k])

def popular_day(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    Args:
        (Str) city_file for city file name.
        (Str) time_period for time period inputs like month, day, not at all or none.
    returns:
        (Str) calculated most polular day.
    '''
    # TODO: complete function
    day_count_list = {}
    
    for row in city_file:
        start_day = pd.to_datetime(row['Start Time']).weekday()
        if start_day in day_count_list:
            day_count_list[start_day] = day_count_list[start_day]+1
        else:
            day_count_list[start_day]=1

    '''
        dictionary max value for a dictionary can be found like this
    '''
    return max(day_count_list.keys(), key=lambda k: day_count_list[k])

def popular_hour(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular hour of day for start time?
    Args:
        (Str) city_file for city file name.
        (Str) time_period for time period inputs like month, day, not at all or none.
    returns:
        (Str) calculated most polular day.
    '''
    # TODO: complete function
    hour_count_list = {}
            
    for row in city_file:
        start_hour = pd.to_datetime(row['Start Time']).hour
        if start_hour in hour_count_list:
            hour_count_list[start_hour] = hour_count_list[start_hour]+1
        else:
            hour_count_list[start_hour]=1

    '''
        dictionary max value for a dictionary can be found like this
    '''
    return max(hour_count_list.keys(), key=lambda k: hour_count_list[k])

def trip_duration(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the total trip duration and average trip duration?
    Args:
        (Str) city_file for city file name.
        (Str) time_period for time period inputs like month, day, not at all or none.
    returns:
        (Str) calculated total trip duration and average trip duration
            formatted in (total_trip_duration, average_trip_duration).
    '''
    # TODO: complete function
    total_trip_duration = 0
    average_trip_duration = 0

    
    total_trip_duration = sum(int(item['Trip Duration']) for item in city_file)
    average_trip_duration = total_trip_duration/len(city_file)
        
    result = []
    result.append(total_trip_duration)
    result.append(average_trip_duration)
    return result


def popular_stations(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular start station and most popular end station?
    Args:
        (Str) city_file for city file name.
        (Str) time_period for time period inputs like month, day, not at all or none.
    returns:
        (Str) return most popular start station and end station
            formatted in (start_station, end_station).
    '''
    # TODO: complete function
    start_sta_count_list = {}
    end_sta_count_list = {}
    
    for row in city_file:
        start_station = row['Start Station']
        end_station = row['End Station']
        if start_station in start_sta_count_list:
            start_sta_count_list[start_station] = start_sta_count_list[start_station]+1
        else:
            start_sta_count_list[start_station]=1

        if end_station in end_sta_count_list:
            end_sta_count_list[end_station] = end_sta_count_list[end_station]+1
        else:
            end_sta_count_list[end_station]=1

    result = []
    result.append(max(start_sta_count_list.keys(), key=lambda k: start_sta_count_list[k]))
    result.append(max(end_sta_count_list.keys(), key=lambda k: end_sta_count_list[k]))
    return result


def popular_trip(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular trip?
    Args:
        (Str) city_file for city file name.
        (Str) time_period for time period inputs like month, day, not at all or none.
    returns:
        (Str) return the most popular trip formatted in start_station-end_station.
    '''
    # TODO: complete function
    trip_count_list = {}
    
    for row in city_file:
        trip = row['Start Station'] + ' - ' + row['End Station']
        if trip in trip_count_list:
            trip_count_list[trip] = trip_count_list[trip]+1
        else:
            trip_count_list[trip]=1

    '''
        dictionary max value for a dictionary can be found like this
    '''
    return max(trip_count_list.keys(), key=lambda k: trip_count_list[k])

def users(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of each user type?
    Args:
        (Str) city_file for city file name.
        (Str) time_period for time period inputs like month, day, not at all or none.
    returns:
        (Str) return a list that contains user types and counts.
    '''
    # TODO: complete function
    user_type_count_list = {}
    
    for row in city_file:
        user_type = row['User Type']
        if user_type in user_type_count_list:
            user_type_count_list[user_type] = user_type_count_list[user_type]+1
        else:
            user_type_count_list[user_type]=1

    '''
        dictionary max value for a dictionary can be found like this
    '''
    return user_type_count_list


def gender(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of gender?
    Args:
        (Str) city_file for city file name.
        (Str) time_period for time period inputs like month, day, not at all or none.
    returns:
        (Str) return a list that contains genders and counts.
    '''
    # TODO: complete function
    gender_count_list = {}
    
    for row in city_file:
        gender = row['Gender']
        if gender in gender_count_list:
            gender_count_list[gender] = gender_count_list[gender]+1
        else:
            gender_count_list[gender]=1

    return gender_count_list


def birth_years(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the earliest (i.e. oldest user), most recent (i.e. youngest user),
    and most popular birth years?
    Args:
        (Str) city_file for city file name.
        (Str) time_period for time period inputs like month, day, not at all or none.
    returns:
        (Str) return earliest, most recent, birth years
            formatted in (return_earliest, most_recent, birth_years).
    '''
    # TODO: complete function
    birth_years_list = {}
    
    for row in city_file:
        birth_year = row['Birth Year']
        if birth_year != '':
            if birth_year in birth_years_list:
                birth_years_list[birth_year] = birth_years_list[birth_year]+1
            else:
                birth_years_list[birth_year]=1

    result = []
    result.append(datetime.date.today().year-float(min(birth_years_list.items())[0]))
    result.append(datetime.date.today().year-float(max(birth_years_list.items())[0]))
    result.append(max(birth_years_list.keys(), key=lambda k: birth_years_list[k]))
    return result


def display_data(display_message):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    display = input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n')
    # TODO: handle raw input and complete function
    if display=='yes':
        for item in display_message:
            print(item)
    


def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    '''used to display message that is added by all functions'''
    display_message = []
    # Filter by city (Chicago, New York, Washington)
    city = get_city()

#    city = 'istanbul.csv' -- used for test
    
    # Filter by time period (month, day, none)
    time_period = get_time_period()
   
#    result = birth_years(city,time_period)
#    display_message.append(str('Earliest user is {} years old, oungest person is {} years old, and most popular birth years are {}').format(result[0], result[1], result[2]))
#    print(display_message)
#    return

    reader = list(csv.DictReader(open(city, newline='')))
       
    print('Calculating the first statistic...')

    # What is the most popular month for start time?
    if time_period == 'none':
        start_time = time.time()
        
        #TODO: call popular_month function and print the results
        display_message.append(str('\nMost popular month is {}').format(popular_month(reader,time_period)))
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

#    return max(day_count_list.keys(), key=lambda k: day_count_list[k])
    
    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == 'none' or time_period == 'month':
        start_time = time.time()
        
        # TODO: call popular_day function and print the results
        display_message.append(str('\nMost popular day is {}').format(popular_day(reader,time_period)))
        
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")    

    
    start_time = time.time()

    
    # What is the most popular hour of day for start time?
    # TODO: call popular_hour function and print the results
    display_message.append(str('\nMost popular hour is {}').format(popular_hour(reader,time_period)))
    
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    # TODO: call trip_duration function and print the results
    result = trip_duration(reader,time_period)
    display_message.append(str('\nTotal trip duration is {}, average duration is {}').format(result[0], result[1]))
    
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    # TODO: call popular_stations function and print the results
    result = popular_stations(reader,time_period)
    display_message.append(str('\nMost popular start station is {}, Most popular end station is {}').format(result[0],result[1]))
    
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular trip?
    # TODO: call popular_trip function and print the results
    display_message.append(str('\nMost popular trip is {} trip').format(popular_trip(reader,time_period)))
    
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of each user type?
    # TODO: call users function and print the results
    display_message.append(str('\nUser type counts are {}').format(users(reader,time_period)))
    
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of gender?
    # TODO: call gender function and print the results
    display_message.append(str('\nGender based user counts are {}').format(gender(reader,time_period)))
    
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
    # most popular birth years?
    # TODO: call birth_years function and print the results
    result = birth_years(reader,time_period)
    display_message.append(str('\nEarliest user is {} years old, oungest person is {} years old, and most popular birth years are {}').format(result[0], result[1], result[2]))
    
    print("That took %s seconds." % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like to
    display_data(display_message)

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
	statistics()