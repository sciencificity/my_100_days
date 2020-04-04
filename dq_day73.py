import csv
import numpy as np

# import nyc_taxi.csv as a list of lists
# go to https://dsserver-prod-resources-1.s3.amazonaws.com/289/nyc_taxis.csv?versionId=JA41pZ57in3NIXYe9LgTf0LGTyex13QC
f = open("nyc_taxis.csv", "r")
taxi_list = list(csv.reader(f))

# remove the header row
taxi_list = taxi_list[1:]

# convert all values to floats
converted_taxi_list = []
for row in taxi_list:
    converted_row = []
    for item in row:
        converted_row.append(float(item))
    converted_taxi_list.append(converted_row)

# start writing your code below this comment
taxi = np.array(converted_taxi_list)
# print(taxi[1,:])
row_0 = taxi[0,:]
rows_391_to_500 = taxi[391:501,:]
row_21_column_5 = taxi[21,5]
row_0
rows_391_to_500
