from iris import plt, iris, pd, make_blobs

# Визуализация с использованием Matplotlib
plt.figure(figsize=(10, 6))
for species in iris['species'].unique():
    subset = iris[iris['species'] == species]
    plt.hist(subset['sepal_length'], alpha=0.5, bins=10, label=species)

plt.title('Гистограмма длины чашелистика (Sepal Length) - Matplotlib')
plt.xlabel('Длина чашелистика (cm)')
plt.ylabel('Частота')
plt.legend()
plt.grid(True)
plt.show()

# Другие примеры

# Генерация случайных данных
X, y = make_blobs(n_samples=1000, centers=3, n_features=2, random_state=42)
df = pd.DataFrame(X, columns=['x', 'y'])
df['label'] = y

# Matplotlib
# Простая линейная диаграмма
plt.figure(figsize=(10, 6))
plt.plot(df['x'], df['y'], 'o')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Простая линейная диаграмма')
plt.show()

# Гистограмма
plt.figure(figsize=(10, 6))
plt.hist(df['x'], bins=20)
plt.xlabel('x')
plt.ylabel('Количество')
plt.title('Гистограмма')
plt.show()