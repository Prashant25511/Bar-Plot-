import matplotlib.pyplot as plt 
import numpy as np 

w = 0.15
x = ["Area", "Current Heat Loss", "Improved Heat Loss", "Heat Loss Saving", "Estimated Energy Saving"]
External_Wall = [82, 1230, 656, 46.67, 14.50]
Floor = [63, 898, 536, 0.00, 9.10]
Roof = [101, 503, 252, 50.00, 6.30]
External_Doors = [4, 320, 66, 79.41, 6.40]
Window = [8, 1018, 178, 82.50, 21.20]

bar1 = np.arange(len(x))
bar2 = [i+w for i in bar1]
bar3 = [i+w for i in bar2]
bar4 = [i+w for i in bar3]
bar5 = [i+w for i in bar4]

plt.bar(bar1, External_Wall, w, label = "External_Wall", color = 'b')
plt.bar(bar2, Roof, w, label = "Roof", color = 'y')
plt.bar(bar3, External_Doors, w, label = "External_Doors", color = 'r')
plt.bar(bar4, Window, w, label = "Window", color = 'k')
plt.bar(bar5, Floor, w, label = "Window", color = 'g')
plt.xticks(bar1+0.3, x, fontname='Times New Roman', fontsize = 12)

plt.xlabel("Different Physical Parameters", fontname='Times New Roman', fontsize = 14)
plt.ylabel("Respective Values", fontname='Times New Roman', fontsize = 14)

for i in range(len(x)):
	plt.text(i, External_Wall[i], External_Wall[i], ha="center", va="bottom", fontsize = 7)
	plt.text(i+w, Roof[i], Roof[i], ha="center", va="bottom", fontsize = 7)
	plt.text(i+2*w, External_Doors[i], External_Doors[i], ha="center", va="bottom", fontsize = 8)
	plt.text(i+3*w, Window[i], Window[i], ha="center", va="bottom", fontsize = 8)
	plt.text(i+4*w, Floor[i], Floor[i], ha="center", va="bottom", fontsize = 8)

	

plt.legend()
plt.title('Comparison of Two Different Houses', fontname='Times New Roman', fontsize = 18, weight = 'bold')

plt.show()

