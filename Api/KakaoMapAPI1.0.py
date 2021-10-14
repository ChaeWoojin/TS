import requests
 
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
 
def getKakaoMapHtml(width, height, addr):
    javascript_key = "120fd46cf1eef74e1428294a7a6e4a06"
    address = getLatLng(addr)
    html = "\
<div id='map' style='width:" + str(width) + "px;height:" + str(height) + "px;display:inline-block;'></div>\n\
<script type='text/javascript' src='//dapi.kakao.com/v2/maps/sdk.js?appkey=" + javascript_key + "'></script>\n\
<script>\n\
var container = document.getElementById('map'), \n\
\toptions = {\n\
\t\tcenter: new kakao.maps.LatLng(" + address[0] + ", " + address[1] + "),\n\
\t\tlevel: 3\n\
\t};\n\
var map = new kakao.maps.Map(container, options);\n\
</script>\n"
    
    return html

def getKakaoSelfMarkHtml(width, height, addr):
    javascript_key = "120fd46cf1eef74e1428294a7a6e4a06"
    address = getLatLng(addr)
    html = "\
<div id='map' style='width:" + str(width) + "px;height:" + str(height) + "px;display:inline-block;'></div>\n\
<script type='text/javascript' src='//dapi.kakao.com/v2/maps/sdk.js?appkey=" + javascript_key + "'></script>\n\
<script>\n\
var container = document.getElementById('map'), \n\
\toptions = {\n\
\t\tcenter: new kakao.maps.LatLng(" + address[0] + ", " + address[1] + "),\n\
\t\tlevel: 3\n\
\t};\n\
var map = new kakao.maps.Map(container, options);\n\
var markerPosition = new kakao.maps.LatLng(" + address[0] + ", " + address[1] + ");\n\
var marker = new kakao.maps.Marker({\n\
\tposition: markerPosition\n\
});\n\
marker.setMap(map);\n\
</script>\n"
    
    return html
