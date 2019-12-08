import time
import sys

def way(direction, length):
    if direction == 'l':
        dir_path = reversed(range(length))
    else:
        dir_path = range(length)
    return length

def running(image):
    imageheight = len(image)
    #for i in range(100):

    # if len(sys.argv) > 1:
    #     if str(sys.argv[1]) == '-l':
    #         length = way(str(sys.argv[1][-1], 100))
    for i in range(length):
        for j in range(imageheight - 1):
            print('\r', i * ' ', image[j], (100 - i) * ' ', end='', flush=False)
        print('\r', i * ' ', image[-1], (100 - i) * ' ', end=((imageheight) * '\033[F'), flush=False)
        time.sleep(0.1)

vehicle_type = 'train\n'

with open('vehicles') as f:
    image_in = f.readlines()

for ar in sys.argv:
    if ar == '-l' or ar == ' l':
        length = way(str(sys.argv[1][-1], 100))
    else:
        length = way(str('right'), 100)
    if ar in image_in:
        vehicle_type = str(ar) + '\n'




# if len(sys.argv) > 1:
#     if str(sys.argv[1]) == '-l':
#         length = way(str(sys.argv[1][-1], 100))
#     else:
#         length = way(str(sys.argv[1][-1], 100))

# vehicle_type = str(sys.argv[1]) + '\n'


start_vehicle = image_in.index(vehicle_type)
end_vehicle = image_in[start_vehicle:].index(50 * '#' + '\n')

image_out = image_in[(start_vehicle + 1):(start_vehicle + end_vehicle)]

running(image_out)
