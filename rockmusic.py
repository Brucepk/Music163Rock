import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
import numpy as np
import PIL.Image as Image
from os import path

'''
作者：pk哥
公众号：Python知识圈
日期：2018/08/11
代码解析详见公众号「Python知识圈」。

'''


f = open(r'F:\\rock\\all\\all_lyrics.txt', 'r', encoding='utf-8')
text = f.read()
f.close()

cut = jieba.cut(text, cut_all=True)
word = ",".join(cut).strip().replace('作词', '').replace('作曲', '')
print(word)

# 绘制词云
coloring = np.array(Image.open("E:\\截图\\163singer\\song163\\gita.jpg"))    # 电脑中自定义词云的图片
my_wordcloud = WordCloud(background_color="white", max_words=2000, max_font_size=50,
                         mask=coloring, random_state=42, font_path='./font/STXINGKA.TTF',
                         scale=2).generate(word)  # 定义词云背景图颜色、尺寸、字体大小、电脑中字体选择,random_state 为每个单词返回一个PIL颜色
image_colors = ImageColorGenerator(coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))  # 绘图颜色
plt.imshow(my_wordcloud)   # 绘图内容
plt.axis("off")
plt.show()  # 显示图
d = path.dirname(__file__)   # project 当前目录
my_wordcloud.to_file(path.join(d, 'rock1.png'))