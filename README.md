# NYCTaxiProject

For this project, we were tasked with 10 inquiries into the data file given. The data file I chose to use was the 4th section of the NYCTaxi data, trip_data_4.csv. 

## Question 1: Time Range + Number of Rows 

The number of rows of the data is pretty straight forward to pin down. Namely, in our main loop, we iterate each row of the data and then keep a counter, 'n', which counts every iteration of our loop. 

```python
n = 0 

for row in reader:

n+=1 
```
