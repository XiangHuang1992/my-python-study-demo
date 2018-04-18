# -*- coding: utf-8 -*-

def shot(world='yes'):
    return world.capitalize() + '!'

print(shot())

screm = shot
print(screm)

del shot

try:
    print(shot)
except NameError as e:
    print(e)

print(screm())


def getTalk(kind='shot'):
    def whisper(world='yes'):
        return world.lower() + '...'

    print(whisper())

getTalk()

try:
    print(whisper())
except NameError as e:
    print(e)

def talk(kind='shot'):
    def shot(world='yes'):
        return world.capitalize() + '!'
    def whisper(world='yes'):
        return world.lower() + '...'

    if kind == 'shot':
        return shot
    else:
        return whisper
gTalk = talk()

print(gTalk())

print(gTalk)
