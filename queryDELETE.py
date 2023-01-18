import psycopg2
import db


def deleteTVchannel(channel):
    query = """DELETE FROM  TVchannel 
                WHERE channel = %(channel)s ;"""
    d = {'channel': channel}
    return db.SQLQuery(query, d)


def deleteOwnerChannel(channel):
    query = """DELETE FROM  OwnerChannel 
                WHERE channel = %(channel)s ;"""
    d = {'channel': channel}
    return db.SQLQuery(query, d)


def deleteRating(nameProgram):
    query = """DELETE FROM  Rating 
                WHERE nameProgram = %(nameProgram)s ;"""
    d = {'nameProgram': nameProgram}
    return db.SQLQuery(query, d)


def deleteTVProgram(nameProgram):
    query = """DELETE FROM  TVProgram 
                WHERE nameProgram = %(nameProgram)s ;"""
    d = {'nameProgram': nameProgram}
    return db.SQLQuery(query, d)


def deleteProgramRelease(nameProgram, releaseNumber):
    query = """DELETE FROM  ProgramRelease 
                WHERE nameProgram = %(nameProgram)s AND releaseNumber = %(releaseNumber)s ;"""
    d = {'nameProgram': nameProgram,
         'releaseNumber': releaseNumber}
    return db.SQLQuery(query, d)


def deletePeople(fullname, born, nameProgram, releaseNumber):
    query = """DELETE FROM People 
                WHERE nameProgram = %(nameProgram)s AND releaseNumber = %(releaseNumber)
                AND fullname = %(fullname)s AND born = %(born)s;"""
    d = {'fullname': fullname,
         'born': born,
         'nameProgram': nameProgram,
         'releaseNumber': releaseNumber}
    return db.SQLQuery(query, d)


if __name__ == '__main__':
    pass
