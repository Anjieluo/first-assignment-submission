import matplotlib.pyplot as plt
#创建画布和坐标轴
fig, ax = plt.subplots()
#绘制文本
ax.text(0.5, 0.5, "Hello World!", fontsize=30, ha='center', va='center')
#隐藏坐标轴
ax.axis('off')
#显示图形
plt.show()
plt.pause(0)
