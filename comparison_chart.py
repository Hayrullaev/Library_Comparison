import plotly.graph_objects as go
import numpy as np

# Данные для графика
labels = ['Легкость использования', 'Кастомизация', 'Эстетика', 'Интерактивность', 'Поддержка 3D', 'Работа с Pandas']
matplotlib_scores = [7, 9, 5, 3, 6, 8]  # Оценки от 1 до 10
seaborn_scores = [9, 7, 9, 1, 2, 8]
plotly_scores = [8, 6, 8, 10, 8, 8]

# Замыкание графиков для Plotly
matplotlib_scores += matplotlib_scores[:1]
seaborn_scores += seaborn_scores[:1]
plotly_scores += plotly_scores[:1]
labels += labels[:1]

# Создание радиального графика
fig = go.Figure()

# Добавление данных для каждой библиотеки
fig.add_trace(go.Scatterpolar(
    r=matplotlib_scores,
    theta=labels,
    fill='toself',
    name='Matplotlib',
    marker_color='blue'
))

fig.add_trace(go.Scatterpolar(
    r=seaborn_scores,
    theta=labels,
    fill='toself',
    name='Seaborn',
    marker_color='orange'
))

fig.add_trace(go.Scatterpolar(
    r=plotly_scores,
    theta=labels,
    fill='toself',
    name='Plotly',
    marker_color='green'
))

# Настройка макета
fig.update_layout(
    title='Сравнение библиотек визуализации данных',
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 10]
        )
    ),
    showlegend=True
)

# Отображение графика
fig.show()