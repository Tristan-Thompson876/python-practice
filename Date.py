import datetime

d = datetime.date(2017, 7 ,7)
present_d = datetime.date.today()
print(present_d)
print(d)

#isoweekday monday is 1 and sunday 7 whereas
#weekday monday 0 is and sunday 6

#example
print(present_d.isoweekday())
print(present_d.weekday())

#In use
daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
thisDAy = daysOfWeek[present_d.isoweekday()]
also_thisDAy = daysOfWeek[present_d.weekday()]
print(thisDAy)
print("Woooh it is " + also_thisDAy + " Lets have fun")

#datetime
dt = datetime.datetime(2024, 1, 15, 12, 45, 10, 10000)
print(dt.date())
print(dt.time())

#not the best way since this doesnt account for leap years
tdelta = datetime.timedelta(days = 21 * 365)
print(dt - tdelta)
