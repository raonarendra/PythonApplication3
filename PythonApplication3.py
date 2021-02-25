
import flask
from flask import request, jsonify


app = flask.Flask(__name__)

# Create some test data for our data monitoring at url "
car_data = [
    {'id': 0,
     'TIMESTAMP': '16:40:22',
     'DMS_FRAME_SETUP': 'xxxx-xxx-xxxx',
     'DROWSY_EYE_IDA': 'yyyy-yyyy-yyyy',
     'Eye_jda_drow_cofidence': 'zzz-zzz-zzz',
     'Drowsylstm': 'xy-xy-xy-xy'},
    {'id': 1,
     'TIMESTAMP': '16:44:33',
     'DMS_FRAME_SETUP': 'xxxx-xxx-xxxx',
     'DROWSY_EYE_IDA': 'yyyy-yyyy-yyyy',
     'Eye_jda_drow_cofidence': 'zzz-zzz-zzz',
     'Drowsylstm': 'xy-xy-xy-xy'},
     {'id': 2,
     'TIMESTAMP': '16:46:52',
     'DMS_FRAME_SETUP': 'xxxx-xxx-xxxx',
     'DROWSY_EYE_IDA': 'yyyy-yyyy-yyyy',
     'Eye_jda_drow_cofidence': 'zzz-zzz-zzz',
     'Drowsylstm': 'xy-xy-xy-xy'},
]


@app.route('/', methods=['GET'])
def home():
    return "<h1>Driver data monitoring</h1><p>This site is a prototype API for driver drowsiness monitoring via sample application.</p>"

# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/car_data/all', methods=['GET'])
def api_all():
    return jsonify(car_data)

@app.route('/api/v1/resources/car_data', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for car_d in car_data:
        if car_d['id'] == id:
            results.append(car_d)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

if __name__ == "__main__":
  app.run()

