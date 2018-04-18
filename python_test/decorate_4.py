def makebold(fn):
    def wrapper():
        return "<b>" + fn() + "</b>"
    return wrapper

def makeitalic(fn):
    def wrapper():
        return "<i>" + fn() + "</i>"
    return wrapper

@makebold
@makeitalic
def say():
    return "hello"

print(say())