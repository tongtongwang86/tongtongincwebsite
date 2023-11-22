# dependencies: pip3 install flask
from flask import Flask, request, send_file
import os
import tempfile
import subprocess
from path import *

app = Flask(__name__)

@app.route('/api/download-video', methods=['POST'])
def receive_text():
    data = request.json

    if 'download' in data:

        audioformatID = data["download"]["audioformatID"]
        videoformatID = data["download"]["videoformatID"]
        VideoID = data["download"]["VideoID"]

        
        command = f"cd {videoDirectory} && yt-dlp -f ba+bv -f {audioformatID}+{videoformatID} '{VideoID}'"
        
        print (command)
        
#        subprocess.run(f"cd {videoDirectory}",shell=True)

        fileName = subprocess.getoutput (f"yt-dlp --print filename -f ba+bv -f {audioformatID}+{videoformatID} '{VideoID}'")
        subprocess.run(command ,shell=True)
        
        fileDirectory = videoDirectory+"/"+fileName
        return send_file(fileDirectory, as_attachment=True, download_name=fileName)

    else:
        return {'error': 'Text field not found in request'}, 400

if __name__ == '__main__':
    app.run(host='192.168.124.15', port=5000, debug=True)
