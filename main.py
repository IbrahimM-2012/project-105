 
 import math 



 # list of elements to calculate
 import csv
 with open
 reader = csv.reader(f)
 file_data = list(reader)


 data = file_data[0]






  def mean(data):
  n =  len (data)
  total = 0
for x in data:
total += int(x)

mean = total / n
return mean




sqaured_list= []
for number in data:
a = int(number) - mean(data)
a= a**2
sqaured_list.append(a)


sum =0
for i in sqaured_list:
sum =sum + i


result = sum/ (len(data)-1)


std_deviation = math.sqrt(result)
print(std_deviation)
