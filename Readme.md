# Python AirSensor/AirMonitor

This is a project to display data from an iAQ Stick with python on Mac OS.

![python-airmonitor screenshot](https://github.com/uvwxy/python-airmonitor/raw/master/airmonitor.png "python-airmonitor Screenshot")

## Usage
To show the airmonitor run the python3 script. To make sure you have the dependencies installed, see below.

```
python3 airmonitor.py
```

### Dependencies
- [Python 3](https://www.python.org/downloads/)
- [hidapi](https://github.com/NF6X/pyhidapi)
- [matplotlib](http://matplotlib.org/)

On Mac OS this is what I did:

```
brew install python3
pip3 install hidapi
pip3 install matplotlib
```

### Details
The 'complicated stuff' on how to communicate with the sensor I took from [here](https://github.com/mknx/smarthome/blob/develop/plugins/iaqstick/__init__.py).




