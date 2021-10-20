from .type_translation import types_values
from .flask_helpers import EmergencyMessage, send_error

from imageai.Detection import ObjectDetection # Object detection library

import os

MODELS_PATH = "detector_models"

# Model
detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(os.getcwd(), MODELS_PATH, "yolo.h5"))
detector.loadModel()

def recognize_objects(frame, objects=None):
  objects = list(set(objects) & set(types_values())) if type(objects) is list else []
  if len(objects) == 0: raise EmergencyMessage(send_error("There must be at least one allowed object"))

  objects = { entity: True for entity in objects }
  custom_objects = detector.CustomObjects(**objects)

  return detector.detectObjectsFromImage(
    input_image=frame,
    input_type="array",
    output_type="array",
    minimum_percentage_probability=30,
    custom_objects=custom_objects
  )[0]