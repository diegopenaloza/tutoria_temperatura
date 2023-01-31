import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px


# Importar los datos a un data frame
df = pd.read_csv("5. T_Hemisferio_Norte.csv", skiprows=8)

df

df.to_excel("output_0.xlsx")  

df['time'] = pd.to_datetime(df['time'], format='%Y%m')
df['year'] = df['time'].dt.year
df['month'] = df['time'].dt.month

df.head(2)

df.to_excel("output_1.xlsx")  

df.info()

sns.heatmap(df.isnull(), cbar=False)

# Limpiar errores de datos
df = df.dropna()

duplicate = df[df.duplicated()]
duplicate 

# +
# Indexar los datos por fechas
# -

df_yearly=df.groupby("year").mean()[["t2"]]

df_yearly.info()

df_yearly.head(2)

df_yearly=df_yearly.rename(columns={"t2":"TempMean"})

df_yearly

df_yearly.to_excel("output.xlsx")  

fig = px.bar(df_yearly, y='t2', x=df_yearly.index, text_auto='.2s',
            title="Controlled text sizes, positions and angles")
fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
fig.show()

# Generar gráfico de boxplots para la temperatura promedio anual
fig = px.box(df_yearly, y="TempMean", width=400, height=600, points="all",    # only outliers
)
# fig.update_traces(quartilemethod="exclusive") # or "inclusive", or "linear" by default
fig.update_layout(title_text="Box Plot Temperatura Promedio Anual")
fig.update_layout(
    paper_bgcolor='white',
    plot_bgcolor='rgba(0,0,0,0)'
)
fig.update_layout(title_text="Box Plot Temperatura Promedio Anual", xaxis=dict(showgrid=False, zeroline=False), yaxis=dict(showgrid=False, zeroline=False))
fig.show()

# +
import plotly.graph_objects as go
# fig = go.Figure(width=400, height=600,)
import plotly.graph_objects as go
fig = go.Figure(layout=go.Layout(width=400, height=600) )

fig.add_trace(go.Box(
    y=df_yearly["TempMean"],
    name="TempMean",
    jitter=0.3,
    pointpos=-1.8,
    boxpoints='all', # represent all points
    marker_color='rgba(219, 64, 82, 0.6)',
 
    # line_color='rgb(7,40,89)',
    
))

fig.update_layout(title_text="Box Plot Temperatura Promedio Anual")

# +
# Crea la figura
fig = px.scatter(df_yearly, x=df_yearly.index, y="TempMean", trendline="ols",
                 title="Temperatura promedio anual",
                 labels={"TempMean": "Temperatura (°C)", "year": "Año"},
                  width=800, height=600
                )

# Personaliza la leyenda
fig.update_layout(legend=dict(title="Tendencia"),
                  xaxis=dict(range=[df_yearly.index[0], '2028-12-31']))
fig.update_traces(line=dict(color='red'))

fig.update_layout(title_text="Box Plot Temperatura Promedio Anual")
fig.update_layout(
    # paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)
fig.update_layout(title_text="Box Plot Temperatura Promedio Anual", xaxis=dict(showgrid=False, zeroline=False), yaxis=dict(showgrid=False, zeroline=False))
fig.show()

# -


