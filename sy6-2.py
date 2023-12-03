from wordcloud import WordCloud
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import jieba
import random

# 生成随机颜色
def random_color():
   return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# 打开文本
text = open(r"./词云实验案例素材/三国演义第1章.txt", encoding="utf-8").read()
# 中文分词
text = ' '.join(jieba.cut(text))   # 利用jieba进行分词形成列表，将列表里面的词用空格分开并拼成长字符串。
# 生成对象
# wc = WordCloud(font_path="SimHei.ttf", width=800, height=600, mode="RGBA", background_color=None).generate(text)
#使用蒙版生成词云
mask = np.array(Image.open(r"./词云实验案例素材/image/tree.webp"))
wc = WordCloud(mask = mask,font_path=r"./词云实验案例素材/simhei.ttf", width=800, height=600, mode="RGBA", background_color=None).generate(text)
wc.font_color=random_color
# 显示词云
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")     #关闭坐标轴
plt.show()

# 保存到文件
wc.to_file("2.2wordcloud2.png")