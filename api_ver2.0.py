from urllib.parse import urlencode, unquote, quote_plus 
import requests 
from bs4 import BeautifulSoup as bs 

class Api:
    
    def __init__(self, arr):
        self.value = []
        self.pageNow = 0
        self.pageTotal = 0
        self.key = "m9FjLDcj45iJhX56Y5Pe6cdBEyIemNLtD9n5%2BeBbopZjkQTlhKtXtqzikiGFBApfmU%2FCspdClYU6s1wDOc%2BsCw%3D%3D" 
        self.keyDecode = [unquote(self.key, 'UTF-8')]
        self.array = self.keyDecode + arr
        self.params = ['ServiceKey', 'pageNo', 'numOfRows', 'sidoCd', 'sgguCd', 'emdongNm', 'yadmNm', 'zipCd', 'clCd', 'dgsbjtCd', 'xPos', 'yPos', 'radius'] 
        self.url = "http://apis.data.go.kr/B551182/hospInfoService1/getHospBasisList1"
        self.queryParams = '?' + urlencode({ quote_plus(self.params[i]) : self.array[i] for i in range(13)})
        self.res = requests.get(self.url + self.queryParams)
        self.xml = self.res.text
        self.html = bs(self.xml, 'html.parser')   
        
    def target(self, target): #입력 변수 arr, 읽으려는 값 target 
        for x in self.html.find_all(target): self.value.append(x.text) 
            
    def page(self):
        for x in self.html.find_all('pageno'): self.pageNow = x.text
        for x in self.html.find_all('totalcount'): self.pageTotal = int(x.text)
        for x in self.html.find_all('numofrows'): self.pageTotal = (self.pageTotal + int(x.text) - 1) // int(x.text)

arr1 = ['1', '3000', '250000', '', '', '', '', '', '', '', '', ''] #대전 병원 2305개
api1 = Api(arr1)
api1.target('yadmnm')
api1.page()

#여기까지 API 사용법
#여기부터 실제 활용

hospitals = api1.value
hosSubject = {}
hosSubjectName = {}
for x in hospitals:
    hosSubject[x] = []
    hosSubjectName[x] = []

subject = {'00': '일반의', '01': '내과', '02': '신경과', '03': '정신건강의학과', '04': '외과', '05': '정형외과', '06': '신경외과', '07': '흉부외과', '08': '성형외과', '09': '마취통증의학과', '10': '산부인과', '11': '소아청소년과', '12': '안과', '13': '이비인후과', '14': '피부과', '15': '비뇨의학과', '16': '영상의학과', '17': '방사선종양학과', '18': '병리과', '19': '진단검사의학과', '20': '결핵과', '21': '재활의학과', '22': '핵의학과', '23': '가정의학과', '24': '응급의학과', '25': '직업환경의학과', '26': '예방의학과', '50': '구강악안면외과', '51': '치과보철과', '52': '치과교정과', '53': '소아치과', '54': '치주과', '55': '치과보존과', '56': '구강내과', '57': '영상치의학과', '58': '구강병리과', '59': '예방치과', '61': '통합치의학과', '80': '한방내과', '81': '한방부인과', '82': '한방소아과', '83': '한방안이비인후피부과', '84': '한방신경정신과', '85': '침구과', '86': '한방재활의학과', '87': '사상체질과', '88': '한방응급'}
for x in subject.keys():
    arr = ['1', '3000', '250000', '', '', '', '', '', x, '', '', '']
    api = Api(arr)
    api.target('yadmnm')
    for y in api.value:
        hosSubject[y].append(x)
        hosSubjectName[y].append(subject[x])
        
import pandas as pd
excel = pd.DataFrame.from_dict(hosSubjectName, orient = 'index')
excel.to_excel('/content/gdrive/MyDrive/KAIST/TS222/HospitalSubject.xlsx')

hospitalName = pd.DataFrame(hospitals)
hospitalName.to_excel('/content/gdrive/MyDrive/KAIST/TS222/HospitalName.xlsx')
