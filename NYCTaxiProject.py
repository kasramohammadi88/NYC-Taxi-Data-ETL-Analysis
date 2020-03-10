import csv
import time
import pandas as pd 

start = time.time()

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
        
long_flag_list = []
lat_flag_list = []

long_upper_range = 180 
long_lower_range = -180 

lat_upper_range = 90
lat_lower_range = -90

# main loop 
for row in reader:
    #print("n is now: ", n)
    
    
    
    col_numbers = len(row)
    
    # processing on header row
    if n == 0: 
        # collect name of headers in list variable 'col_names'
        col_names = row
        
        # Dataframe 'df' created to collect sample data in 
        df = pd.DataFrame(columns = col_names)
        
     
    # processing on first row of data
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
        
       
        
    # processing on any and all non-header data fields (row 1-end)
    if n > 0:   
        
        if n < 6:
            # appending to the sample-collection dataframe 'df' with each row of data looked at for the first 5 rows 
            # of data
            df.loc[len(df)] = row
        
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
        if pickuplong != "0" and pickuplong != "":
            """
            if float(pickuplong) > float(long_upper_range):
                print("pick up Too high")
                print("pickuplong =", pickuplong)
                print("n is: ",n)
            if float(pickuplong) < float(long_lower_range):
                print("pick up Too low")
                print("pickuplong =", pickuplong)
                print("n is: ",n)
            """
            if (float(pickuplong) > float(long_upper_range)) or (float(pickuplong) < float(long_lower_range)): 
                ##print("Second IF statement worked for Pick Up LONG")
                ##print("n is: ", n)
                ##long_range_flag += 1 
                long_flag_list.append(pickuplong)
            else:  
                if float(pickuplong) > max_geo_longitude:
                    max_geo_longitude = float(pickuplong)
                if float(pickuplong) < min_geo_longitude:
                    min_geo_longitude = float(pickuplong) 
                
        # for drop-off longitude field           
        if dropofflong != "0" and dropofflong != "":  
            """
            if float(dropofflong) > float(long_upper_range):
                print("drop off Too high")
                print("dropofflong =", dropofflong)
                print("n is: ",n)
                
            if float(dropofflong) < float(long_lower_range):
                print("drop off Too low")
                print("dropofflong=", dropofflong)
                print("n is: ",n)
            """
            if (float(dropofflong) > float(long_upper_range)) or (float(dropofflong) < float(long_lower_range)): 
                ##print("Second IF statement worked for Drop Off LONG")
                ##print("n is: ", n)
                ##long_range_flag += 1 
                long_flag_list.append(dropofflong)
            else:    
                if float(dropofflong) > max_geo_longitude:
                    max_geo_longitude = float(dropofflong)
                if float(dropofflong) < min_geo_longitude:
                    min_geo_longitude = float(dropofflong)
    
        
            ##print("max long = ", max_geo_longitude)
            ##print("min long = ", min_geo_longitude)
        
            
            
            
        # compare and replace max/min values for Latitude variables 
        
        # for pick up latitude values 
        
        if pickuplat != "0" and pickuplat != "":
            """
            if float(pickuplat) > float(lat_upper_range):
                print("pick up Too high")
                print("pickuplat=", pickuplat)
                print("n is: ",n)
            if float(pickuplat) < float(lat_lower_range):
                print("pick up Too low")
                print("pickuplat =", pickuplat)
                print("n is: ",n)
            """
            
            if (float(pickuplat) > float(lat_upper_range)) or (float(pickuplat) < float(lat_lower_range)): 
                ##print("Second IF statement worked for Pick Up LAT")
                ##print("n is: ", n)
                ##lat_range_flag += 1 
                lat_flag_list.append(pickuplat)
            else:
                if float(pickuplat) > max_geo_latitude:
                    max_geo_latitude = float(pickuplat)
                if float(pickuplat) < min_geo_latitude:
                    min_geo_latitude = float(pickuplat)
            
         
        # for drop off latitude values
        
        if dropofflat != "0" and dropofflat != "":    
            """
            if float(dropofflat) > float(lat_upper_range):
                print("drop off Too high")
                print("dropofflat=", dropofflat)
                print("n is: ",n)
            if float(dropofflat) < float(lat_lower_range):
                print("drop off Too low")
                print("dropofflat =", dropofflat)
                print("n is: ",n)
            """
            
            if (float(dropofflat) > float(lat_upper_range)) or (float(dropofflat) < float(lat_lower_range)): 
                ##print("Second IF statement worked for Drop Off LAT")
                ##print("n is: ", n)
                ##lat_range_flag += 1 
                lat_flag_list.append(dropofflat)
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
    ##if n == 100000: 
    ##    break
        
        
       # preliminary code for spitting out sample data
      #  t = 0
       # for field in row:
          #  sample_data_lists.append(row[t])
          #  t += 1
            
    n += 1
    


print("\n")   
##print("Number of columns: ", len(col_names))
##print("Name of fields: ", col_names)
##print("Dates range from %s to %s" % (min_pickupdts, max_dropoffdts))      
##print("Number of rows in data:", n)   
print("CPU processing time for main loop: ", time.time() - start)  
print("FINAL min long = ", min_geo_longitude, "AND max long = ", max_geo_longitude)
print("FINAL min lat = ", min_geo_latitude, "AND max lat = ", max_geo_latitude) 
print("long range flag: ", len(long_flag_list))
print("lat range flag: ", len(lat_flag_list))
print("Long flag list = ", long_flag_list)
print("Lat flag list = ", lat_flag_list)

