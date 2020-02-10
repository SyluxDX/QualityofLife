import hashlib
from datetime import datetime

RUNTIME = datetime.now().strftime('%Y%m%d%H%M%S')

def progress_bar(step, total, size=20):
    """ Print a progress bar to console """
    percentage = (step/total)
    fill = int(percentage*size)
    blank = size-fill
    line = '[{}{}] {}%'.format('='*fill, ' '*blank, int(percentage*100))
    print('\r{}'.format(line), end='', flush=True)
    if fill == size:
        print()

def generate_guid(data, use_runtime=True):
    """ Generate guid using runtime timestamp and data

        Returns string with guid. """
    if use_runtime:
        line = RUNTIME+data
    else:
        line = data
    guid = hashlib.md5(line.encode())
    return guid.hexdigest()
