# simple-auth-proxy

**Description**

A simple authentication proxy to work in conjunction with FIWARE Identity Manager (KeyRock). It's work fine with most of json REST APIs, but requires some improvements to do complex tasks like upload and download files.

**Instructions**

The simple-auth-proxy needs `python3`, `pip`, `virtualenv` and `make` alredy installed to build and execute it.

To build the simple-auth-proxy, do the following steps on Linux terminal:

  ```
  $ cd /path/to/simple-auth-proxy
  $ python3 -m venv venv
  $ source venv/bin/activate
  $ python3 -m pip install -r requirements.txt
  $ cp config-template.py config.py
  ```

Inform the `config['idm_app_id']` on `config.py` file.

To execute the simple-auth-proxy, write the following command on terminal:

  ```
  $ make run
  ```

In production, use the Gunicorn as follows:

  ```
  $ /path/to/simple-auth-proxy/venv/bin/gunicorn -b 0.0.0.0:5000 app:app
  ```

To run in production with HTTPS protocol, use Gunicorn as follows:

  ```
  $ /path/to/simple-auth-proxy/venv/bin/gunicorn --certfile=certfile.crt –key=keyfile.key -b 0.0.0.0:443 app:app
  ```

If you are using the simple-auth-proxy to proxy the FIWARE Orion, you can test it with the following command:

  ```
  $ curl -H "Authorization: Bearer <access_token>" -X GET http://localhost:5000/v2
  ```


