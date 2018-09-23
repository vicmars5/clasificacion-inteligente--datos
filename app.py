from commandr import command, Run

@command('add')
def addition(argA, argB):
    a = float(argA)
    b = float(argB)
    total = a + b
    print("%s + %s = %s" % (argA, argB, str(total)))

@command('substract')
def substract(argA, argB):
    a = float(argA)
    b = float(argB)
    result = a - b
    print("%s - %s = %s" % (argA, argB, str(result)))

@command('times')
def time(argA, argB):
    a = float(argA)
    b = float(argB)
    result = a * b
    print("%s * %s = %s" % (argA, argB, str(result)))

@command('divide')
def divide(argA, argB):
    a = float(argA)
    b = float(argB)
    result = a / b
    print("%s / %s = %s" % (argA, argB, str(result)))

@command('pow')
def pow(argA, argB):
    a = float(argA)
    b = float(argB)
    result = a ** b
    print("%s ^ %s = %s" % (argA, argB, str(result)))

if __name__ == '__main__':
    Run()
