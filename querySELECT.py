import psycopg2
import db


def selectTVchannel():
    query = "SELECT * FROM TVchannel;"
    return db.SQLQuery(query)


def selectOwnerChannel():
    query = "SELECT * FROM OwnerChannel;"
    return db.SQLQuery(query)


def selectRating():
    query = "SELECT * FROM Rating;"
    return db.SQLQuery(query)


def selectTVProgram():
    query = "SELECT * FROM TVProgram;"
    return db.SQLQuery(query)


def selectProgramRelease():
    query = "SELECT * FROM ProgramRelease;"
    return db.SQLQuery(query)


def selectPeople():
    query = "SELECT * FROM People;"
    return db.SQLQuery(query)


def selectKeyTVchannel(channel):
    query = "SELECT * FROM TVchannel WHERE channel = %(channel)s ;"
    d = {'channel': channel}
    return db.SQLQuery(query, d)


def selectKeyOwnerChannel(channel):
    query = "SELECT * FROM OwnerChannel WHERE channel = %(channel)s ;"
    d = {'channel': channel}
    return db.SQLQuery(query, d)


def selectKeyRating(nameProgram):
    query = "SELECT * FROM Rating WHERE nameProgram = %(nameProgram)s ;"
    d = {'nameProgram': nameProgram}
    return db.SQLQuery(query, d)


def selectKeyTVProgram(nameProgram):
    query = "SELECT * FROM TVProgram WHERE nameProgram = %(nameProgram)s ;"
    d = {'nameProgram': nameProgram}
    return db.SQLQuery(query, d)


def selectKeyProgramRelease(nameProgram, releaseNumber):
    query = """SELECT * FROM ProgramRelease 
    WHERE nameProgram = %(nameProgram)s AND  releaseNumber = %(releaseNumber)s;"""
    d = {'nameProgram': nameProgram,
         'releaseNumber': releaseNumber}
    return db.SQLQuery(query, d)


def selectKeyPeopleProgram(nameProgram, releaseNumber):
    query = "SELECT * FROM People WHERE nameProgram = %(nameProgram)s AND  releaseNumber = %(releaseNumber)s;"
    d = {'nameProgram': nameProgram,
         'releaseNumber': releaseNumber}
    return db.SQLQuery(query, d)


def selectKeyPeopleName(fullname, born):
    query = "SELECT * FROM People WHERE fullname = %(fullname)s AND  born = %(born)s;"
    d = {'fullname': fullname,
         'born': born}
    return db.SQLQuery(query, d)


if __name__ == '__main__':
    print(selectKeyTVchannel("стс"))
    print(selectTVchannel())
    print(selectOwnerChannel())
    print(selectRating())
    print(selectTVProgram())
    print(selectProgramRelease())
    print(selectPeople())