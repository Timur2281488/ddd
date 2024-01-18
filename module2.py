v1=int(input('Введите начальную скорость '))
v2=int(input('Введите конечную скорость '))
t=int(input('Введите время '))
a=
def distance(boost):
    s=0
    def wrapper():
        boost()
        s=v1*t+a*t
        print(s)
    return wrapper

def boost():
    a=(v2-v1)/t
    print(a)
    return(a)

boost=distance(boost)

boost()