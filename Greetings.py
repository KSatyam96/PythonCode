# import datetime
import time

# str = datetime.datetime.now()
# print("datetime.datetime.now() >>", datetime.datetime.now())
# print(datetime.time.hour())
# print(datetime.time())

# print(time.localtime())
# print(time.strftime('%H:%M:%Y'))

name = input("Enter you name : ")
hour = int(time.strftime('%H'))

print('\n')

if ( hour > 12 ):
    print ("Good Evening", name)
elif (hour == 12):
    print ("Good After ",name)
else:
    print ("Good Morning",name)