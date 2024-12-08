from iris import plt, iris, sns, px, df

# Визуализация с использованием Seaborn
plt.figure(figsize=(10, 6))
sns.histplot(data=iris, x='sepal_length', hue='species', bins=10, alpha=0.5, kde=False)

plt.title('Гистограмма длины чашелистика (Sepal Length) - Seaborn')
plt.xlabel('Длина чашелистика (cm)')
plt.ylabel('Частота')
plt.grid(True)
plt.show()


# другие примеры

# Интерактивная диаграмма рассеяния
fig = px.scatter(df, x='x', y='y', color='label')
fig.update_layout(title_text='Интерактивная диаграмма рассеяния с Plotly')
fig.show()