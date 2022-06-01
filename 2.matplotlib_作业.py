import random

from matplotlib import pyplot as plt
from matplotlib import font_manager

# 设置中文字体显示
# 实例化中文字体
font_ya_hei = font_manager.FontProperties(fname='C:/Windows/Fonts/msyh.ttc')

x = [i for i in range(0, 120)]
y = [random.randint(25, 30) for i in range(0, 120)]

# 设置图像大小
plt.figure(figsize=(15, 8))

# 设置x轴刻度显示为字符串
_x = list(x)
_xticks_labels = ['10点{}分'.format(i) for i in range(60)]
_xticks_labels += ['11点{}分'.format(i) for i in range(60)]

# rotation:旋转显示
plt.xticks(_x[::5], _xticks_labels[::5], rotation=45, fontproperties=font_ya_hei)

# 设置y轴刻度
_yticks_labels = [j / 2 for j in range(44, 66)]
plt.yticks(_yticks_labels)

# 添加描述信息
plt.xlabel('时间', fontproperties=font_ya_hei)
plt.ylabel('温度 单位(℃)', fontproperties=font_ya_hei)
plt.title('10点到12点每分钟的温度变化情况', fontproperties=font_ya_hei)

# 绘图
plt.plot(x, y)
# 展示
plt.show()
