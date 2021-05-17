from bs4 import BeautifulSoup
import requests
import os
import urllib.request as req


url = "https://unsplash.com/s/photos/car"
headers = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
request = req.Request(url, headers={
    "User-Agent": headers
})

with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

root = BeautifulSoup(data, "html.parser")

# data = root.find("img", {"class": "_2UpQX"})
data = root.find("div", class_="_1tO5-")


print(data.img.get("src"))

if not os.path.exists("images"):
    os.mkdir("images")  # 建立資料夾

imgLink = requests.get(data.img.get("src"))

with open("images\\" + "car" + str(1) + ".jpg", "wb") as file:  # 開啟資料夾及命名圖片檔
    file.write(imgLink.content)  # 寫入圖片的二進位碼
