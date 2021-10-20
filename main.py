# BackEnd tools
from flask.templating import render_template
from flask import jsonify, Flask, request

from lib.type_translation import TYPES # Helper for translating type keys
from lib.flask_helpers import * # Helper for returning messages instantly
from lib.base64_helpers import base64ToNmpArray, NmpArrayToBase64 # Helper for converting base64 packages
from lib.detection_helpers import recognize_objects # Helper for recognizing object

PAGES_PATH = "pages"

app = Flask(__name__, template_folder=PAGES_PATH)

@app.route('/stream')
def stream(): 
  return render_template('stream.html')

@app.route('/view')
def view(): 
  return render_template('view.html')

@app.route('/types')
def types():
  return jsonify(TYPES)

@app.before_request
def valid_post_requests():
  if request.method != "POST": return
  if not request.is_json: return send_error("Request wasn't a valid JSON")

@app.route('/retrieve', methods=['POST'])
def retrieve():
  try:
    data = request.get_json()

    frame = data.get('frame')
    if frame is None: return send_error("\"Frame\" key must be specified")

    header, img_array = base64ToNmpArray(frame)
    img_array = recognize_objects(img_array, data.get('allowed_objects'))

    return jsonify({ "result": NmpArrayToBase64(header, img_array) }), 200
  except EmergencyMessage as e:
    return e.response

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)