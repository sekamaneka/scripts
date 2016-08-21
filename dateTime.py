import datetime
from astral import Astral
import subprocess

city_name = 'Vienna'
now_time = datetime.datetime.now()
a = Astral()
city = a[city_name]
sun = city.sun(date=datetime.date.today(), local=True)

#print ('%s/%s\n' % (city_name, city.region))
#print('Dawn:	%s' % str(sun['dawn'])[-15:-6])
#print('Sunrise:	%s' % str(sun['sunrise'])[-15:-6])
#print('Sunset:	%s' % str(sun['sunset'])[-15:-6])
#print(datetime.datetime.now())
#print(sun['dawn'].replace(tzinfo=None))
#print(datetime.datetime.now() < sun ['dawn'].replace(tzinfo=None))

sunrise_time = sun['sunrise'].replace(tzinfo=None)
sunset_time = sun['sunset'].replace(tzinfo=None)

if (now_time > sunset_time): 
	subprocess.call(["gatttool","-b", "68:9E:19:16:64:33", "--char-write-req", "-a", "0x002d", "-n", "0000ff00"])	
else:
	subprocess.call(["gatttool","-b", "68:9E:19:16:64:33", "--char-write-req", "-a", "0x002d", "-n", "ffff0000"])

