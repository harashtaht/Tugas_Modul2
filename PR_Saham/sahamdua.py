import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


#======= Data Telkom =========
dfTelkom = pd.read_csv(
    'SahamTLKM.csv',
    index_col=False,
    parse_dates=['Tanggal']
    )

dfTelkom = dfTelkom.set_index('Tanggal')
dfTelkom = dfTelkom.sort_index()
# print(dfTelkom)

#======== Data Indosat =======
dfIndosat = pd.read_csv(
    'SahamISAT.csv',
    index_col=False,
    parse_dates=['Tanggal']
    )

dfIndosat = dfIndosat.set_index('Tanggal')
dfIndosat = dfIndosat.sort_index()

#======== Data FREN ===========#

dfFren = pd.read_csv(
    'SahamFREN.csv',
    index_col=False,
    parse_dates=['Tanggal']
    )

dfFren = dfFren.set_index('Tanggal')
dfFren = dfFren.sort_index()

#========= Data XL =============#

dfXL = pd.read_csv(
    'SahamXL.csv',
    index_col=False,
    parse_dates=['Tanggal']
    )

dfXL = dfXL.set_index('Tanggal')
dfXL = dfXL.sort_index()

# print(dfFren['2016-01'])

#========= Plotting ==============#

# print(dfFren['Close'].resample('Y').mean())

# plt.style.use('seaborn')

# plt.plot(
#     dfTelkom.index, dfTelkom['Close'], 'r-',
#     dfIndosat.index, dfIndosat['Close'], 'g-',
#     dfXL.index, dfXL['Close'], 'b-',
#     dfFren.index, dfFren['Close'], 'y-',
# )

# # set axis
# ax = plt.gca()
# ax.xaxis.set_major_locator(mdates.MonthLocator(
#     interval=3
# ))
# ax.xaxis.set_major_formatter(mdates.DateFormatter(
#     '%b %y'
# ))

# plt.xlabel('Bulan')
# plt.ylabel('Rp')
# plt.xticks(rotation=65)
# plt.legend(['TLKM', 'ISAT', 'EXCL', 'FREN'])
# plt.show()

###============= Testing =================##

# print(dfTelkom.loc['2016']['Close']*0.0000701240)


#####=========== Saham Perusahaan Luar =============###
###============= Data Apple ===============###

dfApple = pd.read_csv(
    'sahamAAPL.csv',
    index_col=False,
    parse_dates=['Date']
    )

dfApple = dfApple.set_index('Date')
dfApple = dfApple.sort_index()


###============= Data Facebook ===============###

dfFacebook= pd.read_csv(
    'sahamFB.csv',
    index_col=False,
    parse_dates=['Date']
    )

dfFacebook = dfFacebook.set_index('Date')
dfFacebook = dfFacebook.sort_index()

# print(dfFacebook)

###============= Data Google ===============###

dfGoogle = pd.read_csv(
    'sahamGOOG.csv',
    index_col=False,
    parse_dates=['Date']
    )

dfGoogle = dfGoogle.set_index('Date')
dfGoogle = dfGoogle.sort_index()

# print(dfGoogle.describe())

###============= Data Microsoft ===============###

dfMicros = pd.read_csv(
    'sahamMSFT.csv',
    index_col=False,
    parse_dates=['Date']
    )

dfMicros = dfMicros.set_index('Date')
dfMicros = dfMicros.sort_index()

# print(dfMicros.describe())


###============= Data Currency ===============###
## Menggunakan Bank BCA
import requests

#Dollar jadi Rupiah = Dollar US * Harga Beli Bank
url = 'https://kurs.web.id/api/v1/bca'
data = requests.get(url)
dataBank = data.json()

hargaJual = int(dataBank['jual'])
hargaBeli = int(dataBank['beli'])
# print(hargaBeli)


x = dfMicros['Close']*hargaBeli

plt.plot(
    dfMicros.index, dfMicros['Close']*hargaBeli, 'r*',
    dfApple.index, dfApple['Close']*hargaBeli, 'g*',
    dfFacebook.index, dfFacebook['Close']*hargaBeli, 'y*',
    dfGoogle.index, dfGoogle['Close']*hargaBeli, 'b*',
    dfIndosat.index, dfIndosat['Close'], 'r.',
    dfXL.index, dfXL['Close'], 'g.',
    dfFren.index, dfFren['Close'], 'y.',
    dfTelkom.index, dfTelkom['Close'], 'b.',
)

