import numpy as np
import matplotlib.pyplot as plt

# 1. Задаємо вершини трикутника
P1 = np.array([0, 0])
P2 = np.array([1, 0])
P3 = np.array([0.5, np.sqrt(3) / 2])
vertices = np.array([P1, P2, P3])

# 2. Генеруємо точки для трикутника Серпінського
num_points = 10000
current_point = np.mean(vertices, axis=0)
points = [current_point]

for _ in range(num_points):
    vertex = vertices[np.random.randint(0, 3)]
    current_point = (current_point + vertex) / 2
    points.append(current_point)

points = np.array(points)

# 3. Побудова трикутника Серпінського (верхній графік)
plt.figure(figsize=(8, 8))
plt.scatter(points[:, 0], points[:, 1], s=1, c='black', alpha=0.5)
plt.axis('off')
plt.title('Трикутник Серпінського')
plt.show()

# 4. Побудова нижнього графіку з ітераційними точками
demo_points = points[:5]
plt.figure(figsize=(8, 6))
plt.scatter(vertices[:, 0], vertices[:, 1], c='red', s=100, label='Вершини (P1, P2, P3)')
triangle = np.vstack([vertices, vertices[0]])
plt.plot(triangle[:, 0], triangle[:, 1], 'r--')
plt.scatter(demo_points[:, 0], demo_points[:, 1], c='black', s=50, label='Ітераційні точки')
for i in range(len(demo_points) - 1):
    plt.plot([demo_points[i][0], demo_points[i+1][0]], 
             [demo_points[i][1], demo_points[i+1][1]], 'b--')
plt.text(P1[0], P1[1], 'P1', fontsize=12, ha='right')
plt.text(P2[0], P2[1], 'P2', fontsize=12, ha='left')
plt.text(P3[0], P3[1], 'P3', fontsize=12, ha='center', va='bottom')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Побудова трикутника Серпінського')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
