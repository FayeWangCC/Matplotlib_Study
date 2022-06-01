from matplotlib import pyplot as plt

x = range(2, 26, 2)
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 27, 22, 18, 15]

# 设置图形大小
plt.figure(figsize=(10, 5))

# 设置x轴刻度
# plt.xticks(range(2, 25))
_xticks_labels = [i for i in range(2, 25)]
plt.xticks(_xticks_labels)
# 设置y轴刻度
_yticks_labels = [i for i in range(min(y) - 3, max(y) + 3)]
plt.yticks(_yticks_labels)
# 绘图
plt.plot(x, y)
# 展示图形
plt.show()
