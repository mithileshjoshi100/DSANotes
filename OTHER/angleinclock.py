'''
Angle made by minute and hour hand in a clock
'''

# input t -> 01:30


def Integer(s:str)->int:
    if s[0] == '0':
        s = s[1:]
    return int(s)

def angle(t:str)-> float:
    h,m = map(Integer,t.split(':'))
    # aprox ans
    ah = h*30 + (m/60)*30
    am = m*6
    print(am-ah)

angle('01:07')