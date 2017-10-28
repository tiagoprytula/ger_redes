import time

#pooling for 1s

x=0
while 1:
    start_time = time.time() * 1000.0
    elapsed_time = time.time() * 1000.0 - start_time
    while elapsed_time <= 1000:
            elapsed_time = time.time() * 1000.0 - start_time
    x+=1
    print(x)
