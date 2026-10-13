import pandas
data =pandas.read_csv("/Users/voshananissanka/Desktop/PythonDevelopment/Intermediate-Project/Squirrel_Visualisation/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20251224.csv")
grey_squirrel_count=len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count=len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count=len(data[data["Primary Fur Color"] == "Black"])

print (grey_squirrel_count)
print(black_squirrel_count)
print(red_squirrel_count)

data_dict ={
    "fur color" : ["Gray","Cinnamon","Black"],
    "Count": [grey_squirrel_count,red_squirrel_count,black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
