
## PROGRAMA QUE CALCULA RECURSIVAMENTE EL MCD ENTRE 2 NÚMEROS ##

def maxdiv(a,b):

    if a==b:
        return a
    elif a<b:
        return maxdiv(a,b-a)
    elif a>b:
        return maxdiv(a-b,b)


print(maxdiv(33,330))
