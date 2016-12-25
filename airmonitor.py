#!/usr/bin/env python

import datetime

import hidapi

import matplotlib.animation as animation
import matplotlib.dates as mdates
import matplotlib.pyplot as plt


seq1 = 0x0001
seq2 = 0x0001
    
def tx_type1(handle, msg):
    msg = bytes('@{:04X}{}\n@@@@@@@@@@'.format(0x0001, msg), 'utf-8')
    hidapi.hid_write(handle, msg)

def tx_type2(handle, msg):
    msg = bytes('@', 'utf-8') + seq2.to_bytes(1, byteorder='big') + bytes('{}\n@@@@@@@@@@@@@'.format(msg), 'utf-8')
    hidapi.hid_write(handle, msg)

def rx(handle, numBytes=0x10):
    return hidapi.hid_read_timeout(handle, numBytes, 1000)

def getPpm(handle):
    tx_type2(handle, '*TR')
    return int.from_bytes(rx(handle)[2:4], byteorder='little')


# Setup Device
hidapi.hid_init()
for dev in hidapi.hid_enumerate(vendor_id=0x03eb, product_id=0x2013):
    handle = hidapi.hid_open_path(dev.path) 

print('reading info from device')
tx_type1(handle, '*IDN?')
info = rx(handle) + rx(handle) + rx(handle) + rx(handle) + rx(handle) + rx(handle) + rx(handle)
print('ret:"' + str(info) + '"')


# Setup Chart
data_x = []
data_y = []

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

def fechAndDraw(i):
    # read and update dataset
    ppm = getPpm(handle)
    data_x.append(datetime.datetime.now())
    data_y.append(ppm)

    # redraw chart
    ax.clear()
    ax.set_title('Air Quality')
    ax.set_xlabel('Time')
    ax.set_ylabel('[ppm]')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    ax.plot_date(data_x, data_y, 'r-')
    
anim = animation.FuncAnimation(fig, fechAndDraw, interval=2000)
plt.show()    
