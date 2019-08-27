
import sys 

def fn(n):
    for i in range(n):
        print('step {0}'.format(i))
        yield

f = fn(10)
while True:
    try:
        next(f)
    except:
        sys.exit()

