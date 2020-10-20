from time import sleep
import socket
from rich.progress import track
__version__ = '0.0.1'
def do_step(set, time):
    sleep(time)
def auto_get_ProgressBar(time):
    for step in track(range(100)):
        do_step(step, time)
ip: str = input('IP: ')
porta = input('Porta: ')
ssh: str = input('localhost: ')
class main:
    def __init__(self):
        https: str = f'https://localhost:{porta}/{ssh}'
        auto_get_ProgressBar(0.1)
        print(f'SSH: Executando... {https}')
        print(f'Conectado ao servidor: {ip}')
if __name__ == '__main__':
    while True:
        try:
            main.__init__('main')
        except KeyboardInterrupt:
            break
        except:
            continue