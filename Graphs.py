import pandas as pd
import plotly_express as px

data = pd.read_csv("data.csv")
scatter_graph = px.scatter(data, x="date", y="cases", color="country")
scatter_graph.show()
