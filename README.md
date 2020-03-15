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
        min_pickupdts = row[5]
        max_dropoffdts = row[6]
```

Now that we have the variables set, we set up the code that will compare each new pick-up and drop-off value to the already set max/min variables, as follows: 

```
if n > 0: 
        if row[5] < min_pickupdts:
            min_pickupdts = row[5] 
        if row[6] > max_dropoffdts:
            max_dropoffdts = row[6]
```

Running this code, we get the following time range for the data: 

```python
print("Dates range from %s to %s" % (min_pickupdts, max_dropoffdts))
``` 
> **Dates range from 2013-04-01 00:00:00 to 2013-05-01 02:19:25**


## Question 2: Field Names + Descriptions

Next, we want to know the name of the fields, or the columns, of the dataset. We simple use this code within the main loop, specifically at row 0, the header row, to find out the name of the fields: 

```python
if n == 0:
        col_names = row

```

and then print the results: 

```python
print("Name of fields: ", col_names)
```
> **Name of fields:  ['medallion', ' hack_license', ' vendor_id', ' rate_code', ' store_and_fwd_flag', ' pickup_datetime', ' dropoff_datetime', ' passenger_count', ' trip_time_in_secs', ' trip_distance', ' pickup_longitude', ' pickup_latitude', ' dropoff_longitude', ' dropoff_latitude']**

Some fields are self-explanatory in their meanings, and others less so. Some of the field descriptions that may not be self-explanatory from their names alone were able to be figured out by looking over the sample data from the datafile (*See Question 3*)

1. *medallion*: a 32 character ID of sorts consisting of letter and numbers 
2. *hack_license*: a 32 character ID of sorts consisting of letter and numbers 
3. *vendor_id*: potentially the vendor ID of the taxi company 
4. *rate_code*: potentially code of rate of charge of the taxi fair 
5. *store_and_fwd_flag*: a boolean flag consisting of 'N' or 'Y' values
6. *pickup_datetime*: datetime of pickup 
7. *dropoff_datetime*: datetime of dropoff
8. *passenger_count*: number of passengers in the taxi during the trip
9. *trip_time_in_secs*: time in seconds of trip 
10. *trip_distance*: distance of trip (units is unknown; likely is miles or km from the looks of the sample data)
11. *pickup_longitude*: longitude decimal value of pickup location 
12. *pickup_latitude*: latitude decimal value of pickup location
13. *dropoff_longitude*: longitude decimal value of dropoff location
14. *dropoff_latitude*: latitude deciaml value of dropoff location 

## Question 3: Sample Data 

To get a feel for the data, we can take a look at a small sample of the data. For this case, I decided 5 rows of data would be succifient for the purpose of getting an idea of what the data looked like. To do this, since the memory usage would be very minimal with a 5 row, 14 column array, I assigned a dataframe from the pandas library to store the sample data. 

First, for the header row, I assigned the name of the columns to the dataframe: 

```python 
if n == 0: 
        df = pd.DataFrame(columns = col_names)
```

Next, the code to add the first 5 rows of the dataset into the dataframe: 

```python 

if n < 6:
    df.loc[len(df)] = row

```

And lastly, to print the sample data to the console:
(*note: n==10 as a condition was chosen at random, the only requirement for this number is that it is greater than 5*)

```python
if n == 10:
        for col in col_names:
            print(df[col])
```


And viola! We get to peep into what the large dataset looks like at a very small scale: 
(*note: alternatively, the sample data could have been collected in a dictionary of lists as well. That method may have been more memory-efficient, potentially. However, due to the small sample number that was collected, the difference between the two methods would be very small)

> * 0    91F6EB84975BBC867E32CB113C7C2CD5
> * 1    EC34CD1B3797DFAFF3FE099BA87B6656
> * 2    C1B9DA774DC2BBC6DE27CE994E7F44A0
> * 3    9BA84250355AB3FC031C9252D395BF8A
> * 4    205A696DF62AD03C88DA8C5EC5248639
> * Name: medallion, dtype: object
> * 0    AD8751110E6292079EB10EB9481FE1A6
> * 1    8FE6A4AEDF89B6B4E19D2377FD3FB7D7
> * 2    E1B595FD55E4C82C1E213EB17438107A
> * 3    16BB0D96A0DCC853AEC7F55C8D6C71E0
> * 4    579C41EA5EC846F8B641A42F9EE3E855
> * Name:  hack_license, dtype: object
> * 0    CMT
> * 1    CMT
> * 2    CMT
> * 3    CMT
> * 4    CMT
> * Name:  vendor_id, dtype: object
> * 0    1
> * 1    1
> * 2    1
> * 3    1
> * 4    1
> * Name:  rate_code, dtype: object
> * 0    N
> * 1    N
> * 2    N
> * 3    N
> * 4    N
> * Name:  store_and_fwd_flag, dtype: object
> * 0    2013-04-04 18:47:45
> * 1    2013-04-05 07:08:34
> * 2    2013-04-04 17:59:50
> * 3    2013-04-04 18:12:01
> * 4    2013-04-04 20:12:57
> * Name:  pickup_datetime, dtype: object
> * 0    2013-04-04 19:00:25
> * 1    2013-04-05 07:17:34
> * 2    2013-04-04 18:21:48
> * 3    2013-04-04 18:25:24
> * 4    2013-04-04 20:29:55> 
> * Name:  dropoff_datetime, dtype: object
> * 0    1
> * 1    1
> * 2    1
> * 3    1
> * 4    1
> * Name:  passenger_count, dtype: object
> * 0     759
> * 1     540
> * 2    1318
> * 3     799
> * 4    1017
> * Name:  trip_time_in_secs, dtype: object
> * 0    2.50
> * 1    1.60
> * 2    3.60
> * 3    1.90
> * 4    3.60
> * Name:  trip_distance, dtype: object
> * 0    -73.957855
> * 1             0
> * 2     -73.98288
> * 3    -73.978119
> * 4    -74.006371
> * Name:  pickup_longitude, dtype: object
> * 0     40.76532
> * 1            0
> * 2     40.75499
> * 3    40.763451
> * 4    40.744755
> * Name:  pickup_latitude, dtype: object
> * 0    -73.976273
> * 1             0
> * 2    -74.009186
> * 3    -73.955666
> * 4    -73.961662
> * Name:  dropoff_longitude, dtype: object
> * 0    40.785648
> * 1            0
> * 2    40.715374
> * 3    40.776642
> * 4    40.761082
> * Name:  dropoff_latitude, dtype: object


## Question 4: SQL Data types for fields 

Looking over the sample data from *Question 3* above, as well as looking at the distinct values of each field (*Question 6*) and max/min values (*Question 7*), the SQL data type needed for each field becomes more apparent. Namely, the following data types would best fit for each data field:  

1. *medallion*: varchar(32)
2. *hack_license*: varchar(32)
3. *vendor_id*: varchar(3) 
4. *rate_code*: int
5. *store_and_fwd_flag*: varchar(1)
6. *pickup_datetime*: datetime
7. *dropoff_datetime*: datetime
8. *passenger_count*: int
9. *trip_time_in_secs*: int 
10. *trip_distance*: decimal(3,1)
11. *pickup_longitude*: decimal(2,6)
12. *pickup_latitude*: decimal(2,6)
13. *dropoff_longitude*: decimal(2,6)
14. *dropoff_latitude*: decimal(2,6)


## Question 5
