# Example of an ToDo App based on FastAPI

To install the requirements run
```
python3 -m pip install -r requirements.txt
```

To run the server execute
```
python3 src/main.py
```

Afterwards the following things are available
- Server is available at http://127.0.0.1:8000
- Documentation at http://127.0.0.1:8000/docs
- Openapi specification available at http://127.0.0.1:8000/openapi.json

To create a user execute

```
python3 src/create_user.py
```

## HTTP Protocol
The project uses uvicorn as a ASGI web server. Please note that this server only supports HTTP 1.1.
To use higher versions like HTTP 2 / 3 consider the usage of hypercorn
To configure it please consult: https://pgjones.gitlab.io/hypercorn/how_to_guides/configuring.html. 
To enable the usage of HTTP/2 you can provide a certificate.  On your local machine you can generate a self-signed certificate:

```
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
```