from lxml import etree
import requests
import time  # 这里导入时间模块，以免豆瓣封你IP

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"  # 伪装成浏览器
}
url = "https://movie.douban.com/chart"  # 豆瓣电影排行榜
data = requests.get(url, headers=headers).text  # 给定url并用requests.get()方法来获取页面的text

s = etree.HTML(data)  # 用etree.HTML()来解析下载的页面数据“data”。
file = s.xpath(
    './/*[@id="content"]/div/div[1]/div/div/table/tr'
)  # copy网页的xpath，截取前半部分通用的
time.sleep(3)  # 睡眠，防止爬太快被网站封了
scores = "评分:"
evaluate = "一句话评价:"
actor = "上映日期及主演："
# 创建一个文件，如果文件已经存在，则清空文件内容
with open("output.txt", "w") as f:
    f.truncate()
with open("output.txt", "a") as f:
    for div in file:
        title = div.xpath("./td[1]/a/@title")[0]
        href = div.xpath("./td[1]/a/@href")[0]
        score = div.xpath("./td[2]/div/div/span[2]/text()")[0]
        num = (
            div.xpath("./td[2]/div/div/span[3]/text()")[0]
            .strip("(")
            .strip()
            .strip(")")
            .strip()
        )
        director = div.xpath("./td[2]/div/p/text()")[0]  # 截取后半部分的xpath，定位到具体的内容
        print(f"{title},{href},{actor}{director},{scores}{score},{num}\n")  # 输出爬取到的内容
        f.write(f"{title},{href},{actor}{director},{scores}{score},{num}\n")  # 将内容写入文件
