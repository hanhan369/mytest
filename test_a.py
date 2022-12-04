import requests
import json
def getallversionBigTopThree(appkey: str) -> list:
    url = 'https://radar.qihoo.net/report/config/dimensionList.do'
    parame = {
        "appkey": appkey,
        "rptType": "m2id",
        "dateRange": "1",
        "dimension": "version",
        "gt": "0"
    }
    resp = requests.post(url, data=parame)
    content = json.loads(resp.content.decode())
    allversion = content['data']
    all_list_version = []
    if len(allversion) >= 1:
        if allversion[0]['name'] == "全部":
            allversion.pop(0)
        for item in allversion:
            all_list_version.append(item['name'])
        print(all_list_version)
        return all_list_version
    return []


all_list_version = getallversionBigTopThree('9b31003b2ee8447bb697ba2e5211ee30')


def compare_version_lists(v1_lst, v2_lst):
    """
    比较版本号列表，从高位到底位逐位比较，根据情况判断大小。
    :param v1_lst:
    :param v2_lst:
    :return:
    """
    for v1, v2 in zip(v1_lst, v2_lst):
        if v1 >= v2:
            return 1
        elif v1 < v2:
            return -1
    return 0

if len(all_list_version)<=1:
    max_version = all_list_version
else:
    max_version = all_list_version[0]

    for i in range(1,len(all_list_version)):
        comp_result = compare_version_lists(all_list_version[i-1],all_list_version[i])

        if comp_result>=0:
            max_version = all_list_version[i-1]
        else:
            max_version = all_list_version[i]
        print(print(all_list_version[i-1]),"   " ,print(all_list_version[i]),"   " ,max_version)
print(max_version)

