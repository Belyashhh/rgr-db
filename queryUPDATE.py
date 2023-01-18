import psycopg2
import db

def updateTVchannel(newchannel, newbroadcast,channel):
    query = """UPDATE TVchannel 
                SET channel = %(newchannel)s, broadcast=%(newbroadcast)s 
                WHERE channel = %(channel)s ;"""
    d = {'newchannel': newchannel,
         'newbroadcast': newbroadcast,
         'channel': channel}
    return db.SQLQuery(query, d)


def updateOwnerChannel(newchannel, newOwner,channel):
    query = """UPDATE OwnerChannel 
                SET channel = %(newchannel)s, оwner=%(newOwner)s 
                WHERE channel = %(channel)s ;"""
    d = {'newchannel': newchannel,
         'newOwner': newOwner,
         'channel': channel}
    return db.SQLQuery(query, d)


def updateRating(nameProgram, newNameProgram, newchannel, rating):
    query = """UPDATE Rating 
                SET nameProgram = %(newNameProgram)s, channel = %(newchannel)s, rating=%(rating)s 
                WHERE nameProgram = %(nameProgram)s ;"""
    d = {'newNameProgram': newNameProgram,
         'newchannel': newchannel,
         'rating': rating,
         'nameProgram': nameProgram}
    return db.SQLQuery(query, d)


def updateTVProgram(nameProgram, newNameProgram, newchannel, director):
    query = """UPDATE TVProgram 
                SET nameProgram = %(newNameProgram)s, channel = %(newchannel)s, director=%(director)s 
                WHERE nameProgram = %(nameProgram)s ;"""
    d = {'newNameProgram': newNameProgram,
         'newchannel': newchannel,
         'director': director,
         'nameProgram': nameProgram}
    return db.SQLQuery(query, d)

def updateProgramRelease(nameProgram, releaseNumber, newNameProgram, newNumber, premiere):
    query = """UPDATE ProgramRelease 
                SET nameProgram = %(newNameProgram)s, releaseNumber = %(newNumber)s, premiere=%(premiere)s 
                WHERE nameProgram = %(nameProgram)s AND releaseNumber = %(releaseNumber)s;"""
    d = {'newNameProgram': newNameProgram,
         'newNumber': newNumber,
         'premiere': premiere,
         'nameProgram': nameProgram,
         'releaseNumber': releaseNumber}
    return db.SQLQuery(query, d)


def updatePeople(fullname, born, nameProgram, releaseNumber, newNameProgram, newNumber,newfullname, newborn):
    query = """UPDATE People 
                SET fullname = %(newfullname)s, 
                born = %(newborn)s, 
                nameProgram = %(newNameProgram)s, 
                releaseNumber = %(newNumber)s
                WHERE nameProgram = %(nameProgram)s AND releaseNumber = %(releaseNumber)
                AND fullname = %(fullname)s AND born = %(born)s;"""
    d = {'fullname': fullname,
         'born': born,
         'newfullname': newfullname,
         'newborn': newborn,
         'newNameProgram': newNameProgram,
         'newNumber': newNumber,
         'nameProgram': nameProgram,
         'releaseNumber': releaseNumber}
    return db.SQLQuery(query, d)


if __name__ == '__main__':
    print(updateTVchannel("тнт", "цифра","тнт"))
