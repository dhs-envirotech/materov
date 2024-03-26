from inputs import devices, get_key
from picamera2 import Picamera2, Preview

print(devices.keyboards);

picam2 = Picamera2()
picam2.start_preview(Preview.QTGL, x=100, y=100) 
picam2.configure(picam2.create_preview_configuration())
picam2.set_controls({"FrameDurationLimits": (33333, 33333)})

picam2.start()
running = True
state = {}
while running:
    event = get_key()[0]
    if event.ev_type == 'Key':
        if event.code == 'KEY_0':
            running = False
        state[event.code] = event.state
        print(state)

picam2.stop()