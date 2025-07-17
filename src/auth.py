import requests
import time
import nacl.encoding
import nacl.signing
import urllib.parse
import base64  # Thêm import base64

def get_dmarket_headers(public_key, private_key, method, endpoint, query_params="", body=""):
    timestamp = str(int(time.time()))
    sign_string = f"{method}{endpoint}{query_params}{body}{timestamp}"
    
    signing_key = nacl.signing.SigningKey(
        private_key[:64], encoder=nacl.encoding.HexEncoder
    )
    signature = signing_key.sign(sign_string.encode()).signature.hex()
    
    return {
        "X-Api-Key": public_key,
        "X-Sign-Date": timestamp,
        "X-Request-Sign": signature
    }

def get_skinport_headers(client_id, client_secret):
    encoded_data = f"{client_id}:{client_secret}".encode()
    auth_string = base64.b64encode(encoded_data).decode('utf-8')
    return {
        "Authorization": f"Basic {auth_string}",
        "Accept-Encoding": "br"
    }
