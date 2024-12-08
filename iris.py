import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.datasets import make_blobs

# Загружаем датасет Iris
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
iris = pd.read_csv(url, header=None, names=columns)




import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_blobs
import plotly.express as px

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