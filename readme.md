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
- [ ] revolute documentation
- [x] sync revolute
- [x] migrate mac onto server and fix track page
- [x] implement dolphin2.2
- [ ] render farm
- [ ] one step further page
- [x] youtube vid download ytdlp
- [x] modular backend script running
- [ ] suggestion tracker
- [x] ai??
- [ ] ptable
- [ ] citation generator
- [ ] calculator
- [x] json not syncing with ejs webpage without restarting bug
- [ ] weather
- [x] change log
- [ ] members
- [ ] members dashboard link to cloud
---done---
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
- [x] change log git commit sync
- [x] conic curves
- [x] Clicker
- [x] Cloud
- [x] migrate to server
- [x] documentation site
- [x] pcie bifurcation 
- [x] get hyper m.2 nvme card working with 2*4tb
- [x] forward into vm setup own cloud
- [x] pci passthrough
- [x] add ram to server
- [x] new server
- [x] static ip
