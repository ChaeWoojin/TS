def getLatLng(address):
    xypos = ""
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address
    rest_api_key = '7139c34ca29f68ba3740d0a0d7bd0ff7'
    header = {'Authorization': 'KakaoAK ' + rest_api_key}
    r = requests.get(url, headers=header)
    if r.status_code == 200:
        result_address = r.json()["documents"][0]["address"]
        xypos = result_address["y"], result_address["x"]
    else: xypos = "ERROR[" + str(r.status_code) + "]"
    return xypos

def reLatLng(addr): #이거 써서 위도 경도 받기
    adic = {'대전광역시 유성구 한우물로66번길 6 (대정동)': ('36.31134766285486', '127.33114732660894'), '대전광역시 유성구 자운로 90  (자운동)': ('36.399598', '127.349007'), 
            '대전광역시 유성구 자운로 90 (추목동)': ('36.40111397993467', '127.35364146882837')}
    if addr in adic:
        return adic[addr]
    else: 
        adre = {'대전광역시 유성구 자운로 90-0 (자운동)': '대전 유성구 자운동 97', '대전광역시 동구 산내로 1398-41 (대성동)': '대전 동구 대성동 295-1', 
                '대전광역시 동구  산내로 1317 (낭월동)': '대전광역시 동구 산내로 1317', '대전광역시 서구 계백로 1264-1264 (정림동)': '대전 서구 계백로 1264', 
                '대전광역시 유성구 관평2로 7 (관평동)': '대전 유성구 관평2로 7-7', '대전광역시 유성구 관들1길 63-63 (관평동)': '대전광역시 유성구 관들1길 63',
                '대전광역시 서구 둔산로 76-76 5층 (둔산동)': '대전광역시 서구 둔산로 76', '대전광역시 유성구 월드컵대로 275-39 (구암동)': '대전 유성구 월드컵대로275번길 39', 
                '대전광역시 동구 대전로 813 (정동)': '대전광역시 동구 대전로813번길 6', '대전광역시 동구 동부로 56 (판암동)': '대전 동구 동부로 56-8',
                '대전광역시 동구 옥천로176번길 4 (판암동)': '대전광역시 동구 판암동 323-4'}
        if addr in adre:
            addr = adre[addr]
        else:
            addr = addr.split(' ')
            addr = addr[0] + ' ' + addr[1] + ' ' + addr[2] + ' ' + addr[3]
        return getLatLng(addr)
