def generate(n):
    if n == 1 : 
        return ['()']
    strs = generate(n-1)
    for back in strs:
        a1 = '(' + back + ')'
        a2 = '()' + back 
        a3 = back + '()'
        print(a1,a2,a3)
    return [a1,a2,a3]

generate(3)