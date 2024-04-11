function debounce(func, delay) {
    let timeoutId;

    return (...args) => {
        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => {
            func(...args)
        }, delay);
    };
};

// Socket.io
const socket = io(),
    connected = document.getElementById('connected');

function heartbeat() {
    connected.textContent = socket.connected ? `Connected! (${socket.id})` : 'Disconnected';
    connected.setAttribute('style', socket.connected ? 'color: rgb(0, 166, 110)' : 'color: rgb(217, 53, 38)')
}

socket.on('connect', heartbeat);
setInterval(heartbeat, 1000);

const keyIndicators = Array.from(document.querySelectorAll('.keyboard article'))
    .reduce((object, element) => ({ ...object, [element.textContent.toLowerCase()]: element }), {});
const stateVisual = document.getElementById('state');

let keyboard = {};
const updateState = debounce(() => {
    // null instead of 0 allows the motors to coast instead of e-brake
    let state = { horizontal: [null, null], vertical: null };

    if (keyboard['q']) state.vertical = -1;
    else if (keyboard['e']) state.vertical = 1;

    if (keyboard['w']) state.horizontal = [1, 1];
    else if (keyboard['s']) state.horizontal = [-1, -1];
    if (keyboard['a']) state.horizontal = [-1, 1];
    else if (keyboard['d']) state.horizontal = [1, -1];

    socket.emit('drive', state);
    stateVisual.textContent = JSON.stringify(state);
}, 100);

document.addEventListener('keydown', (e) => {
    if (e.key in keyIndicators) {
        keyIndicators[e.key].style.backgroundColor = 'rgb(32, 96, 223)';
        keyboard[e.key] = true;
        updateState();
    }
});
document.addEventListener('keyup', (e) => {
    if (e.key in keyIndicators) {
        keyIndicators[e.key].style.backgroundColor = 'black';
        keyboard[e.key] = false;
        updateState();
    }
});
