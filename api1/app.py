import requests
from flask import Flask, jsonify, request
from colorlog import ColoredFormatter
from logging import StreamHandler, basicConfig, getLogger, INFO


getLogger('').handlers.clear()

basicConfig(level=INFO)
logger = getLogger('api1')

logger.handlers.clear()
logger.propagate = False

handler = StreamHandler()
formatter = ColoredFormatter(
    '%(log_color)s%(levelname)s:%(name)s:%(message)s',
    log_colors={
        'INFO': 'blue',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    }
)
handler.setFormatter(formatter)
logger.handlers = [handler]


app = Flask(__name__)

@app.route('/api1', methods=['GET', 'POST'])
def api1():
    data = None
    if request.method == 'POST':
        data = request.json

    logger.info('API1: Received request from User %s' % (
        'with data: ' + str(data) if data else 'without data'
    ))

    target_url = 'http://api2:5001/api2'

    if data:
        response = requests.post(target_url, json=data)
    else:
        response = requests.get(target_url)

    logger.info('API1: Got response from API2: %s' % response.text)

    return jsonify({'answer': response.json().get('answer')})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)