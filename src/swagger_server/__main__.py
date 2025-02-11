#!/usr/bin/env python3

from connexion import FlaskApp
from swagger_server import encoder
import uvicorn


app = FlaskApp(__name__, specification_dir='./swagger/')
if __name__ == '__main__':

    app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': '5GMETA License API'}, pythonic_params=True)
    config = uvicorn.Config("__main__:app", host='0.0.0.0', port=5000, log_level="info")
    server = uvicorn.Server(config)
    server.run()
