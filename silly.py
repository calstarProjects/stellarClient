import keyboard

colors = {
    'red': 0,
    'blue': 0,
    'green': 0
}

y = None

while True:
    x = keyboard.read_event()

    if x.name == 'esc':
        break
    elif x.name == 'r':
        colors['red'] += 1
    elif x.name == 'b':
        colors['blue'] += 1
    elif x.name == 'g':
        colors['green'] += 1
    while not  keyboard.read_event().event_type == 'up':
        pass

print(colors)