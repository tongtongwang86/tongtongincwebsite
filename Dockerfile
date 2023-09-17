FROM nikolaik/python-nodejs:latest

RUN pip install folium eviltransform schedule pandas

# FROM node:20-slim
WORKDIR /app
COPY package.json /app
RUN npm install
# RUN apt-get update || : && apt-get install python3.11 -y
# RUN apt install python3-pip -y


# RUN apt install python3-folium




COPY . /app
# ENV PATH="${PATH}:/bin"
CMD [ "npm" , "start"]
