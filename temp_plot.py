#! /usr/bin/env python
import datetime
import matplotlib
matplotlib.use("Agg")
import matplotlib.pylab as plt
import pandas as pd
import numpy as np
import matplotlib.dates as mdates
from matplotlib.dates import AutoDateFormatter, AutoDateLocator

plt.close()

data = pd.read_fwf('teplota.log',header=None,names=['time','amount'],widths=[27,5])
data.time = pd.to_datetime(data['time'], format='%Y-%m-%d %H:%M:%S.%f')

fig, ax = plt.subplots()


datemax = data.time.tail(1)
datemin = datemax - datetime.timedelta(days=2)
ax.set_xlim(datemin.item(), datemax.item())

print 'datemax.item(): ',datemax.item()
# format the coords message box
def price(x):
    return '$%1.2f' % x
ax.format_xdata = mdates.DateFormatter('%Y-%m-%d %H:%M:%S')
ax.format_ydata = price
ax.grid(True)
ax.set_ylabel('Temperature ($^\circ$C)')
ax.set_xlabel(datemin.item())



# Sets the tick labels diagonal
fig.autofmt_xdate()

plt.plot(data.time,data.amount)
plt.savefig("testgraph.png")
