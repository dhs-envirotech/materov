import time
from threading import Timer

from inputs import devices, get_key
from picamera2 import Picamera2, Preview

print(devices.keyboards)

# Camera
camera = Picamera2()
camera.start_preview(Preview.QTGL, x=100, y=100) 
camera.configure(camera.create_preview_configuration())
camera.set_controls({"FrameDurationLimits": (33333, 33333)})
camera.start()

# Handle Keyboard Input
def debounce(func, delay):
    def debounced(*args, **kwargs):
        debounced.last_call = time.time()

        def call_it():
            if time.time() - debounced.last_call >= delay:
                func(*args, **kwargs)

        if hasattr(debounced, 'timer'):
            debounced.timer.cancel()
        debounced.timer = Timer(delay, call_it)
        debounced.timer.start()

    return debounced

def update_motors():
    print(state)

handle_keyboard = debounce(update_motors, 0.1)
running = True
state = {}
while running:
    events = get_key()
    event = events[0]

    # For debug only just in case this is ever more than 1
    if len(events) > 1:
        print('Multiple events: ', events)

    if event.ev_type == 'Key':
        if event.code == 'KEY_0':
            running = False
            continue

        if event.code in ['KEY_W', 'KEY_A', 'KEY_S', 'KEY_D', 'KEY_Q', 'KEY_E', 'KEY_F']:
            state[event.code] = event.state
            handle_keyboard()

camera.stop()