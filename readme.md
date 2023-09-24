docker run --name tongtongwebsite -it -p 8009:3000 -v $(pwd):/app  tongtongincwebsite  
docker build -t tongtongincwebsite .

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