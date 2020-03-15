"""

First, we want to import all needed packages, and intialize variables, constructor objects, etc. before 
running our main loop

"""


# import packages 

import csv
import time
import pandas as pd 
import matplotlib.pyplot as plt



# assign and open data file. When writing to the subset_every_thousand_row.csv file, the alternate 'fn2' variable 
# will need to be opened instead


fn = 'D:/Files/Engineering/Clarkson University - Data Analytics\
/IA626 - Big Data Processing & Cloud Services/NYC Taxi Project/trip_data_4.csv'
fn2 = 'C:/Users/Evariste/Documents/GitHub/NYCTaxiProject/subset_every_thousand_row.csv'

# assign variable to desired file to open, as well as whether writing to subset is to be done. These two 
# variables can be changed based on what you want the code to do 
file_used = fn 
write_subset = False 

# opening the desired file.  
f = open(file_used,"r")

# assign constructor object for csv reader object, so proper comma separated format is accounted for during 
# loop processing
reader = csv.reader(f)

# create new subset csv file and open the file in 'append mode', then assigning the constructor object 
# 'writer' to be used in the loop to write to the file. When the main taxi file is being processed on, 
# this part of the code needs to be commented-out

if write_subset is True: 
    f2 = open('subset_every_thousand_row.csv','w')
    f2.write("")
    f2.close()   
    f2 = open('subset_every_thousand_row.csv','a')
    writer = csv.writer(f2, delimiter=',',lineterminator='\n')

# intializing of various variables, lists, dictionaries,etc. to be used in the main loop below
n = 0

col_names = [] 
        
long_flag_list = []
lat_flag_list = []

long_flag2_list = []
lat_flag2_list = []

long_upper_range = 180 
long_lower_range = -180 

lat_upper_range = 90
lat_lower_range = -90

geo_empty_count = 0
geo_zero_count = 0

NY_long_range = [-80, -70]
NY_lat_range = [40,45]

vendorID_dist_dic = {}
ratecode_dist_dic = {}
storeandfwdflag_dist_dic = {}
passcount_dist_dic = {}


passenger_count_per_hour = {}


start = time.time()


