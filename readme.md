URL: tongtonginc.com


docker run --name tongtongwebsite -it -p 8009:3000 -v $(pwd):/app  tongtongincwebsite  
docker build -t tongtongincwebsite .
./CVSlogger.sh

---Required files---

Mapgen/ItemsToTrack.py , Mapgen/airpoditem.py

items = ["<Serialnumber1>","<Serialnumber2>"]
humanname = ["<Name1>","<Name2>"]
lineColor = "#597B98"
markerColor = "#97B2C8"


Cvslogger.sh
chmod 700 CVSlogger.sh

---To do---
- [ ] render farm
- [ ] one step further page
- [ ] suggestion tracker
- [ ] ptable
- [ ] citation generator
- [ ] calculator
- [ ] weather