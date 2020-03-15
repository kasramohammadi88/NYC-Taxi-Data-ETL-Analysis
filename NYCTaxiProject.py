import csv
import time
import pandas as pd 
import matplotlib.pyplot as plt

start = time.time()

# open NYC Taxi data file 
fn = 'C:/Users/Evariste/Documents/GitHub/NYCTaxiProject/subset_every_thousand_row.csv'
##fn = 'D:/Files/Engineering/Clarkson University - Data Analytics\
##/IA626 - Big Data Processing & Cloud Services/NYC Taxi Project/trip_data_4.csv'
f = open(fn,"r")

# assign constructor object for csv reader object, so proper comma separated format is accounted for during 
# loop processing
reader = csv.reader(f)
"""
f2 = open('subset_every_thousand_row.csv','w')
f2.write("")
f2.close()   
f2 = open('subset_every_thousand_row.csv','a')
writer = csv.writer(f2, delimiter=',',lineterminator='\n')
"""
# intializing row count variable 'n'
n = 0

# intialize start time to measure CPU time to process main loop
start = time.time()
# intialization of list of names of column headers
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

bar_chart_test = {1:1, 2:12, 3:51}

    
    


# main loop 
for row in reader:
    """ 
    
    PROCESSING ON ALL ROWS, HEADER + DATA 
    
    """
    
    # write every thousanth row to subset_every_thousand_row.csv file using csv.writer function
    ##if n % 1000 == 0:
    ##    writer.writerow(row)
    
    
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
        # and latitude observation
        max_geo_longitude = float(row[10])
        min_geo_longitude = float(row[10])
        max_geo_latitude = float(row[11])
        min_geo_latitude = float(row[11])
        
        
        #print(max_geo_latitude, "\n", min_geo_latitude, "\n", max_geo_longitude, "\n", min_geo_longitude)
        #print("type of geo data is: ", type(min_geo_longitude), type(min_geo_latitude), type(max_geo_latitude), type(max_geo_longitude))
        
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
        
        if hour_pickup != hour_dropoff:
            if hour_pickup not in passenger_count_per_hour.keys():
                passenger_count_per_hour[hour_pickup] = int(row[7])
            else:
                passenger_count_per_hour[hour_pickup] += int(row[7])
      
                
        
        
        ##print(passenger_count_per_dayhour)
        
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
            
        # calculating average number of passengers per hour in the data 
        
        
        
       
       
        
        
            
        
        
        ## how to append to a list that is a value of a key of a dictionary 
        ##passenger_count_per_hour[0].append(2)
        
        
        
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
        
        ##if n < 6:
            # appending to the sample-collection dataframe 'df' with each row of data looked at for the first 5 rows 
            # of data
        ##    df.loc[len(df)] = row
        
        #print(row[10], row[12])
        #print(row[11], row[13])
        
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
        
        # for any occurance of an empty string, automatically replace that value with 0 and load into 
        # corresponding variable
        
            ##print("\npick up long value: ", pickuplong, "AND drop off long value", dropofflong)
          
            ##print("pick up long type = ", type(pickuplong), "AND drop off long type = ", type(dropofflong))
            
        # compare and replace max/min values for Longitude variables 
            ##print("pick up long is 0:" , pickuplong == "0")
            ##print("drop off long is 0:" , dropofflong == "0")
        
        
        ##if n == 59246:
        ##    print("drop off lat @ n = 59246: ", dropofflat)
        
        
        ##test = 100
        
        ##if float(upper_range) > float(test):
        ##    print("test works!")
            
        # for pickup longitude field
        if pickuplong == "0":
            geo_zero_count += 1
        if pickuplong == "":
            geo_empty_count += 1 
            
        if pickuplong != "0" and pickuplong != "":
            
            if (float(pickuplong) > float(long_upper_range)) or (float(pickuplong) < float(long_lower_range)): 
                ##print("Second IF statement worked for Pick Up LONG")
                ##print("n is: ", n)
                ##long_range_flag += 1 
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
                ##print("Second IF statement worked for Drop Off LONG")
                ##print("n is: ", n)
                ##long_range_flag += 1 
                long_flag_list.append(dropofflong)
            elif (float(dropofflong) > float(NY_long_range[1])) or (float(dropofflong) < float(NY_long_range[0])):
                long_flag2_list.append(dropofflong)
            else:    
                if float(dropofflong) > max_geo_longitude:
                    max_geo_longitude = float(dropofflong)
                if float(dropofflong) < min_geo_longitude:
                    min_geo_longitude = float(dropofflong)
    
        
            ##print("max long = ", max_geo_longitude)
            ##print("min long = ", min_geo_longitude)
        
            
            
            
        # compare and replace max/min values for Latitude variables 
        
        # for pick up latitude values 
        if pickuplat == "0":
            geo_zero_count += 1
        if pickuplat == "":
            geo_empty_count += 1
        
        if pickuplat != "0" and pickuplat != "":
            
            
            if (float(pickuplat) > float(lat_upper_range)) or (float(pickuplat) < float(lat_lower_range)): 
                ##print("Second IF statement worked for Pick Up LAT")
                ##print("n is: ", n)
                ##lat_range_flag += 1 
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
                ##print("Second IF statement worked for Drop Off LAT")
                ##print("n is: ", n)
                ##lat_range_flag += 1 
                lat_flag_list.append(dropofflat)
            elif (float(dropofflat) > float(NY_lat_range[1])) or (float(dropofflat) < float(NY_lat_range[0])):
                lat_flag2_list.append(dropofflat)
            else:
                if float(dropofflat) < min_geo_latitude:
                    min_geo_latitude = float(dropofflat)
                if float(dropofflat) > max_geo_latitude:
                    max_geo_latitude = float(dropofflat)
               
                
       ## if n % 100 == 0: 
            ##print("n = ", n)
            ##print("CURRENT min long = ", min_geo_longitude, "AND max long = ", max_geo_longitude)
            ##print("CURRENT min lat = ", min_geo_latitude, "AND max lat = ", max_geo_latitude) 
            
    
        
    # printing of collected sample data in DataFrame df, column by column    
    ##if n == 10:
    ##    for col in col_names:
    ##        print(df[col])
          
        
    # truncate processing on data to specified row number
    ##if n == 10: 
    ##   break
        
        
       # preliminary code for spitting out sample data
      #  t = 0
       # for field in row:
          #  sample_data_lists.append(row[t])
          #  t += 1
            
    n += 1
    
