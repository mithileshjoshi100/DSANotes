def mygen():
    yield 'A'
    yield 'B'
    yield 'C'

g = mygen()
#print(next(g))
#print(next(g))
#print(next(g))
#print(next(g))
# lst = (x*x for x in range(10))
# print(lst)
# try:
#     while True:
#         print(next(lst))
# except:
#     print('Done')
import time
def counter(n:int):
    print('Counting start')
    while n>0:
        yield n
        n -= 1

c = counter(10)
for x in c:
    print(x)
    time.sleep(1)
