import bs4
import urllib.request as req


def getData(url):

    request = req.Request(url, headers={
        "cookie": "over18=1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    })

    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div", class_="title")

    for title in titles:
        if title.a != None:
            print(title.a.string)

    nextLink = root.find("a", string="‹ 上頁")
    return nextLink["href"]
    # print(nextLink["href"])


url = "https://www.ptt.cc/bbs/Gossiping/index.html"

i = 0
for i in range(5):
    url = "https://www.ptt.cc" + getData(url)
    i += 1
