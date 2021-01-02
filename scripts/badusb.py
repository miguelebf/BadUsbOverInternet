'''
Script que funciona como servidor a la espera de conexiones
de los badusb y envia duckyscripts para ser ejecutados.
'''

import logging

logging.basicConfig(
    level=DEBUG,
    filename='badusb_over_internet.log',
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S'
)
