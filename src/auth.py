import requests
import time
import nacl.encoding
import nacl.signing
import urllib.parse

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

def get_skinport_token(client_id, client_secret):
    url = "https://api.skinport.com/v1/auth"
    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials"
    }
    response = requests.post(url, data=data)
    response.raise_for_status()
    return response.json().get("access_token")