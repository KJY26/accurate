import requests
import time
import xml.etree.ElementTree as et

def main():
    local = time.localtime(time.time()-3600)

    legend = ['강수형태','습도','1시간 강수량','기온','동서바람성분','풍향','남북바람성분','풍속']

    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
    params = {'serviceKey': 'loGEsi8RLLPDoscN/+N/FQs4Gck/La0uzw51zooTczK3aWcmK6mvoHJ8tfF1uCtnKl2OdfmXYnz1QtEauhwWPA==','pageNo': '1', 'numOfRows': '1000', 'dataType': 'XML','base_date': str(local.tm_year).zfill(2) + str(local.tm_mon).zfill(2) + str(local.tm_mday).zfill(2),'base_time': str(local.tm_hour).zfill(2) + str(local.tm_min).zfill(2), 'nx': '61', 'ny': '126'}

    response = requests.get(url, params=params)
    text = response.text
    fname = str(local.tm_year).zfill(2)+str(local.tm_mon).zfill(2)+str(local.tm_mday).zfill(2)+str(local.tm_hour).zfill(2)+str(local.tm_min).zfill(2)
    f = open("report"+".xml", 'w', encoding='UTF-8')
    f.write(text)
    f.close()

    file = et.parse("report"+".xml")
    root = file.getroot()

    try:
        data = root[1][1]
    except:
        print("Error in data")
        exit()

    result = open("results/"+fname+".txt", 'w', encoding='UTF-8')

    i = 0
    for child in data:
        result.write(legend[i]+'\n')
        print(legend[i])
        print(child[5].text)
        result.write(child[5].text + ' ' + "\n")
        result.write("\n")
        print()
        i=i+1

    result.close()

if __name__ == '__main__':
    main()