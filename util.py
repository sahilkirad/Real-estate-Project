import json
import pickle
import numpy as np
__locations = None
__data_columns = None
__model = None

def get_estimated_price(site_location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(site_location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0],2)
def get_site_location_names():
    return __locations
def load_saved_artifacts():
    print("Loading saved artifacts....start")
    global __data_columns
    global __locations

    with open("./columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
    global __model
    with open("C:\\Users\\HP\\PyCharmMiscProject\\Pune house data.pickle",'rb') as f:
        __model = pickle.load(f)
    print("Loading saved artifacts..done")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_site_location_names())
    print(get_estimated_price('Camp',1000,3,4))
    print(get_estimated_price('Sadashiv Peth', 300, 2, 3))
    print(get_estimated_price('Baner', 500, 1, 2))