from django.shortcuts import render
##공공데이터포탈
from .hospitaldatas import Api, Hospital
##카카오맵
from .kakaoMapApi import getKakaoMapHtml, getKakaoMarkersHtml, getKakaoSelfMarkHtml, getLatLng, reLatLng
##로마자 번역
from hangul_romanize import Transliter
from hangul_romanize.rule import academic
# Create your views here.

def test(request):
    return render(request, 'hospot/test.html')

def main(request):
    return render(request, 'hospot/cover.html')

def index(request):
    department_list=[]
    with open('./hospot/memory', 'r', encoding="utf-8") as f:
        list=f.readlines()
        for i in range(3,len(list)):
            if i==len(list)-1:
                typename=" ".join(list[i].split(' ')[1:])
                department_list.append(typename)
            else:
                typenamelist=list[i].split(' ')[1:]
                typename=" ".join(typenamelist)
                department_list.append(typename)
    context={'department_list': department_list}
    return render(request, 'hospot/department_type.html', context)

def department(request, department_id):
    list=['1', '10', '250000', '', '', '', '', '', '', '', '', '']
    num=department_id
    if (department_id in range(27)):
        pass
    elif(department_id in range (27, 37)):
        num+=23
    elif (department_id == 37):
        num+=24
    else:
        num+=42
    list[9]=str(num)
    hospital_list = Api(list)
    hospital_list.target('yadmnm')
    names=hospital_list.value
    profiles=[]
    transliter = Transliter(academic)
    addrs=[]

    for name in names:
        romanname = transliter.translit(name).replace("-", "")
        list[5]=str(name)
        hospital_profile=Api(list)
        hospital_profile.target('addr')
        addr=" ".join(hospital_profile.value)
        romanaddr = transliter.translit(addr).replace("-", "")
        hospital_profile.target('telno')
        telno="".join(hospital_profile.value)
        hospital_profile.target('hospurl')
        url="".join(hospital_profile.value)
        xypos=reLatLng(addr)
        hosprofile=Hospital(name, romanname, addr, telno, url, xypos[0], xypos[1])
        profiles.append(hosprofile)
        addrs.append(reLatLng(addr))
    addrs=tuple(addrs)
    context = {'profiles': profiles, addrs: addrs}
    return render(request, 'hospot/department_list.html', context)


def size(request, department_id, hospital_size):
    html = 'hospot/' + str(department_id) + '/base.html'
    return render(request, html)


def profile(request, department_id, hospital_size, code_id):
    hospital_list = Api(['1', '3000', '250000', '', '', '', '', '', '', '', '', ''])
    hospital_list[7] = str(code_id)  ##병원 등급
    hospital_list[8] = str(department_id)  ##병원 분과 종류
    context = {'hospital_list': hospital_list}
    html = 'hospot/' + str(department_id) + '/' + str(code_id) + '.html'
    return render(request, html)

