from re import VERBOSE
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os
import ast
import sys
import json
from PIL import Image
import requests
from skimage import color
from skimage import io
#--------------------------------------------------------크롤링-----------------------------------------------
driver = webdriver.Chrome()
driver.get("http://www.google.co.kr/imghp?hl=ko&tab=wi&ogbl")
Name = ("기아타이거즈 선수 사진")
elem = driver.find_element_by_name("q")
elem.send_keys(Name)
elem.send_keys(Keys.RETURN)

SCROLL_PAUSE_TIME = 1

last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_elements_by_css_selector(".mye4qd").click()
        except:
            break
    last_height = new_height
images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 1
try:
    for image in images:
        image.click()
        time.sleep(2)
        imgUrl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(imgUrl, "기아타이거즈" + str(count) + ".png")

        count = count + 1
        if count == 200:
            break
except:
    pass
driver.close()
# #----------------------------------------------------------------------흑백전환-------------------------------------------------------------------------------

# file_list = os.listdir("C:\\_pythontest01\\dog\\selenium\\han\\")
# count = 1
# try:
#     for image in range(len(file_list)):
#         img = io.imread(file_list[image])
#         imgGray = color.rgb2gray(img)
#         char_path = r"C:\\grayDino\\"+"조진웅"+str(count)+".png"
#         io.imsave(char_path, imgGray)
#         count+=1
# except:
#     pass


# #----------------------------------------------------------------------짜르기------------------------------------------------------------------------------

# client_id = "CC88RjbvZ4fMWAWQ7GkY"
# client_secret = "NtkWkcAIG_"
# path = r'C:\grayDino'
# file_list = os.listdir(path)
# count = 1
# url = "https://openapi.naver.com/v1/vision/face"
# for idx in range(len(file_list)):
#     files = {'image': open(path +'/' + file_list[idx], 'rb')}
#     print(files)
#     headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
#     response = requests.post(url,  files=files, headers=headers)
#     rescode = response.status_code
#     try:
#         if(rescode==200):
#             a = ast.literal_eval(str(response.text))
#             va = a.get('info')
#             vb = va.get('faceCount')
#             if vb == 1:
#                 b = a.get('faces')
#                 c = b[0].get('roi')
#                 x = c.get('x')
#                 y = c.get('y')
#                 x1 = c.get('width')
#                 y1 = c.get('height')
#                 z = x+x1
#                 p = y+y1
#                 img = Image.open(path + '/' + file_list[idx])
#                 cropping_area = (x,y,z,p)
#                 cropped_img = img.crop(cropping_area)
#                 cropped_img.save("d:\\"+ "조진웅" + str(count) + '.png')
#                 count += 1
#     except:
#         pass 
         
        
#     else:
#         pass