import flask


class EmergencyMessage(Exception):
  def __init__(self, response):
    self.response = response
    super().__init__(self.response)

def send_error(message, status = 400):
  return flask.jsonify({ "error": message }), status