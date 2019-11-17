import time

def running(trainimage):
    for i in range(100):
        #print('\r', i * ' ', 'TRAIN', (100 - i) * ' ', end='\n', flush=False)
        #print('\r', i * ' ', 'TRAIN 2', (100 - i) * ' ', end='\n', flush=False)
        #print('\r', i * ' ', 'newline', (100 - i) * ' ', end=2 * '\033[F', flush=False)
        print('\r', i * ' ', trainimage.split('\n', 2)[0], (100 - i) * ' ', end='\n', flush=False)
        print('\r', i * ' ', trainimage.split('\n', 2)[1], (100 - i) * ' ', end='\n', flush=False)
        print('\r', i * ' ', trainimage.split('\n', 2)[2], (100 - i) * ' ', end=2 * '\033[F', flush=False)
        time.sleep(0.1)


trainimage = '  ____  ____  ____  ____  ____\n /   |-|   |-|   |-|   |-|    \ \n  <____  ____  ____  ____  ____>'

running(trainimage)

#print(trainimage.split('\n', 2))
