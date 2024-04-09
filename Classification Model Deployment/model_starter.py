import pandas as pd
from joblib import dump
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder
from sklearn.ensemble import GradientBoostingClassifier

COLS = ['class', 'odor', 'gill-size', 'gill-color', 'stalk-surface-above-ring',
       'stalk-surface-below-ring', 'stalk-color-above-ring',
       'stalk-color-below-ring', 'ring-type', 'spore-print-color']

df = pd.read_csv('mushrooms.csv')
df = df[COLS]

pipe = Pipeline([
    ('encoder', OrdinalEncoder()),
    ('gbc', GradientBoostingClassifier(max_depth=5, random_state=42))
])

x = df.drop(['class'], axis=1)
y = df['class']

pipe.fit(x, y)

dump(pipe, 'model/pipe.joblib')
