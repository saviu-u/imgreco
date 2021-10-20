# Image treatment and encoding
from PIL import Image
from io import BytesIO
from base64 import b64encode, b64decode
import numpy as np

from .flask_helpers import EmergencyMessage, send_error

def base64ToNmpArray(data):
  try:
    header, data = data.split(',', 1)
    img = b64decode(data)
    img = Image.open(BytesIO(img))

    img = np.asarray(img)
    return (header, img)
  except:
    raise EmergencyMessage(send_error("\"Frame\" was not a valid base64 message"))

def NmpArrayToBase64(header, array):
  try:
    img = Image.fromarray(array)
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img = b64encode(buffered.getvalue())
    img = img.decode("UTF-8")
    img = header + "," + img
    return img
  except:
    raise EmergencyMessage(send_error("Internal error on converting result to base64, contact the admin", 500))