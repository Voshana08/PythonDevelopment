# with open("weather_data.csv") as data_file:
#     weather = data_file.readlines()
#     print(weather[2])
    
import csv


# with open("weather_data.csv") as data_file:
#     data =csv.reader(data_file)
#     # print(data)
#     tempretures =[]
#     for row in data:
        

#         tempretures.append(row[1])
            
#     tempretures.pop(0)
#     for i in range(len(tempretures)):
#         tempretures[i] =int(tempretures[i])   
        
        
        
        
#     print(tempretures)

#Working with Pandas
import pandas

data =pandas.read_csv("weather_data.csv")
print(data["temp"])
print(type(data))

data_dict=data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)
print(data['temp'].mean())