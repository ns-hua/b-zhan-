import requests
import re
url = "https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js"
headers = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
response = requests.get(url,headers)
re_alias_list = r'"alias":"(.*?)","'
alias_list = re.findall(re_alias_list,response.text)
alias_list = alias_list[:2]
counter = 1
for i in alias_list:
    url_2 = "https://lol.qq.com/biz/hero/"+ i +".js"
    response = response = requests.get(url_2,headers)
    re_num_list = r'"num":(.*?),"name"'
    num_list = re.findall(re_num_list,response.text)
    for n in num_list:
        if(int(n)<=9):
            url = "https://game.gtimg.cn/images/lol/act/img/skin/big"+str(counter)+"00"+n+".jpg"
        else:
            url = "https://game.gtimg.cn/images/lol/act/img/skin/big" + str(counter) + "0" + n + ".jpg"
        response = requests.get(url,headers)
        with open("D:\\pycharm\\hellow word\\皮肤\\"+url.split("/")[-1]+'.jpg','wb')as f:
            f.write(response.content)
            print("已下载：第"+url.split("/")[-1]+"图片")
    counter = counter+1
