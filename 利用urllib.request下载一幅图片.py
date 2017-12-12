import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1,1000)
    full_name = str(name)+'.jpg'
    urllib.request.urlretrieve(url,full_name)
download_web_image("http://club2.autoimg.cn/album/g17/M11/2F/88/userphotos/2017/08/12/23/500_wKjBxlmPIKaAF1iSAAMsVpkYP1s862.jpg")






