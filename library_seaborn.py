from iris import px, iris, sns, plt, df

# Визуализация с использованием Plotly
fig = px.histogram(iris, x='sepal_length', color='species', barmode='overlay', title='Гистограмма длины чашелистика (Sepal Length) - Plotly',
                   labels={'sepal_length': 'Длина чашелистика (cm)', 'count': 'Частота'})

fig.update_layout(xaxis_title='Длина чашелистика (cm)', yaxis_title='Частота')
fig.show()


# Seaborn
# Диаграмма рассеяния
sns.set(style="whitegrid")
sns.scatterplot(x='x', y='y', hue='label', data=df)
plt.title('Диаграмма рассеяния с Seaborn')
plt.show()

# Тепловая карта
corr_matrix = df.corr()
ax = sns.heatmap(corr_matrix, annot=True)
plt.title('Тепловая карта корреляции')
plt.show()