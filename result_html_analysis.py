#coding=utf-8
import json
import os
import time

from subprocess import run
import sys

path_json = os.path.join(sys.argv[1],sys.argv[2])
name_result_json = "result_json_"+sys.argv[3]+".json"
name_result_html = "result_html_"+sys.argv[3]+".html"
path_result_json = os.path.join(sys.argv[1],"result",name_result_json)
path_result_html = os.path.join(sys.argv[1],"result",name_result_html)
path_newman = r"C:\Users\Administrator\AppData\Roaming\npm\newman"

#实例：
# path_json = r"D:\newman_test\fail1-sug.postman_collection.json"
# path_result_json = r"D:\newman_test\aaa.json"
# path_result_html = r'D:\newman_test\bbb.html'
cmd_str = path_newman+' run '+ path_json + ' -r json,htmlextra --reporter-json-export '+ path_result_json + '   --reporter-htmlextra-export '+ path_result_html
print(cmd_str)
# run(cmd_str, shell=True)
os.system(cmd_str)
print("执行完毕，等待解析...")
# time.sleep(3)
with open(path_result_json,"r",encoding='utf-8') as f:
    ret_dic = json.load(f)
    if(len(ret_dic['run']['failures']) == 0):
        print("断言全部通过")
    else:
        print("断言失败case如下：")
    for i in range(len(ret_dic['run']['failures'])):
        test_txt = ret_dic['run']['failures'][i]['error']['test']
        failure_txt = ret_dic['run']['failures'][i]['error']['message']
        print(f"断言：{test_txt},执行结果：{failure_txt}")


