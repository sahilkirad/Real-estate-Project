from flask import Flask, request, jsonify
import util
app = Flask(__name__)
@app.route('/get_site_location_names')
def get_site_location_names():
    response = jsonify({
        'site_locations': util.get_site_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run()