# main loop 
for row in reader:
    """ 
    
    PROCESSING ON ALL ROWS, HEADER + DATA 
    
    """
    
    # if write_subset is selected, write every thousanth row to subset_every_thousand_row.csv file using 
    # csv.writer function
    if write_subset is True: 
        if n % 1000 == 0:
            writer.writerow(row)
    
    # collect number of columns
    col_numbers = len(row)
    
    """

    PROCESSING ON HEADER ROW ONLY 
    
    """
    
    if n == 0: 
        # collect name of headers in list variable 'col_names'
        col_names = row
        
        # Dataframe 'df' created to collect sample data in 
        df = pd.DataFrame(columns = col_names)
       
     
    """
    
    PROCESSING ON FIRST ROW OF DATA 
    
    """
    if n == 1:    
        # intializing the earliest pick-up time variable and the latest drop-off time variable 
        min_pickupdts = row[5]
        max_dropoffdts = row[6]
        
        
        # intializing max-min values for geo-locational fields; abitrarily intializing to first pickup longitude
        # and latitude observations
        max_geo_longitude = float(row[10])
        min_geo_longitude = float(row[10])
        max_geo_latitude = float(row[11])
        min_geo_latitude = float(row[11])
        
        
        # intilizing for passenger count, trip time, trip distance, to be used in max/min calculations below
        max_pass_count = int(row[7])
        min_pass_count = int(row[7])
       
        max_trip_time = int(row[8])
        min_trip_time = int(row[8])
       
        max_trip_dist = float(row[9])
        min_trip_dist = float(row[9])
        
    
    """
    
    PROCESSING ON ANY AND ALL DATA ROWS (ROW 1 - END)
    
    """
    if n > 0:   
        
        
        
        # split to seperate date and time portion of dts field
        dts_split_pickup = row[5].split(" ")
        dts_split_dropoff = row[6].split(" ")
        
        
        # isolate the two digit hour of the day variable 
        hour_pickup = dts_split_pickup[1].split(":")[0] 
        hour_dropoff = dts_split_dropoff[1].split(":")[0]
        
     
        # count up passengers within each hour of the day in dictionary 
        if hour_dropoff not in passenger_count_per_hour.keys():
            passenger_count_per_hour[hour_dropoff] = int(row[7])
        else:
            passenger_count_per_hour[hour_dropoff] += int(row[7])
        
        # this if statement ensures that if the drop-off and pick-up hours are the same, to not double count
        # the passenger count for that particular taxi trip
        if hour_pickup != hour_dropoff:
            if hour_pickup not in passenger_count_per_hour.keys():
                passenger_count_per_hour[hour_pickup] = int(row[7])
            else:
                passenger_count_per_hour[hour_pickup] += int(row[7])
      
        
        # min/max value calculation for row[7], row[8], row[9], passenger count, trip time,
        # trip distance, respectively
        
        if max_pass_count < int(row[7]):
            max_pass_count = int(row[7])
        if min_pass_count > int(row[7]):
            min_pass_count = int(row[7])
            
        if max_trip_time < int(row[8]):
            max_trip_time = int(row[8])
        if min_trip_time > int(row[8]):
            min_trip_time = int(row[8])
            
        if max_trip_dist < float(row[9]):
            max_trip_dist = float(row[9])
        if min_trip_dist > float(row[9]):
            min_trip_dist = float(row[9])
            
        
        
        
        # collecting and processing unique fields
        
        # Distinct value collection for vendor ID, row[2]
        if row[2] not in vendorID_dist_dic.keys():
            vendorID_dist_dic[row[2]] = 1 
        else: 
            vendorID_dist_dic[row[2]] += 1

        # Distinct value collection for rate code, row[3]
        if row[3] not in ratecode_dist_dic.keys():
            ratecode_dist_dic[row[3]] = 1 
        else: 
            ratecode_dist_dic[row[3]] += 1
            
        # Distinct value collection for store and fwd flag, row[4]
        if row[4] not in storeandfwdflag_dist_dic.keys():
            storeandfwdflag_dist_dic[row[4]] = 1 
        else: 
            storeandfwdflag_dist_dic[row[4]] += 1
            
        # Distinct value collection for passenger count, row[7]
        if row[7] not in passcount_dist_dic.keys():
            passcount_dist_dic[row[7]] = 1 
        else: 
            passcount_dist_dic[row[7]] += 1
        
        if n < 6:
            # appending to the sample-collection dataframe 'df' with each row of data looked at for the first 5 rows 
            # of data
            df.loc[len(df)] = row
        
        
        # compare and replace values for min_pickupdts and max_dropoffdts to derive at the min and max date values
        if row[5] < min_pickupdts:
            min_pickupdts = row[5] 
        if row[6] > max_dropoffdts:
            max_dropoffdts = row[6]         
        
        # assign variables to geo-locational data points for use in min/max processesing down below  
        pickuplong = row[10]
        pickuplat = row[11]
        dropofflong = row[12]
        dropofflat = row[13]
        
        
        # compare and replace min/max values longitude fields
        
        # for pick-up longitude field
        if pickuplong == "0":
            geo_zero_count += 1
        if pickuplong == "":
            geo_empty_count += 1 
            
        if pickuplong != "0" and pickuplong != "":
            
            if (float(pickuplong) > float(long_upper_range)) or (float(pickuplong) < float(long_lower_range)): 
                long_flag_list.append(pickuplong)
            elif (float(pickuplong) > float(NY_long_range[1])) or (float(pickuplong) < float(NY_long_range[0])):
                long_flag2_list.append(pickuplong)
            else:  
                if float(pickuplong) > max_geo_longitude:
                    max_geo_longitude = float(pickuplong)
                if float(pickuplong) < min_geo_longitude:
                    min_geo_longitude = float(pickuplong) 
                
        # for drop-off longitude field          

        if dropofflong == "0":
            geo_zero_count += 1
        if dropofflong == "":
            geo_empty_count += 1    
            
        if dropofflong != "0" and dropofflong != "":  
            
            if (float(dropofflong) > float(long_upper_range)) or (float(dropofflong) < float(long_lower_range)): 
                long_flag_list.append(dropofflong)
            elif (float(dropofflong) > float(NY_long_range[1])) or (float(dropofflong) < float(NY_long_range[0])):
                long_flag2_list.append(dropofflong)
            else:    
                if float(dropofflong) > max_geo_longitude:
                    max_geo_longitude = float(dropofflong)
                if float(dropofflong) < min_geo_longitude:
                    min_geo_longitude = float(dropofflong)
    
        
            
        # compare and replace max/min values for Latitude variables 
        
        # for pick up latitude values 
        if pickuplat == "0":
            geo_zero_count += 1
        if pickuplat == "":
            geo_empty_count += 1
        
        if pickuplat != "0" and pickuplat != "":
            
            
            if (float(pickuplat) > float(lat_upper_range)) or (float(pickuplat) < float(lat_lower_range)): 
                lat_flag_list.append(pickuplat)
            elif (float(pickuplat) > float(NY_lat_range[1])) or (float(pickuplat) < float(NY_lat_range[0])):
                lat_flag2_list.append(pickuplat)
            else:
                if float(pickuplat) > max_geo_latitude:
                    max_geo_latitude = float(pickuplat)
                if float(pickuplat) < min_geo_latitude:
                    min_geo_latitude = float(pickuplat)
        
            
         
        # for drop off latitude values
        if dropofflat == "0":
            geo_zero_count += 1
        if dropofflat == "":
            geo_empty_count += 1
            
        if dropofflat != "0" and dropofflat != "":    
            
            
            if (float(dropofflat) > float(lat_upper_range)) or (float(dropofflat) < float(lat_lower_range)): 
                lat_flag_list.append(dropofflat)
            elif (float(dropofflat) > float(NY_lat_range[1])) or (float(dropofflat) < float(NY_lat_range[0])):
                lat_flag2_list.append(dropofflat)
            else:
                if float(dropofflat) < min_geo_latitude:
                    min_geo_latitude = float(dropofflat)
                if float(dropofflat) > max_geo_latitude:
                    max_geo_latitude = float(dropofflat)
               
                    
        
    # printing of collected sample data in DataFrame df, column by column    
    if n == 10:
        for col in col_names:
            print(df[col])
          
        
    # truncate processing on data to specified row number for testing purposes
    ##if n == 10: 
    ##   break
        
        
    n += 1
    
