import os, sys
from flask import Flask,request
app = Flask(__name__)
ACCESS_TOKEN = "EAAJiQQDXZByIBAD23YNcxK0klSDkxKQ35molXfyXEcyZAvSojgsowzNAw2gAnrIsD54B5wIMWo2kTC0I1XlEY3iAuMA5RG3LAW1gZBhFcq43mq0ufUPiwx0oXf8syw92RLgNW2H9E5grVKKuQu83knnvgMIc1iBlYTt6WmRWwZDZD"
VERIFY_TOKEN = "hello"

@app.route('/', methods=['GET'])
def verify():
    # webhook verification
    if request.args.get('hub.mode') == 'subscribe' and request.args.get('hub.challenge'):
        if request.args.get('hub.verify_token') == VERIFY_TOKEN:
            return 'Verification token missmatch', 403
        return request.args['hub.challenge'], 200
    return 'Hello World', 200

if __name__ == '__main__':
    app.run(debug = False) 
