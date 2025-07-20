from flask import Flask, jsonify, request
from colorlog import ColoredFormatter
from logging import StreamHandler, basicConfig, getLogger, INFO


getLogger('').handlers.clear()

basicConfig(level=INFO)
logger = getLogger('api2')

logger.handlers.clear()
logger.propagate = False

handler = StreamHandler()
formatter = ColoredFormatter(
    '%(log_color)s%(levelname)s:%(name)s:%(message)s',
    log_colors={
        'INFO': 'yellow',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    }
)
handler.setFormatter(formatter)
logger.handlers = [handler]

app = Flask(__name__)

@app.route('/api2', methods=['GET', 'POST'])
def api2():
    data = None
    if request.method == 'POST':
        data = request.json

    logger.info('API2: Received request from API1 %s' % (
        'with data: ' + str(data) if data else 'without data'
    ))

    return jsonify({'answer': 'Hello from make me happy' if not data else data.get('message')})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)