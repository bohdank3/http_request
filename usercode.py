
def handle(data):
    import jwt
    data["hello"] = "Hello world!"
    return data
