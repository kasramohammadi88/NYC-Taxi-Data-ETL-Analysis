import csv
import time

#start = time.time()

# open NYC Taxi data file 
fn = 'D:/Files/Engineering/Clarkson University - Data Analytics\
/IA626 - Big Data Processing & Cloud Services/NYC Taxi Project/trip_data_4.csv'
f = open(fn,"r")

# assign constructor object for csv reader object, so proper comma separated format is accounted for during 
# loop processing
reader = csv.reader(f)

# intializing row count variable 'n'
n = 0
# intialize start time to measure CPU time to process main loop
start = time.time()
# intialization of list of names of column headers
col_names = []
# main loop 
for row in reader:
    if n == 0: 
        col_names = row
    '''
    # intialization for max-min comparison at the first row of the data
    if n == 1: 
        max_pickupdts = row[5]
        min_pickupdts = row[5]
        max_dropoffdts = row[6]
        min_dropoffdts = row[6]
    # processing on all non-header data fields
    if n > 0:
        if row[5] > max_pickupdts:
            max_pickupdts = row[5]
        if row[5] < min_pickupdts:
            min_pickupdts = row[5] 
        if row[6] > max_dropoffdts:
            max_dropoffdts = row[5]
        if row[6] < min_dropoffdts:
            min_dropoffdts = row[5] 
    '''        
            
            
    #if n > 200:
    #    break
        
    n += 1
print("Number of columns: ", len(col_names))
print("Name of fields: ", col_names)
#print("Pick-up ranges from %s to %s" % (min_pickupdts, max_pickupdts))
#print("Drop-off ranges from %s to %s" % (min_dropoffdts, max_dropoffdts))          
print("Number of rows in data:", n)   
print("CPU processing time for main loop: ", time.time() - start)  

