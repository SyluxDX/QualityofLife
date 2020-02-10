from quality import progress_bar
from random import random
from time import sleep

total = 2400

for x in range(total):
    aux = random()
    if aux < 0.1:
        sleep(0.05)
    if aux > 0.9:
        sleep(0.5)
    progress_bar(x+1, total, 50)
