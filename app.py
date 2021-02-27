from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import requests
import json
from os import getenv
from random import randint
app = Flask(__name__)
api = Api(app)
#
# locations_collected = []
#
#
# def ipstack(request_ipv4='check'):
#
#     if request_ipv4:
#         access_key = getenv('ipstackKey')
#         base_url = f'http://api.ipstack.com/{request_ipv4}?access_key={
#         access_key}'
#         check = requests.get(base_url)
#         locations_collected.append(check)
#
#     return locations_collected

class Testsettin(Resource):

    test_set = ['250.10.247.40',
                '58.146.87.212',
                '0.242.187.128',
                '189.147.147.15',
                '50.152.25.31',
                '74.135.229.139',
                '223.180.89.79',
                '149.154.86.1',
                '76.0.198.12',
                '179.111.92.213',
                '251.219.146.9',
                '146.150.225.180',
                '43.30.40.132',
                '88.230.139.194',
                '219.143.81.80'
                ]

    second_set = [
            "241.28.103.93",
            "161.47.118.200",
            "73.98.2.50",
            "220.0.28.104",
            "39.165.71.101",
            "164.189.52.190",
            "206.80.10.154",
            "3.131.56.210",
            "155.22.16.173",
            "32.1.213.113",
        ]

    def get(self):
        return self.second_set[randint(1,10)]



parser = reqparse.RequestParser()

LOCATION = {
        "continent_name": "Europe",
        "country_code": "PL",
        "country_name": "Poland",
        "region_code": "MZ",
        "region_name": "Mazovia",
        "city": "\u015ar\u00f3dmie\u015bcie",
    }

LOC = []


class Geolocation(Resource):

    def get(self):
        data0 = LOC
        data = DATA.json()
        # data1 = LOCATION
        # data2 = LOC.fromkeys(data)
        # data3 = LOC.extend(data)
        data0.append(data)
        return data

    def post(self):
        parser.add_argument("continent_name")
        parser.add_argument("country_code")
        parser.add_argument("country_name")
        parser.add_argument("region_code")
        parser.add_argument("region_name")
        parser.add_argument("city")
        args = parser.parse_args()

        arg_id = int(max(LOCATION.keys())) + 1
        arg_id = '%i' % arg_id
        LOCATION[arg_id] = {
            "region_code": args["region_code"],
            "region_name": args["region_name"],
            "city": args["city"],
            }

        return LOCATION[arg_id], 201


api.add_resource(Geolocation, '/loc/')
api.add_resource(Testsettin, '/tes/')

if __name__ == '__main__':
    app.run(debug=True)
