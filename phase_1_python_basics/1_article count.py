# 英文文章词频统计器（进阶版）
# 包含：停用词过滤 + 词形还原 + 柱状图可视化

import re
import matplotlib.pyplot as plt

# ================== 设置中文字体 ==================
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# ================== 1. 输入文章 ==================
with open("1_article.txt", "r", encoding="utf-8") as f:
    article = f.read()

# ================== 2. 预处理 ==================
# 转为小写
text_lower = article.lower()
# 用正则提取纯单词（去除标点和数字）
words = re.findall(r'\b[a-z]+\b', text_lower)

# ================== 3. 停用词过滤 ==================
stop_words = set(stopwords.words('english'))
# 保留自定义停用词（根据需要增删）
custom_stop = {'python', 'code'}  # 可根据分析目的自定义
stop_words.update(custom_stop)

# 过滤停用词
filtered_words = [w for w in words if w not in stop_words]

# ================== 4. 词形还原 ==================
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(w) for w in filtered_words]

# ================== 5. 词频统计 ==================
word_count = {}
for word in lemmatized_words:
    word_count[word] = word_count.get(word, 0) + 1

# 按频次排序，取前15个
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:15]

# ================== 6. 终端输出 ==================
print("=" * 40)
print("词频统计结果（已过滤停用词 & 词形还原）")
print("=" * 40)
for word, count in sorted_words:
    print(f"{word}: {count}")

# ================== 7. 可视化（柱状图） ==================
# 分离单词和计数
words_display, counts = zip(*sorted_words)

plt.figure(figsize=(10, 5))
plt.bar(words_display, counts, color='teal')
plt.title('Top 15 高频词', fontsize=14)
plt.xlabel('单词')
plt.ylabel('出现次数')
plt.xticks(rotation=45)  # 单词斜向显示，避免重叠
plt.tight_layout()

# 保存为图片（可在同目录下生成）
plt.savefig('1_word_frequency_chart.png', dpi=150)
print("\n图表已保存为 1_word_frequency_chart.png")

# 显示图表
plt.show()

