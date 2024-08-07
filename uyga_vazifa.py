import classes

try:
    minut = int(input("Enter the minutes: "))       
    time = classes.MinutesConverter(minut)
    print(time.toHours())    
except:
    print("Unknown problem occurred! ")

########################################################

# rocet1 = classes.SpaceAircraft("001",12,1000,10,5)
# rocet1.launch(10)
# rocet1.land(10)
# rocet1.info()
