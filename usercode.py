import jwt
def handle(data):
   

    payload_data = {
      "iat": data["now"],
      "exp": data["future"],
      "jti": data["jti"],
      "application_id": data["application_id"]
	 }


    key = data["key"]
    token = jwt.encode(
      payload=payload_data,
      key=key,
      algorithm='HS256'
    )
   
    data["hello"] = "Hello world!"
    data["token"] = token
    return data
