import pytest
import requests  
import json

def get(n):
    val = requests.get(f'http://127.0.0.1:8888?n={n}').text
    print(val)
    return json.loads(val).get('result')

def test_1():
    assert get(4) == 3

def test_2():
    assert get(8) == 21

def test_3():
    assert get(15) == 610