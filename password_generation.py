import random

class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.__psw_chars = psw_chars
        self.__min_length = min_length
        self.__max_length = max_length

    def __call__(self, *args, **kwargs):
        new_psw = ''
        for i in range(random.randint(self.__min_length,self.__max_length)):
            new_psw += self.__psw_chars[random.randint(0,len(self.__psw_chars)-1)]

        return new_psw

min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"

rnd = RandomPassword(psw_chars, min_length, max_length)
lst_pass = [rnd() for i in range(3)]

