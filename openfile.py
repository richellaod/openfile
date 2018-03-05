# Richella O'Driscoll 2018-03-05
#Iris Data Exercise

with open("data/iris.csv") as f:
      for line in f: 
            print('{:5} {:5} {:5} {:5}'.format(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3]))
     
