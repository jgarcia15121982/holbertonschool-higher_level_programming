#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        my_tuple = ("None", )
        return len(my_tuple), my_tuple[0]
    my_tuple = (sentence)
    return len(my_tuple), my_tuple[0]
