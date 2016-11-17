import os
import json
import time
import datetime
from flask import send_from_directory
from flask import request, Blueprint
#from elasticsearch import Elasticsearch

import requests
import ast
# app.config.from_object(os.environ['APP_SETTINGS'])

api = Blueprint('APIs', __name__)

@api.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@api.route('/')
def hello():
    return "Hello World!"

@api.route('/<analytics>',methods= ['GET','POST'])
def fetch_analytics(analytics):
        data = request.data
    	fetch_data = analytics
    	data_list = fetch_data.split(",")
    	data_dict = {}
        today = str(datetime.date.today())
    	data_dict["STUDENT_ID"] = data_list[0]
    	data_dict["LAB_ID"] = data_list[1]
        data_dict["LAB_NAME"] = data_list[2]
        #data_dict["EXPERIMENT_NAME"] = data_list[3] + "-" + data_list[2]
        #data_dict["EXPERIMENT_ID"] = data_list[4]
        data_dict["EXPERIMENT_ID"] = data_list[3]
        data_dict["EXPERIMENT_NAME"] = data_list[4]
        data_dict["DATE_OF_EXPERIMENT"] = today
        data_dict["TIME_OF_EXPERIMENT"] = time.strftime("%H:%M")
        data_dict["IP_ADDRESS"] = request.environ.get('HTTP_X_REAL_IP',request.remote_addr)

        res = requests.get("http://freegeoip.net/json/" + data_dict["IP_ADDRESS"])
        data = res.text
        ip_dir = ast.literal_eval(data)
        data_dict["REGION"] = ip_dir["region_name"]
        #print type(ip_dir)
        #print ip_dir

    	json_data = json.dumps(data_dict)
        try:
                pass
    		es = Elasticsearch([{'host':'some-server.domain', 'port':some-port}])
    		es.index(index="some-indexx", doc_type="some-doc-type", body=data_dict)
        except Exception as e:
                print e


        return "Hello {}!".format(analytics)
