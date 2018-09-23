from commandr import command, Run

@command('add')
def addition(argA, argB):
    """ <a> <b>
    Add one number to another

    Arguments:
        <item> First number
        <item> Second number
    """
    a = float(argA)
    b = float(argB)
    total = a + b
    print("%s + %s = %s" % (argA, argB, str(total)))

@command('substract')
def substract(argA, argB):
    """ <a> <b>
    Substract "b" from "a"

    Arguments:
        <item> First number
        <item> Second number
    """
    a = float(argA)
    b = float(argB)
    result = a - b
    print("%s - %s = %s" % (argA, argB, str(result)))

@command('times')
def time(argA, argB):
    """ <a> <b>
    Multiply "b" and "a"

    Arguments:
        <item> First number
        <item> Second number
    """
    a = float(argA)
    b = float(argB)
    result = a * b
    print("%s * %s = %s" % (argA, argB, str(result)))

@command('divide')
def divide(argA, argB):
    """ <a> <b>
    Divide "a" / "b"

    Arguments:
        <item> First number
        <item> Second number
    """
    a = float(argA)
    b = float(argB)
    result = a / b
    print("%s / %s = %s" % (argA, argB, str(result)))

@command('pow')
def pow(argA, argB):
    """ <a> <b>
    Power - "a" **"b"

    Arguments:
        <item> First number
        <item> Second number
    """
    a = float(argA)
    b = float(argB)
    result = a ** b
    print("%s ^ %s = %s" % (argA, argB, str(result)))

if __name__ == '__main__':
    Run()
