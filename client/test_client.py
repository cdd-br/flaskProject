import requests
import json

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "api/v1/connect/testeIfaceGui")

print(response.headers)

print(response.json())

ans = response.json()['status']

ans1 = 'OK'
print(ans)

def test_conectividade():
    assert 200 == ans

def test_ping():
    assert 'OK' == ans1

def test_almir():
    assert 'OK' == ans1