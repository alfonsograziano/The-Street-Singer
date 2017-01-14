#!/usr/bin/env python
# -*- coding: utf-8 -*-


class SharedPreferences():
    def __init__(self, filename):
        self.filename = filename

    def getDataFromName(self, name):
        text_list = []
        with open(self.filename) as f:
            text_list = f.read().splitlines()

        for f in text_list:
            try:
                if f.split(":")[0] == name:
                    return f.split(":")[1]
            except:
                pass
        return False

    def setDataFromName(self, name, data):
        new_list = []
        text = ""
        with open(self.filename) as f:
            text_list = f.read().splitlines()

        for f in text_list:
            try:
                if f.split(":")[0] == name:
                    new_list.append(f.split(":")[0] + ":" + data)
                else:
                    new_list.append(f)
            except:
                pass

        for i in new_list:
            text += i + "\n"

        with open(self.filename, "w") as f:
            f.write(text)