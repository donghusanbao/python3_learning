import numpy as np
import matplotlib.pyplot as plt

fig1 = plt.figure(num='fig1', figsize=(8, 4), dpi=75, facecolor='#FFFFFF')
ax1 = fig1.add_subplot(121)
ax1.set_title('Pic 1')
ax1.set_xlabel('x', fontsize=18, fontfamily='sans-serif', fontstyle='italic')
ax1.set_ylabel('y', fontsize='x-large', fontstyle='oblique')
x = np.arange(5)
y1 = x ** 2
y2 = x
y3 = x ** 1.5
y4 = np.log(2 * x + 1)
ax1.set_xlim(0, 4)
ax1.set_ylim(0, 16)
ax1.tick_params(axis="x", labelsize=15, labelrotation=-20)
ax1.tick_params(axis="y", labelsize=15)
ax1.xaxis.set_ticks(np.linspace(0, 4, 9, endpoint=True))
ax1.yaxis.set_ticks(np.linspace(0, 16, 9, endpoint=True))
ax1.plot(x, y1, marker='s', ls='-', label='first', c='g', linewidth=4, ms=12, mfc='w', mec='g', mew=2)
ax1.plot(x, y2, marker='o', ls='-', label='second', c='b', linewidth=4, ms=12, mfc='w', mec='b', mew=2)
ax1.plot(x, y3, marker='^', ls='-', label='third', c='black', linewidth=4, ms=12, mfc='w', mec='black', mew=2)
ax1.plot(x, y4, marker='>', ls='-', label='fourth', c='y', linewidth=4, ms=12, mfc='w', mec='y', mew=2)
leg = ax1.legend(loc='upper left', fontsize=10, markerscale=0.7, frameon=True, ncol=2, borderpad=0.5,
                 labelspacing=1, handlelength=3, handletextpad=1, borderaxespad=0.5, columnspacing=1)
for line in leg.get_lines():
    line.set_linewidth(2.0)
ax2 = fig1.add_subplot(122)
ax2.set_title('pic 2')
plt.xlabel('x')
plt.ylabel('y')
x = np.arange(5)
y1 = 2 * x + 1
y2 = x + 1
plt.bar(x, y1, width=0.3, label='first')
plt.bar(x + 0.4, y2, width=0.3, label='second')
plt.legend()
plt.show()
