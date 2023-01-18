import psycopg2
import db


def insertTVchannel(channelName, channelBroadcast):
    query = """INSERT INTO TVchannel(channel, broadcast) 
            VALUES(%(channel)s, %(broadcast)s);"""
    d = {'channel': channelName, 'broadcast': channelBroadcast}
    return db.SQLQuery(query, d)


def insertOwnerChannel(channelName, channeOwner):
    query = """INSERT INTO OwnerChannel(channel, owner) 
            VALUES(%(channel)s, %(owner)s);"""
    d = {'channel': channelName, 'owner': channeOwner}
    return db.SQLQuery(query, d)


def insertRating(Program, channelName, ProgramRating):
    query = """INSERT INTO Rating(nameProgram, channel, rating) 
            VALUES(%(nameProgram)s,%(channel)s, %(rating)s);"""
    d = {'nameProgram': Program,
         'channel': channelName,
         'rating': ProgramRating}
    return db.SQLQuery(query, d)


def insertTVProgram(nameProgram, channel, director):
    query = """INSERT INTO TVProgram(nameProgram, channel, director) 
            VALUES(%(nameProgram)s,%(channel)s, %(director)s)"""
    d = {'nameProgram': nameProgram,
         'channel': channel,
         'director': director}
    return db.SQLQuery(query, d)


def insertProgramRelease(nameProgram, releaseNumber, premiere):
    query = """INSERT INTO ProgramRelease(nameProgram, releaseNumber, premiere) 
            VALUES(%(nameProgram)s,%(releaseNumber)s, %(premiere)s);"""
    d = {'nameProgram': nameProgram,
         'releaseNumber': releaseNumber,
         'premiere': premiere}
    return db.SQLQuery(query, d)


def insertPeople(fullname, born, nameProgram, releaseNumber):
    query = """INSERT INTO People(fullname, born, nameProgram, releaseNumber) 
            VALUES(%(fullname)s, %(born)s, %(nameProgram)s,%(releaseNumber)s);"""
    d = {'fullname': fullname,
         'born': born,
         'nameProgram': nameProgram,
         'releaseNumber': releaseNumber}
    return db.SQLQuery(query, d)



if __name__ == '__main__':
    # print(insertTVchannel("карусель", "цифа"))
    # print(insertOwnerChannel("карусель", "ВГТРК"))
    print(insertRating("мультики2", "карусель", 10))
    print(insertTVProgram("мультики2", "карусель", "чел1"))
    # print(insertProgramRelease("мультики", "123", "01.01.2021"))
    # print(insertPeople("чел","01.01.2001","мультики","123"))

