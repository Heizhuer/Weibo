import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud, ImageColorGenerator
import numpy
import PIL.Image as Image


fp = open("test.txt", encoding="utf-8", errors="ignore")
new_fp = open("new_fp.txt", "a", encoding="utf-8", errors="ignore")
try:
    all_text = fp.read()
    new_fp.write(all_text)
finally:
    fp.close()
    new_fp.close()

with open('new_fp.txt', 'r', encoding='utf-8') as fp:
    text = fp.read()
    text = "".join([i.strip() for i in text])

    # jieba分词
    wordlist_jieba = jieba.cut(text, cut_all=False)
    wl_space_split = " ".join(wordlist_jieba)
    # print(wl_space_split)

    # 云词
    coloring = numpy.array(Image.open("F:\conda\weibo\img\heart.png"))
    my_wordcloud = WordCloud(background_color="white", max_words=2000, mask=coloring,
                             max_font_size=60, random_state=42, scale=4,
                             font_path="C:\Windows\Fonts\simhei.ttf").generate(wl_space_split)

    image_colors = ImageColorGenerator(coloring)
    plt.imshow(my_wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
    plt.axis("off")
    plt.figure()
    plt.show()
    # 保存图片 并发送到手机
    # my_wordcloud.to_file('Signature_word')
    # itchat.send_image("xxx", 'filehelper')