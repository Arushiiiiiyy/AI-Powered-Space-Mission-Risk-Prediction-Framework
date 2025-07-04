# This program raises an error if the temperature goes out of range
# this program also checks if the pressure stays or goes out of range
# The maximum and minimum taken values are random , can be changed with 
#situation
temperature=int(input("Temperature="))
pressure=int(input("Pressure="))
max_allowed_t=-160
min_allowed_t=-170
max_allowed_p=10000
min_allowed_p=100
warning=0
if(temperature>max_allowed_t or temperature<min_allowed_t):
    warning=1

if(pressure<min_allowed_p or pressure>max_allowed_p):
    warning=1;


if(warning==1):
    print("WARNING")
    #here we can apply an AI-ML model which 
    #autonomously fixes the issue :)

else:
    print("SYSTEM WORKING")

#
