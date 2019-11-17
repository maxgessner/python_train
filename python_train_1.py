import time
import sys


def running(image):
    imageheight = len(image)
    for i in range(100):
        for j in range(imageheight - 1):
            print('\r', i * ' ', image[j], (100 - i) * ' ', end='', flush=False)
        print('\r', i * ' ', image[-1], (100 - i) * ' ', end=((imageheight) * '\033[F'), flush=False)
        time.sleep(0.1)


with open('vehicles') as f:
    image_in = f.readlines()

vehicle_type = 'train\n'

if len(sys.argv) > 1:
    vehicle_type = str(sys.argv[1]) + '\n'

start_vehicle = image_in.index(vehicle_type)
end_vehicle = image_in[start_vehicle:].index(50 * '#' + '\n')

image_out = image_in[(start_vehicle + 1):(start_vehicle + end_vehicle)]

running(image_out)
