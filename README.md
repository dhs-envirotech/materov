# Setup

This is the code used to control the underwater ROV for the [MateROV](https://materovcompetition.org/) competeition.

## Usage
Let's assuming you are currently in the `~/materov` cloned directory

1. Create a Python virtual enviornment
```bash
python3 -m venv --system-site-packages .venv
```
2. Source the local enviornment (You have to run this every time a new terminal session is created)
```bash
source .venv/bin/activate
```
3. Install packages
```bash
pip3 install inputs adafruit-circuitpython-motorkit
```
