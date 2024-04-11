# Setup

This is the code used to control the underwater ROV for the [MateROV](https://materovcompetition.org/) competeition.

## Usage
Let's assuming you are currently in the `~/materov` cloned directory

1. Create a Python virtual enviornment
```bash
python3 -m venv --system-site-packages venv
```
2. Source the local enviornment (You have to run this every time a new terminal session is created)
```bash
source venv/bin/activate
```
3. Install packages
```bash
pip3 install flask adafruit-circuitpython-motorkit
```
4. Run!
```bash
python3 main.py
```

## About

I used [Socket.IO](https://socket.io) and [PicoCSS](https://picocss.com) for this minimal project.

Colors are also from PicoCSS: https://picocss.com/docs/colors