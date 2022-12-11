import jwt
def handle(data):
   

    payload_data = {
      "iat": 1670430472,
      "exp": 1671035272,
      "jti": "8TSuQqpkpAQC",
      "application_id": "7918e7f8-ed7b-4be1-aca7-9bb2422e3f92"
	 }


    key = """-----BEGIN PRIVATE KEY-----
    MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCMcnz3BghQ5aQUqcVU6k5Ym2TJ2m9SjdeDRy/Svlp7Buel+22lzN/liqNt20qF/iXGCQEFAxx5hVKuIVcjOK2P0hNrZ1s23H4fR3wJT4XRqBlzUtMyqn9YvovzxEhQhOnEw7YfLVwK2tid2DVubLZTHwX0P/NOJ224TqR62RoL7XugCCLzMW4Th5Gd0KQLK9OfOQb7N/xoCM87vgH4ID6qTvPOGWwKNJlneOA7UTtYwWen5VLd14UIQPeqBuBXElMc5HABQkreXYeDdVxNBNubFlNw5bRmSvILZ+aQZZNYvG511kvhuLmgt7Ue1wKZG1/YFHVqar0k5iBz1KczVm+ZAgMBAAECggEAK9iiQsxTVE4dB4Zo4LW1d9wrfwj+sBswKP/UYkqjHL1vHFZ+SMDJNXQuyWEoxuQtDsJI2zO5dAa3ZT1rYseTB89h2KoPw/TaOxGqG44EDQwZxfMZlDu+Pgpezt98ZAbapF8lQF582baw4bZaF/tAgHqy9Snx33hXvK5wkxmsFAS9pffBByNdT7Plm7DHJ4ySyFoyiyaEWcyuOsLqulK/VxvJcReqAt4TKSS5OEaxT01aAwCTwG44biz92Ieug5SFQgI8Fncs8kYRR1JVhEjfnEc2xxModhyG4AKAvAAN5RhiPn3MNlDR5So37OZ5kGbVZ5jHi3dm12PbcsI4qcJ4MQKBgQDA8w5PfchmmQftVdSK7fcsR29GrowR+wBbAZ9Fx4S4oDPdqvCS05bJO27JgydjDaLys5IlBXcOn3MQ2GGqx7a+jbhy2aeUiYcZ9wLr55Ia8QZfRKsjFKjy6AvU438stnQZ1wujEYDA7F4s8iCIs36qwD2DTaVrT8cMccw5ieQjIwKBgQC6V2zANCRBpaAoNxajcfEby4nz4g3eHCQhdAMjubkU5+IfvFhn+JrVvLtusVufqcc0iXz8SMMMTQJnEz2FGM3U1yYBwBzL7zNf0V6CVMCHpOwH0Db4Tbd0i8teUaaqPE3xvN7YaI3z7M2uhet/RCZE5zcAEqyRDzHCy8JRLzAcEwKBgChMm5iOtOR44eb4HkRGH3HoGZ2xpx+6RQC8/f8dBONq0mph4Y1JFB1DhIgiFH/jwTzftI527b7oHqhOCVgaDlkOUI/sVcv4TXdm1/1diG6IGMSdGwFgt0jEnnQAb/duxCEBgTS12yZwN9s7VwA2PSZ8sFxUQ1B+gRxgSD9cRYHxAoGADojzOqrWiShaLcjeQzGIFRrzT8q6OjEHwHREKm06Op87zC3s129U5IcsN54t/25G05pF3Yfvbu4y2cdubQtaQtflZw2NMXsfDsJOFOx3eB0tLA7ZutSVEso0us6zqWO60LhiyY6eRACcqphXnj26nnVKnP7X5xjAUOmD5sE/h3ECgYAiQp6BZ4OFzPwH7OxQ4cxyb9aCgUDIsgSuU41+Alc0hZ+09rC0yfv80fCZg2la74BE2rc5H+qvPKYaGpH8y5NN3LAhklDi+kN6P2wAapb72SxlMAXygcrGQQFWY1Fh00GXUqH/HNG/UiQoniRaeptdAuBeDNVlpyPEMtfocNoPxA==
    -----END PRIVATE KEY-----"""
    token = jwt.encode(
      payload=payload_data,
      key=key,
      algorithm='HS256'
    )
   
    data["hello"] = "Hello world!"
    data["token"] = token
    return data
