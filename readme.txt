This document for "Explore US Bike Sharing data" project.

Author: Ender Topuz
e-mail: endertopuz81@gmail.com

while doing project my notes are below
- How to get the data from input
    test = input(prompt) directly returns the prompted data to variable test
- read the data from csv
    I used csv module
    I learned the details from - https://docs.python.org/3/library/csv.html?highlight=csv
        with open('names.csv', newline='') as csvfile:
        ...reader = csv.DictReader(csvfile)
- to find the max value of a dictionary I googled it. from below page I found the solution
    https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
        stats = {'a':1000, 'b':3000, 'c': 100}
        max(stats.iterkeys(), key=lambda k: stats[k])
-firstly I used reader method in all the functions, but It caused performance problems, so I changed the code and just one time I am calling the reader
- reader couldn't be used more than one, so I convert it to list, so I could get the data one time
- I have added time perid and filter
- type conversion caused an error at if clause then I put the objects in str
- try to increase performance


my result is like that:

Hello! Let's explore some US bikeshare data!
Would you like to see data for Chicago, New York, or Washington?
chicago


Would you like to filter the data by month, day, or not at all? Type "none" for no time filter.
none
Reading data, Please wait...
That took 13.047913551330566 seconds.
Calculating the first statistic...
That took 86.74926352500916 seconds.
Calculating the next statistic...
That took 86.73048639297485 seconds.
Calculating the next statistic...
That took 121.41973686218262 seconds.
Calculating the next statistic...
That took 0.8658876419067383 seconds.
Calculating the next statistic...
That took 1.4850332736968994 seconds.
Calculating the next statistic...
That took 1.2763524055480957 seconds.
Calculating the next statistic...
That took 0.45093226432800293 seconds.
Calculating the next statistic...
That took 0.3600761890411377 seconds.
Calculating the next statistic...
That took 0.40435242652893066 seconds.


Would you like to view individual trip data?Type 'yes' or 'no'.
yes

Most popular month is June

Most popular day is Tuesday

Most popular hour is 17

Total trip duration is 1458069892, average duration is 939.7777590146342

Most popular start station is Streeter Dr & Grand Ave, Most popular end station is Streeter Dr & Grand Ave

Most popular trip is Lake Shore Dr & Monroe St - Streeter Dr & Grand Ave trip

User type counts are {'Customer': 317162, 'Subscriber': 1234339, 'Dependent': 4}

Gender based user counts are {'': 316867, 'Male': 935854, 'Female': 298784}

Earliest user is 119.0 years old, Youngest person is 2.0 years old, and most popular birth years are 1989.0


Would you like to restart? Type 'yes' or 'no'.
no