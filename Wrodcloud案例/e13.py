from wordcloud import WordCloud
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import jieba

# 打开文本
text = open("2.第一回 灵根育孕源流出 心性修持大道生.txt", encoding="utf-8").read()
# 中文分词
text = ' '.join(jieba.cut(text))   # 利用jieba进行分词形成列表，将列表里面的词用空格分开并拼成长字符串。
# 生成对象
# wc = WordCloud(font_path="SimHei.ttf", width=800, height=600, mode="RGBA", background_color=None).generate(text)
#使用蒙版生成词云
mask = np.array(Image.open("wordcloud_mask.png"))
wc = WordCloud(mask = mask,font_path="SimHei.ttf", width=800, height=600, mode="RGBA", background_color=None).generate(text)

# 显示词云
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")     #关闭坐标轴
plt.show()

# 保存到文件
wc.to_file("2.2wordcloud2.png")