import requests
import time
import xml.etree.ElementTree as et

def main():
    local = time.localtime(time.time()) # 2시간 전 데이터 받아옴

    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
    params ={'serviceKey' : 'loGEsi8RLLPDoscN/+N/FQs4Gck/La0uzw51zooTczK3aWcmK6mvoHJ8tfF1uCtnKl2OdfmXYnz1QtEauhwWPA==', 'pageNo' : '1', 'numOfRows' : '1000', 'dataType' : 'XML', 'base_date' : str(local.tm_year).zfill(2)+str(local.tm_mon).zfill(2)+str(local.tm_mday).zfill(2), 'base_time' : str(local.tm_hour).zfill(2)+str(local.tm_min).zfill(2), 'nx' : '61', 'ny' : '126' }

    response = requests.get(url, params=params)
    text = response.text
    fname = str(local.tm_year).zfill(2)+str(local.tm_mon).zfill(2)+str(local.tm_mday).zfill(2)+str(local.tm_hour).zfill(2)+str(local.tm_min).zfill(2)
    f = open("xmls/"+"report"+".xml", 'w', encoding='UTF-8')
    f.write(text)
    f.close()

    file = et.parse("xmls/"+"report"+".xml")
    root = file.getroot()

    data = root[1][1]

    result = open("result.txt", 'w', encoding='UTF-8')

    print()
    for child in data:
        for value in child:
            print(value.tag, value.text)
            result.write(value.tag+' '+value.text+"\n")
        print()
        result.write("\n")


if __name__ == '__main__':
    main()