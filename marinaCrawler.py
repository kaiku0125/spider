from __future__ import division
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as Soup
import os
import time
import requests
import sys
import progressbar
import math

from urllib3.packages.six import b

IG_USERNAME='pianoprince0125@gmail.com'
IG_PASSWORD='yourpassword'
# 步驟1: 改targetUrl
# 步驟2: 改scrolling的次數區間
# 步驟3: 改儲存名稱

# 加启动配置
option = webdriver.ChromeOptions()
option.add_experimental_option('useAutomationExtension', False)
option.add_experimental_option('excludeSwitches', ['enable-automation'])
url = 'https://www.instagram.com/marinanagasawa1008' #targetUrl
IGurl = 'https://www.instagram.com'
chromedriver_path = r"C:\Users\Kaiku\Desktop\crawler\spider\chromedriver.exe"

browser = webdriver.Chrome(executable_path=chromedriver_path,chrome_options=option)
soup = Soup(browser.page_source, "html.parser")
media_url = []
finalall_url = []
SCROLL_PAUSE_TIME = 1


def openchrome():
    page = browser.get(url)

def login():
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.NAME, 'username')))

    # ------ 網頁元素定位 ------
    username_input = browser.find_elements_by_name('username')[0]
    password_input = browser.find_elements_by_name('password')[0]
    print("inputing username and password...")
    # ------ 輸入帳號密碼 ------
    username_input.send_keys(IG_USERNAME)
    password_input.send_keys(IG_PASSWORD)

    # ------ 登入 ------
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH,
    '//*[@id="loginForm"]/div/div[3]/button/div')))
    # ------ 網頁元素定位 ------
    login_click = browser.find_elements_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')[0]
    # ------ 點擊登入鍵 ------
    login_click.click()

    # ------ 不儲存登入資料 ------
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')))

    # ------網頁元素定位 ------
    store_click = browser.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')[0]

    # ------ 點擊不儲存鍵 ------
    store_click.click()

    # ------ 不開啟通知 ------
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button[2]')))

    # ------ 網頁元素定位 ------                                                                                                    
    notification_click = browser.find_elements_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')[0]

    # ------ 點擊不開啟通知 ------
    notification_click.click()
    print("Log in!")

def main():
    browser.get(url)
    wait = 0
    print('scrolling...')
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    scroll = True
    while scroll == True:
        lastCount = lenOfPage
        time.sleep(4)
        wait +=1
        lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        
        browser.page_source
        soup = Soup(browser.page_source, "html.parser")
        # get all browser post url
        if wait > 10:
            for i in soup.find_all('a', href = True):
                if i['href'].startswith('/p/'):
                    print('Link found : {0}'.format(i['href']))
                    if i['href'] not in media_url:
                        media_url.append(IGurl + i['href'])
        
        if lastCount==lenOfPage:
            scroll=False
        
        if wait == 15:
            scroll =False

        print('scrolling page :' + str(wait))

        # browser.execute_script("window.scrollTo(0,4000);")
        # time.sleep(SCROLL_PAUSE_TIME)
        # wait +=1
        # print('scrolling page :' + str(wait))
        # if wait == 40:
        #     break
    print('scrolling finish...')

    
     
    #獲得每個貼文的img
    count = 0 
    for i in media_url:
        browser.get(i)
        browser.page_source
        soup = Soup(browser.page_source, "html.parser")
        time.sleep(2)
        try:
            WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.CLASS_NAME, '_6CZji')))
            button = browser.find_elements_by_class_name('_6CZji')[0]
            
        except:
            button = None

        # 只有1張
        if button == None:
            soup = Soup(browser.page_source, "html.parser")
            img_frame = soup.find(class_="KL4Bh")
            try:
                new_img = img_frame.img.get('src')
                if (new_img != None):
                    finalall_url.append(new_img)
                    count += 1
                    print(count)
            except:
                pass

        # 進入post之後，每一秒按一次直到沒有下一頁按鈕為止
        # 並將得到的URL儲存在finalall_url之中
        while button!= None:
            soup = Soup(browser.page_source, "html.parser")
            time.sleep(1)
            try:
                img_frame = soup.find_all(class_="Ckrof")
                for i in img_frame:
                    try:
                        new_img = i.img.get('src')
                        if (new_img != None) & (new_img not in finalall_url):
                            finalall_url.append(new_img)
                            count += 1
                            print(count)
                    except:
                        pass
                button.click()
            except:
                break
        
            
    # 儲存檔案
    if not os.path.exists("marina"):
        os.mkdir("marina")

    num = 402
    for i in finalall_url:
        image = requests.get(i)
        with open("marina\\" + "marinaImg" + str(num) + ".jpg", "wb") as file:  # 開啟資料夾及命名圖片檔
            file.write(image.content)
        num+=1
        progressbar(num,count+num)
        time.sleep(0.25)

    # pbar.finish()
    print( '\n照片已儲存...')


def progressbar(cur, total):
    percent = '{:.2%}'.format(cur / total)
    sys.stdout.write('\r')
    sys.stdout.write("[%-50s] %s" % (
                            '=' * int(math.floor(cur * 50 / total)),
                            percent))
    sys.stdout.flush()

if __name__ == '__main__':
    openchrome()
    login()
    main()
    


