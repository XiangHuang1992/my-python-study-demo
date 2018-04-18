# -*- coding: utf-8 -*-

def my_shiny_new_decorator(a_function_to_decorate):
    def the_warpper_around_the_orginal_function():
        print('before the func runs')

        a_function_to_decorate()

        print('after the func runs')

    return the_warpper_around_the_orginal_function

def a_stand_alone_function():
    print("i am a stand alone funcation, don't dare modity me! ")

a_stand_alone_function()


a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function)

#a_stand_alone_function_decorated()

a_stand_alone_function = my_shiny_new_decorator(a_stand_alone_function)

a_stand_alone_function()



@my_shiny_new_decorator
def another_stand_alone_function():
    print('leave me alone')

another_stand_alone_function()
