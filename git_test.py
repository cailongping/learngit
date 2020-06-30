import time 
def test():
    print(time.asctime())

    return {'time':time.localtime()}

t=test()
print(t)
print('hello git')
print('hello world')
