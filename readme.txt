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
- I couldn't understand where I use the time period 