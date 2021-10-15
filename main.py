# from flask import Flask
# from flask_socketio import SocketIO

# app = Flask(__name__)
# socketio = SocketIO(app)

# @app.route('/')
# def index():
#   return "Hello world"

# @socketio.on("stream")
# def my_event(message):
#   print("*" * 100, message)

# if __name__ == '__main__':
#   socketio.run(app)

from PIL import Image
from io import BytesIO
from flask.templating import render_template
from flask_socketio import SocketIO
from flask import Flask

import base64
import cv2 as cv
import numpy as np

CASCADE_PATH = "cascades"
PAGES_PATH = "pages"

app = Flask(__name__, template_folder=PAGES_PATH)
socketio = SocketIO(app, cors_allowed_origins='*')

socket_trigger = 0

face_cascade_name = f'{CASCADE_PATH}/haarcascade_frontalface_alt.xml'
eyes_cascade_name = f'{CASCADE_PATH}/haarcascade_eye.xml'

face_cascade = cv.CascadeClassifier()
eyes_cascade = cv.CascadeClassifier()
#-- 1. Load the cascades
if not face_cascade.load(cv.samples.findFile(face_cascade_name)):
  print('--(!)Error loading face cascade')
  exit(0)
if not eyes_cascade.load(cv.samples.findFile(eyes_cascade_name)):
  print('--(!)Error loading eyes cascade')
  exit(0)

@app.route('/stream')
def stream(): 
  return render_template('stream.html')

@app.route('/view')
def view(): 
  return render_template('view.html')

@socketio.on('stream')
def on_message(data):
  global socket_trigger
  session_flag = socket_trigger

  header, data = data.split(',', 1)
  img = base64.b64decode(data)
  img = Image.open(BytesIO(img))

  img = np.asarray(img)
  img = detectAndDisplay(img)

  img = Image.fromarray(img)
  buffered = BytesIO()
  img.save(buffered, format="JPEG")
  img = base64.b64encode(buffered.getvalue())
  img = img.decode("UTF-8")
  img = header + "," + img

  if session_flag < socket_trigger:
    print("Frame lost")
    return

  socket_trigger += 1
  socketio.emit('stream-python', img)

def detectAndDisplay(frame):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)
    #-- Detect faces
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x,y,w,h) in faces:
        center = (x + w//2, y + h//2)
        frame = cv.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
        faceROI = frame_gray[y:y+h,x:x+w]
        #-- In each face, detect eyes
        eyes = eyes_cascade.detectMultiScale(faceROI)
        for (x2,y2,w2,h2) in eyes:
            eye_center = (x + x2 + w2//2, y + y2 + h2//2)
            radius = int(round((w2 + h2)*0.25))
            frame = cv.circle(frame, eye_center, radius, (255, 0, 0 ), 4)
    return frame

if __name__ == '__main__':
  socketio.run(app, debug = True, port=5000)