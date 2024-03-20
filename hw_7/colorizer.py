class Colorizer:
    COLORS = {
        'default': '\033[0m',
        'red': '\033[91m',
        'grey': '\033[90m',
        'yellow': '\033[93m',
        'green': '\033[92m',
        'blue': '\033[94m',
    }

    def __init__(self, color):
        self.color = color

    def __enter__(self):
        if self.color in self.COLORS:
            print(self.COLORS[self.color], end='')

    def __exit__(self, exc_type, exc_value, traceback):
        print(self.COLORS['default'], end='')


with Colorizer('blue'):
    print('printed in blue')

print('\033[93m', end='')
print('aaa')
print('bbb')
print('\033[0m', end='')
print('ccc')
