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
- [x] Add last refresh time on website
- [x] improve website aesthetics
- [x] combine all 3 scripts into one
- [x] add time range limit for data points so there is only n amount of point on screen at once
- [x] add layer select for multiple maps
- [x] zoom to fit
- [x] add map layers for airpods
- [x] git ignore csv, data ,itemtotrack
- [x] plot csv values only when there is change 
- [x] fix index.html
- [x] dockerize
- [x] iphone15 status page
- [x] calendar page
- [x] about page
- [x] company logo top left
- [ ] one step further page
- [x] change log git commit sync
- [x] conic curves
- [x] Clicker
- [x] Cloud
- [ ] render farm
- [ ] youtube vid download
- [ ] add storage to mac
- [ ] modular backend script running
- [ ] suggestion tracker
- [ ] ai??
- [ ] ptable
- [ ] citation generator
- [ ] calculator
- [ ] weather
- [ ] new server
	-[ ] static ip
- [ ] change log
- [ ] members
- [ ] members dashboard link to cloud
