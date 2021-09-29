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
        self.value = []
        for x in self.html.find_all(target): self.value.append(x.text) 
    
    def item(self, param): #읽을 값들 list로 받음
        self.value = []
        for x in self.html.find_all('item'):
          temp = {}
          for y in param:
            for z in x.find_all(y):
              temp[y] = z.text
            if y not in temp.keys():
              temp[y] = None
          self.value.append(temp)
        
    def page(self):
        for x in self.html.find_all('pageno'): self.pageNow = x.text
        for x in self.html.find_all('totalcount'): self.pageTotal = int(x.text)
        for x in self.html.find_all('numofrows'): self.pageTotal = (self.pageTotal + int(x.text) - 1) // int(x.text)
