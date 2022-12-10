import jwt

def handle(data):
    encoded_jwt = = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
    print(encoded_jwt)
    return data

