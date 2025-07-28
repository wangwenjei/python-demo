import requests

URL = 'http://101.227.82.130:13002/WS/stream/outline'
Headers = {
    'Content-Type': 'application/json',
    # 'Content-Type': 'text/event-stream',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTczMDE4NzA1OSwianRpIjoiOTk3MTU2ZWItMWI2Yi00N2RjLWJmYzItODNjMWY5ZTI2M2U2IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImdvbGRlbnN0YW5kIiwibmJmIjoxNzMwMTg3MDU5LCJjc3JmIjoiMzE2NTVlYWUtZWVjYi00OTg1LTk0ZTAtYmJkYTQwODE4YmY2IiwiZXhwIjoyMDQ1NTQ3MDU5fQ.JKcnsCQCmBkN2TSbTjWy5Dd2xuPKy6jzai2QTI4hfHQ'
}
data = {
    "title": "血液透析:当血液循环遇到挑战时的救助之道",
    "keyword": "血液循环、血液透析"
}

res = requests.post(url=URL, headers=Headers, json=data)

print(res.text)
print(res.content)
