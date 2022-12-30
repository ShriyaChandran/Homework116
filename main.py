import pandas as pd
import plotly.express as px

df = pd.read_csv("Admission_Predict.csv")

toefl_score = df["TOEFL Score"].tolist()
result = df["Chance of admit"].tolist()



fig = px.scatter(x=toefl_score, y=result)
fig.show()

import plotly.graph_objects as go

toefl_score = df["TOEFL Score"].tolist()
gre_score = df["GRE Score"].tolist()

results = df["Chance of admit"].tolist()
colors=[]
for data in results:
  if data == 1:
    colors.append("green")
  else:
    colors.append("red")



fig = go.Figure(data=go.Scatter(
    x=toefl_score,
    y=gre_score,
    mode='markers',
    marker=dict(color=colors)
))
fig.show()

#scores and chances of admit
scores = df[["GRE Score", "TOEFL Score"]]

#results
results = df["Chance of admit"]