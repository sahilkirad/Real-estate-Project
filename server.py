from flask import Flask, request, jsonify
import util
app = Flask(__name__)
@app.route('/get_site_location_names',methods=['GET'])
def get_site_location_names():
    response = jsonify({
        'site_locations': util.get_site_location_names()
    })
    print(response.data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route('/predict_home_price',methods=['GET','POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    site_location=request.form['site_location']
    bhk=int(request.form['bhk'])
    bath=int(request.form['bath'])

    response =jsonify({
        'estimated_price':util.get_estimated_price(site_location,total_sqft,bhk,bath),
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
if __name__ == '__main__':
    print("starting python flask for Home Price Prediction")
    util.load_saved_artifacts()
    app.run()