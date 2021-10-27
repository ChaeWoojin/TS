from django.test import TestCase
from hangul_romanize import Transliter
from hangul_romanize.rule import academic
from mysite.hospot.hospitaldatas import Api, Hospital
from mysite.hospot.kakaoMapApi import getKakaoMapHtml, getKakaoSelfMarkHtml
# Create your tests here.


list = ['1', '10', '250000', '', '', '', '', '', '', '', '', '', '']
num = 0
list[9] = str(num)
hospital_list = Api(list)
hospital_list.target('yadmnm')
names = hospital_list.value
profiles = []
transliter = Transliter(academic)

for name in names:
    profile=[]
    RomanName = transliter.translit(name).replace("-", "")
    list[5] = str(name)
    hospital_profile = Api(list)
    hospital_profile.target('addr')
    addr = " ".join(hospital_profile.value)
    hospital_profile.target('telno')
    telno = "".join(hospital_profile.value)
    hospital_profile.target('hospUrl')
    url = "".join(hospital_profile.value)
    hospital_profile.target('xpos')
    xpos = "".join(hospital_profile.value)
    hospital_profile.target('ypos')
    ypos = "".join(hospital_profile.value)
    hosprofile = Hospital(name, addr, telno, url, xpos, ypos)
    profile.append(name)
    profile.append(addr)
    profile.append(telno)
    profile.append(url)
    profile.append(xpos)
    profile.append(ypos)
    profiles.append(profile)

for profile in profiles:
    print(profile.addr)