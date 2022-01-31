#!/usr/bin/python3
class MyInt(int):
    def __eq__(self, dif):
        return int(self) != dif

    def __ne__(self, dif):
        return int(self) == dif
