#!/usr/bin/env python2"
# -*- coding: utf-8 -*-


class MusicConverter:
    """
    This class contains all functions for the note conversion
    """
    def __init__(self):
        """
        Here I init all note and bonus lists
        """
        self.italianNote = ["do", "do#", "re", "re#", "mi", "fa", "fa#", "sol", "sol#", "la", "la#", "si"]
        self.englishNote = ["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b"]

        self.italianNoteF = ["do", "reb", "re", "mib", "mi", "fa", "solb", "sol", "lab", "la", "sib", "si"]
        self.englishNoteF = ["c", "cb", "d", "db", "e", "f", "gb", "g", "ab", "a", "bb", "b"]

        self.bonusList = ["m", "-", "+", "2", "4", "5", "6", "7"]

    def get_note_list(self, note_string):
        notelist = note_string.split(" ")
        newlist = []
        for f in notelist:
            try:
                if "/" in f:
                    newlist.append(f.split("/")[0])
                    newlist.append("/")
                    newlist.append(f.split("/")[1])
                elif "(" in f:
                    newlist.append(f.split("(")[0])
                    newlist.append("(")
                    newlist.append(f.split("(")[1])
                elif ")" in f:
                    newlist.append(f.split(")")[0])
                    newlist.append(")")
                    newlist.append(f.split(")")[1])
                else:
                    newlist.append(f)
            except:
                newlist.append(f)

        return newlist

    def convert_f_to_s(self, note):
        """
        This funciont take a note and convert it into sharp
        :param note:
        Note is a single string that must contain a note
        :return:
        If note is already sharp return note, else return converted note into sharp
        """

        bonus = ""
        mynote = note

        if self.is_sharp(mynote):
            return mynote

        else:
            mynote,bonus = self.get_bonus(mynote)
            if mynote in self.italianNoteF:
                index = self.italianNoteF.index(mynote)
                return self.italianNote[index] + bonus

            elif mynote in self.englishNoteF:
                index = self.englishNoteF.index(mynote)
                return self.englishNote[index] + bonus
            else:
                return note

    def convert_s_to_f(self, note):
        """
        This funciont take a note and convert it into flat
        :param note:
        Note is a single string that must contain a note
        :return:
        If note is already flat return note, else return converted note into flat
        """
        bonus = ""
        mynote = note

        if not self.is_sharp(mynote):
            return mynote

        else:
            mynote, bonus = self.get_bonus(mynote)
            if mynote in self.italianNote:
                index = self.italianNotF.index(mynote)
                return self.italianNoteF[index] + bonus

            elif mynote in self.englishNote:
                index = self.englishNote.index(mynote)
                return self.englishNoteF[index] + bonus
            else:
                return note

    def convert_italian_to_english(self, note):
        """
        This funciont take a note and convert it into english notation
        :param note:
        Note is a single string that must contain a note
        :return:
        If note is already in english notation return note, else return converted note into english notation
        """
        mynote = note
        bonus = ""

        if not self.is_italian(mynote):
            return note

        mynote, bonus = self.get_bonus(mynote)

        if not self.is_italian(mynote):
            return note

        if mynote in self.italianNote:
            index = self.italianNote.index(mynote)
            return self.englishNote[index] + bonus
        elif mynote in self.italianNoteF:
            index = self.italianNoteF.index(mynote)
            return self.englishNoteF[index] + bonus
        else:
            return note

    def convert_english_to_italian(self, note):
        """
        This funciont take a note and convert it into italian notation
        :param note:
        Note is a single string that must contain a note
        :return:
        If note is already in italian notation return note, else return converted note into italian notation
        """
        mynote = note
        bonus = ""

        if self.is_italian(mynote):
            return note

        mynote, bonus = self.get_bonus(mynote)

        if self.is_italian(mynote):
            return note

        if mynote in self.englishNote:
            index = self.englishNote.index(mynote)
            return self.italianNote[index] + bonus
        elif mynote in self.englishNoteF:
            index = self.englishNoteF.index(mynote)
            return self.italianNoteF[index] + bonus
        else:
            return note

    def get_first_note(self, listline):
        """
        This funcion analyze a list of note and spaces and get the first note into it
        :param listline:
        listline must be a list that contain spaces and notes
        :return:
        if there are not notes return None, else return the first note find
        """
        listline = [x.lower() for x in listline]


        for f in listline:
            mynote,bonus = self.get_bonus(f)

            if mynote in self.italianNote or mynote in self.englishNote or \
                    mynote in self.italianNoteF or mynote in self.englishNoteF:
                return mynote + bonus

    def is_note_line(self, line):
        """
        This function verify if one text line contains or not notes
        :param line:
        line must be a string that contain a note-list
        :return:
        if line is a notes line return true, else return false
        """
        line = line.lower()

        if line == "" or line == " ":
            return False

        isnote = False
        notes = 0
        notnotes = 0
        linelist = line.split(" ")
        i = 0
        while i < len(linelist):
            if linelist[i] != "":
                mynote = ""
                try:
                    find = False
                    if len(linelist[i]) >= 2:
                        if linelist[i][-1] == "#" or linelist[i][-1] == "b" or linelist[i][-1] in self.bonusList:
                            mynote = linelist[i][:-1]
                            find = True

                    if len(linelist[i]) >= 3:
                        if linelist[i][-2] == "#" or linelist[i][-2] == "b" or linelist[i][-2] in self.bonusList:
                            mynote = linelist[i][:-2]
                            find = True

                    if not find:
                        mynote = linelist[i]

                    if mynote in self.italianNote or mynote in self.englishNote:
                        notes += 1
                    else:
                        notnotes += 1
                except Exception:
                    pass
                    # do nothing
            i += 1
        if notes >= notnotes:
            isnote = True

        return isnote

    def find_modifier(self, note, finalnote):
        """
        This function get two notes, get the index of the notes, and get the tone difference
        :param note:
        :param finalnote:
        :return:
        if note and finalnote are the same, the function return 0, else return the tone difference between the two notes
        """
        tone = 0.00
        note = note.lower()
        finalnote = finalnote.lower()

        note = self.convert_english_to_italian(self.convert_f_to_s(note))
        finalnote = self.convert_english_to_italian(self.convert_f_to_s(finalnote))

        note, bonus1 = self.get_bonus(note)
        finalnote, bonus2 = self.get_bonus(finalnote)

        if note in self.italianNote and finalnote in self.italianNote:
            if note == finalnote:
                return tone
            else:
                currentindex = self.italianNote.index(note)
                final_index = self.italianNote.index(finalnote)

                print("current note index: " + str(currentindex))
                print("final note index: " + str(final_index))

                while currentindex != final_index:
                    if currentindex == 11:
                        currentindex = 0
                        tone += 1
                    else:
                        tone += 1
                        currentindex += 1
        return float(tone / 2.0)

    def convert(self, note, modifier):
        """
        This funcion modify a note into another from a modifier
        :param note:
        must be a string contains note to modify
        :param modifier:
        must be a float (if i remember great) that is the "tone modifier"
        :return:
        return the modified note
        for example, if mote is 'do', and modifier is 1.5
        the return value is 're#' --> 'do' + 1.5 tones (3 semitones) = 're#'
        """

        nofiteraction = int(modifier * 2)
        bonus = ""
        mynote = ""

        mynote,bonus = self.get_bonus(note)

        if mynote in self.italianNote:
            index = self.italianNote.index(mynote)

            maxindex = len(self.italianNote) - 1

            while nofiteraction != 0:
                if index == maxindex:
                    index = 0
                else:
                    index += 1
                nofiteraction -= 1

            return self.italianNote[index] + bonus

        elif mynote in self.englishNote:
            index = self.englishNote.index(mynote)

            maxindex = len(self.englishNote) - 1

            while nofiteraction != 0:
                if index == maxindex:
                    index = 0
                else:
                    index += 1
                nofiteraction -= 1

            return self.englishNote[index] + bonus

        else:
            return mynote + bonus

    def convert_list_into_italian_notation(self, notelist):
        notelist = [x.lower() for x in notelist]

        newlist = []
        for l in notelist:
            try:
                newlist.append(self.convert_english_to_italian(l))
                #newlist.append(" ")
            except Exception:
                newlist.append(l)
                #newlist.append(" ")

        return newlist

        return newlist

    def convert_list_into_english_notation(self, notelist):
        notelist = [x.lower() for x in notelist]

        newlist = []
        for l in notelist:
            try:
                newlist.append(self.convert_italian_to_english(l))
                #newlist.append(" ")
            except Exception:
                newlist.append(l)
                #newlist.append(" ")

        return newlist

    def convert_list_into_sharp(self, notelist):
        notelist = [x.lower() for x in notelist]

        newlist = []
        for l in notelist:
            try:
                newlist.append(self.convert_f_to_s(l))
                # newlist.append(" ")
            except Exception:
                newlist.append(l)
                # newlist.append(" ")

        return newlist

    def convert_list_into_flat(self, notelist):
        notelist = [x.lower() for x in notelist]

        newlist = []
        for l in notelist:
            try:
                newlist.append(self.convert_s_to_f(l))
                # newlist.append(" ")
            except Exception:
                newlist.append(l)
                # newlist.append(" ")

        return newlist

    def get_bonus(self, note):
        mynote = note
        bonus = ""
        count = 0

        # I control if note is italian on english notation
        if self.is_italian(note):
            notelist = self.italianNote
        else:
            notelist = self.englishNote

        while count < len(notelist):
            try:
                if note[0: len(notelist[count])] == notelist[count]:
                    mynote = note[0: len(notelist[count])]
                    bonus = note[len(notelist[count]):]

                    # if in bonus there is sharp or float, i put it in note string
                    if bonus[0] == "#":
                        mynote += "#"
                        bonus = bonus[1:]
                    if bonus[0] == "b":
                        mynote += "b"
                        bonus = bonus[1:]
                    break
                else:
                    count +=1
            except:
                count += 1

        return [mynote, bonus]

    def is_italian(self, note):
        if note in self.italianNote or note in self.italianNoteF:
            return True
        else:
            mynote = note
            bonus = ""
            count = 0
            notelist = self.italianNote

            while count < len(notelist):
                try:
                    if note[0: len(notelist[count])] == notelist[count]:
                        mynote = note[0: len(notelist[count])]
                        bonus = note[len(notelist[count]):]

                        # if in bonus there is sharp or float, i put it in note string
                        if bonus[0] == "#":
                            mynote += "#"
                            bonus = bonus[1:]
                        if bonus[0] == "b":
                            mynote += "b"
                            bonus = bonus[1:]
                        break
                    else:
                        count += 1
                except:
                    count += 1

            if mynote in self.italianNote or mynote in self.italianNoteF:
                return True

            return False

    def is_sharp(self,note):
        if "#" in note:
            return True
        return False

    def pack(self, list_line):
        line = ""
        count = 0
        while count < len(list_line):
            if list_line[count] == "/" and list_line[count -1] == " " and list_line[count +1] == " ":
                try:
                    line = line[:-1]
                    line += "/"
                    count +=1
                except:
                    pass

            elif list_line[count] == "(" and list_line[count -1] == " " and list_line[count +1] == " ":
                try:
                    line = line[:-1]
                    line += "("
                    count +=1
                except:
                    pass
            elif list_line[count] == ")" and list_line[count - 1] == " " and list_line[count + 1] == " ":
                try:
                    line = line[:-1]
                    line += ")"
                    count += 1
                except:
                    pass
            else:
                line += list_line[count]
            count += 1
        return line
