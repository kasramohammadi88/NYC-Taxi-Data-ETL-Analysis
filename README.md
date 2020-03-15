# NYCTaxiProject

For this project, we were tasked with 10 inquiries into the data file given. The data file I chose to use was the 4th section of the NYCTaxi data, trip_data_4.csv. 

## Question 1: Time Range + Number of Rows 

The number of rows of the data is pretty straight forward to pin down. Namely, in our main loop, we iterate each row of the data and then keep a counter, 'n', which counts every iteration of our loop. The structure of the code for this part looks like this:  

```python
n = 0 

for row in reader:

n+=1 
```

and we then simply print out the value of n at the end to find the total number of rows of the dataset:

```python 
print("Number of rows in data:", n) 
``` 

and the result was the following: 
> **Number of rows in data: 15100469**




for the time range of the data, we take a look at the two time related fields: 

* pickup_datetime
* dropoff_datetime 

Logically, to find a accurate time range of the data, given the common sense domain understanding of a taxi fair, the earliest time stamp would be the earliest *pick-up* time, and the latest time stamp would be latest *drop-off* time. 

To accomplish the coding for the min pick-up and max drop-off values, we first intialize the min pick-up and max drop-off variables as the first variables seen for the fields in row 1:

```python
if n == 1:    
        # intializing the earliest pick-up time variable and the latest drop-off time variable 
        min_pickupdts = row[5]
        max_dropoffdts = row[6]
```

Now that we have the variables set, we set up the code that will compare each new pick-up and drop-off value to the already set max/min variables, as follows: 

```
if n > 0: 
# compare and replace values for min_pickupdts and max_dropoffdts to derive at the min and max date values
        if row[5] < min_pickupdts:
            min_pickupdts = row[5] 
        if row[6] > max_dropoffdts:
            max_dropoffdts = row[6]
```

Running this code, we 







