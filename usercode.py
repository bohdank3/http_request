import jwt 
from cryptography.hazmat.primitives 


def handle(data):
  payload_data = {
    "iat": 1670430472,
    "exp": 1671035272,
    "jti": "8TSuQqpkpAQC",
    "application_id": "7918e7f8-ed7b-4be1-aca7-9bb2422e3f92"
  }



  key = """-----BEGIN PRIVATE KEY-----
  MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCMcnz3BghQ5aQU
  qcVU6k5Ym2TJ2m9SjdeDRy/Svlp7Buel+22lzN/liqNt20qF/iXGCQEFAxx5hVKu
  IVcjOK2P0hNrZ1s23H4fR3wJT4XRqBlzUtMyqn9YvovzxEhQhOnEw7YfLVwK2tid
  2DVubLZTHwX0P/NOJ224TqR62RoL7XugCCLzMW4Th5Gd0KQLK9OfOQb7N/xoCM87
  vgH4ID6qTvPOGWwKNJlneOA7UTtYwWen5VLd14UIQPeqBuBXElMc5HABQkreXYeD
  dVxNBNubFlNw5bRmSvILZ+aQZZNYvG511kvhuLmgt7Ue1wKZG1/YFHVqar0k5iBz
  1KczVm+ZAgMBAAECggEAK9iiQsxTVE4dB4Zo4LW1d9wrfwj+sBswKP/UYkqjHL1v
  HFZ+SMDJNXQuyWEoxuQtDsJI2zO5dAa3ZT1rYseTB89h2KoPw/TaOxGqG44EDQwZ
  xfMZlDu+Pgpezt98ZAbapF8lQF582baw4bZaF/tAgHqy9Snx33hXvK5wkxmsFAS9
  pffBByNdT7Plm7DHJ4ySyFoyiyaEWcyuOsLqulK/VxvJcReqAt4TKSS5OEaxT01a
  AwCTwG44biz92Ieug5SFQgI8Fncs8kYRR1JVhEjfnEc2xxModhyG4AKAvAAN5Rhi
  Pn3MNlDR5So37OZ5kGbVZ5jHi3dm12PbcsI4qcJ4MQKBgQDA8w5PfchmmQftVdSK
  7fcsR29GrowR+wBbAZ9Fx4S4oDPdqvCS05bJO27JgydjDaLys5IlBXcOn3MQ2GGq
  x7a+jbhy2aeUiYcZ9wLr55Ia8QZfRKsjFKjy6AvU438stnQZ1wujEYDA7F4s8iCI
  s36qwD2DTaVrT8cMccw5ieQjIwKBgQC6V2zANCRBpaAoNxajcfEby4nz4g3eHCQh
  dAMjubkU5+IfvFhn+JrVvLtusVufqcc0iXz8SMMMTQJnEz2FGM3U1yYBwBzL7zNf
  0V6CVMCHpOwH0Db4Tbd0i8teUaaqPE3xvN7YaI3z7M2uhet/RCZE5zcAEqyRDzHC
  y8JRLzAcEwKBgChMm5iOtOR44eb4HkRGH3HoGZ2xpx+6RQC8/f8dBONq0mph4Y1J
  FB1DhIgiFH/jwTzftI527b7oHqhOCVgaDlkOUI/sVcv4TXdm1/1diG6IGMSdGwFg
  t0jEnnQAb/duxCEBgTS12yZwN9s7VwA2PSZ8sFxUQ1B+gRxgSD9cRYHxAoGADojz
  OqrWiShaLcjeQzGIFRrzT8q6OjEHwHREKm06Op87zC3s129U5IcsN54t/25G05pF
  3Yfvbu4y2cdubQtaQtflZw2NMXsfDsJOFOx3eB0tLA7ZutSVEso0us6zqWO60Lhi
  yY6eRACcqphXnj26nnVKnP7X5xjAUOmD5sE/h3ECgYAiQp6BZ4OFzPwH7OxQ4cxy
  b9aCgUDIsgSuU41+Alc0hZ+09rC0yfv80fCZg2la74BE2rc5H+qvPKYaGpH8y5NN
  3LAhklDi+kN6P2wAapb72SxlMAXygcrGQQFWY1Fh00GXUqH/HNG/UiQoniRaeptd
  AuBeDNVlpyPEMtfocNoPxA==
  -----END PRIVATE KEY-----
  """

  token = jwt.encode(
      payload=payload_data,
      key=key,
      algorithm='HS256'
  )

  data["token"] = token
  return data
