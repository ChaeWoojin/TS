from urllib.parse import urlencode, unquote, quote_plus
import requests
from bs4 import BeautifulSoup as bs

key = "m9FjLDcj45iJhX56Y5Pe6cdBEyIemNLtD9n5%2BeBbopZjkQTlhKtXtqzikiGFBApfmU%2FCspdClYU6s1wDOc%2BsCw%3D%3D"
keyDecode = [unquote(key, 'UTF-8')]
params = ['ServiceKey', 'pageNo', 'numOfRows', 'sidoCd', 'sgguCd', 'emdongNm', 'yadmNm', 'zipCd', 'clCd', 'dgsbjtCd', 'xPos', 'yPos', 'radius']


def check_api(arr, target): #입력 변수 arr, 읽으려는 값 target
    arr = keyDecode + arr
    saved = []
    url = "http://apis.data.go.kr/B551182/hospInfoService1/getHospBasisList1"
    returnType = "xml"
    queryParams = '?' + urlencode({ quote_plus(params[i]) : arr[i] for i in range(13)})
    res = requests.get(url + queryParams)
    xml = res.text
    html = bs(xml, 'html.parser')
    for x in html.find_all(target): #읽으려는 값
        saved.append(x.text)
    return saved
