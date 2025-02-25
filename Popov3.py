import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Создаем сетку значений x и y
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

# Вычисляем значения z
z = np.sin(np.sqrt(x**2 + y**2))

# Создаем 3D график
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Строим поверхность
ax.plot_surface(x, y, z, cmap='viridis')

# Добавляем подписи
ax.set_title('3D график функции z = sin(sqrt(x^2 + y^2))')
ax.set_xlabel('X ось')
ax.set_ylabel('Y ось')
ax.set_zlabel('Z ось')

# Показываем график
plt.show()