from pyorbital.orbital import Orbital
from datetime import datetime, timedelta
from pyorbital import tlefile

#ilename = "/data/samples_tles.master.txt"
now = datetime.now()
orb = Orbital("11U", "data/named_sample_tles_master.txt")
orb2 = Orbital("12U", "data/named_sample_tles_master.txt")

position = orb.get_position(now)
position2 = orb2.get_position(now)


print(position)


# asdf = orb.get_lonlatalt(now)
# for i in range(0,1000):
#     now += timedelta(seconds=4)
#     position = orb.get_position(now)
#     print("time : "+ str(i))
#     print(position)