# loop to create average passengers per hour 

passenger_average_per_hour = {}

for hour in passenger_count_per_hour:
    if int(hour) == 1 or int(hour) == 0:
        ##print("00 or 01 recognized!")
        passenger_average_per_hour[int(hour)] = passenger_count_per_hour[hour] / 31
    else: 
        ##print("NOT 00 or 01 recognized!")
        passenger_average_per_hour[int(hour)] = passenger_count_per_hour[hour] / 30
        
        
#print(passenger_average_per_hour)

sorted_pass_avg_per_hour = {}
        
for key in sorted(passenger_average_per_hour.keys()):
    sorted_pass_avg_per_hour[key] = passenger_average_per_hour[key]

print(sorted_pass_avg_per_hour)

plt.bar(range(len(sorted_pass_avg_per_hour)), list(sorted_pass_avg_per_hour.values()), align='center')
plt.xticks(range(len(sorted_pass_avg_per_hour)), list(sorted_pass_avg_per_hour.keys()))
# # for python 2.x:
# plt.bar(range(len(D)), D.values(), align='center')  # python 2.x
# plt.xticks(range(len(D)), D.keys())  # in python 2.x

plt.show()
    




print("\n")   
##print("Number of columns: ", len(col_names))
#print("Name of fields: ", col_names)
print("Dates range from %s to %s" % (min_pickupdts, max_dropoffdts))      
##print("Number of rows in data:", n)   
print("CPU processing time for main loop: ", time.time() - start)  
#print("FINAL longitude range: [%s:%s]" % (min_geo_longitude,max_geo_longitude))
#print("FINAL latitude range: [%s:%s]" % (min_geo_latitude,max_geo_latitude))
#print("long range flag:", len(long_flag_list), "- percentage of data: %s%%" % ((len(long_flag_list)/n)*100))
#print("lat range flag:", len(lat_flag_list), "- percentage of data: %s%%" % ((len(lat_flag_list)/n)*100))
#print("geo empty string flag:", geo_empty_count, "- percentage of data: %s%%" % ((geo_empty_count/n)*100))
#print("geo zero flag:", geo_zero_count, "- percentage of data: %s%%" % ((geo_zero_count/n)*100))
#print("NY lat range flag:", len(lat_flag2_list), "- percentage of data: %s%%" % ((len(lat_flag2_list)/n)*100))
#print("NY long range flag:", len(long_flag2_list), "- percentage of data: %s%%" % ((len(long_flag2_list)/n)*100))
#print("distinct vendor IDs:", vendorID_dist_dic)
#print("distinct rate codes:", ratecode_dist_dic)
#print("distinct store and fwd flags:", storeandfwdflag_dist_dic)
#print("distinct passenger count:", passcount_dist_dic)
##print("NY long range flag list = ", long_flag2_list)
##print("NY lat range flag list = ", lat_flag2_list)

##print("Long flag list = ", long_flag_list)
##print("Lat flag list = ", lat_flag_list)

#print("passenger count range: [%s:%s]" % (min_pass_count,max_pass_count))
#print("trip time range: [%s:%s]" % (min_trip_time,max_trip_time))
#print("trip dist range: [%s:%s]" % (min_trip_dist,max_trip_dist))


##print("passenger_count_per_hour = ", passenger_count_per_hour)
