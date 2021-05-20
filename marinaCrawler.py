
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as Soup
import os
import time
import requests

IG_USERNAME='pianoprince0125@yahoo.com.tw'
IG_PASSWORD='linkevin'

# 加启动配置
option = webdriver.ChromeOptions()

option.add_experimental_option('useAutomationExtension', False)
option.add_experimental_option('excludeSwitches', ['enable-automation'])
url = 'https://www.instagram.com/marinanagasawa1008/'
chromedriver_path = r"C:\Users\Kaiku\Desktop\crawler\spider\chromedriver.exe"

browser = webdriver.Chrome(executable_path=chromedriver_path,chrome_options=option)
soup = Soup(browser.page_source, "html.parser")
media_url = []



def openchrome():
    page = browser.get(url)

def main():
    browser.get(url)
    soup = Soup(browser.page_source, "html.parser")
    data = soup.find_all(class_="KL4Bh")[1].img.get('src')
    # for i in data:
    #     img_frame = i.img.get('src')
    #     media_url.append(img_frame)
    img_frame = requests.get(data)
    if not os.path.exists("marina"):
        os.mkdir("marina")

    with open("marina\\" + "marinaImg" + str(2) + ".jpg", "wb") as file:  # 開啟資料夾及命名圖片檔
        file.write(img_frame.content)


    
    # if soup.find(class_ = 'KL48h' != None):
    #     print('KL48h != None')
    #     soup = Soup(browser.page_source,'html.parser')
    #     print(soup)
    #     print('1--------------------------')
    #     img_frame = soup.find_all("div",class_ = "KL48h")
    #     print(img_frame)
    #     print('2------------------------------')
    #     for i in img_frame:
    #         try:
    #             data = img_frame.img.get("src")
    #             print(data)
    #             print('3-----------------------------------')
    #             media_url.append(data)
    #             print('0000')
    #         except:
    #             print('11111')

        # button = 1
        # while button != None:
        #     soup = Soup(browser.page_source,'html.parser')
        #     time.sleep(1)
        #     img_frame = soup.find_all(class_ = "CKrof")
        #     for i in img_frame:
        #         try:
        #             new_img = i.img.get('src')
        #             if new_img != None & new_img not in media_url:
        #                 media_url.append(new_img)
        #                 count += 1
        #         except:
        #             print('some error')

    # else:
    #     soup = Soup(browser.page_source,'html.parser')
    #     print('2222')



    # browser.get(url)
    
    # data = soup.find_all(class_="KL4Bh")[0].img.get('src')
    

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



if __name__ == '__main__':
    openchrome()
    login()
    main()
    print(media_url)
    