# set axis
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.MonthLocator(
    interval=3
))
ax.xaxis.set_major_formatter(mdates.DateFormatter(
    '%b %y'
))

plt.xlabel('Bulan')
plt.ylabel('Rp')
plt.xticks(rotation=65)
plt.legend(['Microsoft', 'Apple', 'Facebook', 'Google', 'Indosat', 'XL', 'Fren', 'Telkomsel'])
plt.grid()
# plt.show()


#####======== Testing Plot Lain : Colorscale===========###
import plotly.graph_objects as go
import numpy as np

# fig = go.Figure(data=go.Scatter(
#     y = dfIndosat['Close'],
#     x = dfIndosat.index,
#     name='Indosat',
#     mode='markers',
#     marker=dict(
#         size=4,
#         color=np.random.randn(500), #set color equal to a variable
#         colorscale='Viridis', # one of plotly colorscales
#         showscale=True
#     )
# ))

# fig.add_trace(go.Scatter(
#     x=dfTelkom.index, y=dfTelkom['Close'],
#     name='Telkomsel',
#     mode='markers',
#     marker=dict(
#         size=4,
#         color=np.random.randn(500), #set color equal to a variable
#         colorscale='Viridis', # one of plotly colorscales
#         showscale=True
# )))

# fig.show()
######## ========================================= ###########

#Testing

fig = go.Figure(data=go.Scatter(
    y = dfIndosat['Close'],
    x = dfIndosat.index,
    name='Indosat',
    mode='lines+markers',
    marker=dict(
        size=4,
        color='blue', #set color equal to a variable
        # colorscale='Viridis', # one of plotly colorscales
        # showscale=True
    )
))

fig.add_trace(go.Scatter(
    x=dfTelkom.index, y=dfTelkom['Close'],
    name='Telkomsel',
    mode='lines+markers',
    marker=dict(
        size=4,
        color='red', #set color equal to a variable
        # colorscale='Viridis', # one of plotly colorscales
        # showscale=True
)))


fig.add_trace(go.Scatter(
    x=dfXL.index, y=dfXL['Close'],
    name='XL',
    mode='lines+markers',
    marker=dict(
        size=4,
        color='yellow', #set color equal to a variable
        # colorscale='Viridis', # one of plotly colorscales
        # showscale=True
)))


fig.add_trace(go.Scatter(
    x=dfFren.index, y=dfFren['Close'],
    name='Fren',
    mode='lines+markers',
    marker=dict(
        size=4,
        color='green', #set color equal to a variable
        # colorscale='Viridis', # one of plotly colorscales
        # showscale=True
)))

# fig.add_trace(go.Scatter(
#     x=dfApple.index, y=dfApple['Close']*hargaBeli,
#     name='Apple',
#     mode='lines+markers',
#     marker=dict(
#         size=4,
#         color='grey', #set color equal to a variable
#         # colorscale='Viridis', # one of plotly colorscales
#         # showscale=True
# )))


# fig.add_trace(go.Scatter(
#     x=dfMicros.index, y=dfMicros['Close']*hargaBeli,
#     name='Microsoft',
#     mode='lines+markers',
#     marker=dict(
#         size=4,
#         color='magenta', #set color equal to a variable
#         # colorscale='Viridis', # one of plotly colorscales
#         # showscale=True
# )))

# fig.add_trace(go.Scatter(
#     x=dfFacebook.index, y=dfFacebook['Close']*hargaBeli,
#     name='Facebook',
#     mode='lines+markers',
#     marker=dict(
#         size=4,
#         color='purple', #set color equal to a variable
#         # colorscale='Viridis', # one of plotly colorscales
#         # showscale=True
# )))

# fig.add_trace(go.Scatter(
#     x=dfGoogle.index, y=dfGoogle['Close']*hargaBeli,
#     name='Google',
#     mode='lines+markers',
#     marker=dict(
#         size=4,
#         color='orange', #set color equal to a variable
#         # colorscale='Viridis', # one of plotly colorscales
#         # showscale=True
# )))

fig.show()