# second loop; to create average passengers per hour dictionary 

passenger_average_per_hour = {}

for hour in passenger_count_per_hour:
    if int(hour) == 1 or int(hour) == 0:
        passenger_average_per_hour[int(hour)] = passenger_count_per_hour[hour] / 31
    else: 
        passenger_average_per_hour[int(hour)] = passenger_count_per_hour[hour] / 30
        

sorted_pass_avg_per_hour = {}

# to sort passenger_average_per_hour dictionary by keys values         
for key in sorted(passenger_average_per_hour.keys()):
    sorted_pass_avg_per_hour[key] = passenger_average_per_hour[key]


plt.bar(range(len(sorted_pass_avg_per_hour)), list(sorted_pass_avg_per_hour.values()), align='center')
plt.xticks(range(len(sorted_pass_avg_per_hour)), list(sorted_pass_avg_per_hour.keys()))

# plt.show()
    


print("\n") 
print("CPU processing time for all three loops: ", time.time() - start)  
print("\n")   
print("Number of columns: ", len(col_names))
print("Name of fields: ", col_names)
print("Number of rows in data:", n)  
print("\n") 
print("Dates range from %s to %s" % (min_pickupdts, max_dropoffdts))    
print("\n")   
print("FINAL longitude range: [%s:%s]" % (min_geo_longitude,max_geo_longitude))
print("FINAL latitude range: [%s:%s]" % (min_geo_latitude,max_geo_latitude))
print("\n") 
print("long range flag:", len(long_flag_list), "- percentage of data: %s%%" % ((len(long_flag_list)/n)*100))
print("lat range flag:", len(lat_flag_list), "- percentage of data: %s%%" % ((len(lat_flag_list)/n)*100))
print("geo empty string flag:", geo_empty_count, "- percentage of data: %s%%" % ((geo_empty_count/n)*100))
print("geo zero flag:", geo_zero_count, "- percentage of data: %s%%" % ((geo_zero_count/n)*100))
print("NY lat range flag:", len(lat_flag2_list), "- percentage of data: %s%%" % ((len(lat_flag2_list)/n)*100))
print("NY long range flag:", len(long_flag2_list), "- percentage of data: %s%%" % ((len(long_flag2_list)/n)*100))
print("\n") 
print("distinct vendor IDs:", vendorID_dist_dic)
print("distinct rate codes:", ratecode_dist_dic)
print("distinct store and fwd flags:", storeandfwdflag_dist_dic)
print("distinct passenger count:", passcount_dist_dic)
print("\n") 
print("passenger count range: [%s:%s]" % (min_pass_count,max_pass_count))
print("trip time range: [%s:%s]" % (min_trip_time,max_trip_time))
print("trip dist range: [%s:%s]" % (min_trip_dist,max_trip_dist))
