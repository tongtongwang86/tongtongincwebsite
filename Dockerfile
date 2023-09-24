FROM nikolaik/python-nodejs:latest

RUN pip install eviltransform schedule pandas branca requests Jinja2 Numpy
RUN pip install build



# FROM node:20-slim
WORKDIR /app
# RUN pwd


COPY package.json /app
RUN npm install
RUN npm install houdinijs

RUN pip freeze > requirements.txt
# RUN pip freeze > requirements.txt


# RUN apt-get update || : && apt-get install python3.11 -y
# RUN apt install python3-pip -y


# RUN apt install python3-folium

COPY . /app

# RUN python3.11 -m build packages/folium

RUN cd packages/folium-package && python3.11 setup.py install

# RUN python3 packages/folium-package/setup.py bdist_wheel
# pip install /packages/folium-package/setup.py
# ENV PATH="${PATH}:/bin"
CMD [ "npm" , "start"]
