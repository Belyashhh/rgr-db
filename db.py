import psycopg2

parametrs = {
    'host': '192.168.0.22',
    'port': '5432',
    'user': 'admin1',
    'password': 'admin12',
    'db': 'testdb'}

# 'port': port,
def changeParametrs(host, port, user, password, db):
    global parametrs
    parametrs = {
        'host': host,
        'port': port,
        'user': user,
        'password': password,
        'db': db}
    print(parametrs)


def getConnection():
    connection = psycopg2.connect(
        host=parametrs['host'],
        user=parametrs['user'],
        password=parametrs['password'],
        database=parametrs['db'])
    return connection


def SQLQuery(query, d=None):
    result = ""
    try:
        connection = getConnection()
        cursor = connection.cursor()
        cursor.execute(query, d)

        if query.split()[0] in ['INSERT', 'DELETE', 'UPDATE', 'CREATE']:
            connection.commit()

        if query.split()[0] == 'SELECT':
            for row in cursor:
                result += "\n" + str(row)

        result += "\n" + str(cursor.statusmessage)
    except Exception as ex:
        result += "\nError while working with PostgreSQL" + ex
    finally:
        if connection:
            cursor.close()
            connection.close()
        return result


def initDataBase():
    query = """
        CREATE TABLE TVchannel (
        channel varchar(256) NOT NULL,
        broadcast varchar(256) NOT NULL,
        CONSTRAINT TVchannel_pkey PRIMARY KEY (channel)
        );

        CREATE TABLE OwnerChannel (
        channel varchar(256) NOT NULL,
        owner varchar(256) NOT NULL,
        CONSTRAINT OwnerChannel_pkey PRIMARY KEY (channel),
        );


        CREATE TABLE Rating (
        nameProgram varchar(256) NOT NULL,
        channel varchar(256) NOT NULL,
        rating integer,
        CONSTRAINT Rating_pkey PRIMARY KEY (nameProgram),
        );

        CREATE TABLE TVProgram (
        nameProgram varchar(256) NOT NULL,
        channel varchar(256) NOT NULL,
        director varchar(256) NOT NULL,
        CONSTRAINT Program_pkey PRIMARY KEY (nameProgram),
        );

        CREATE TABLE ProgramRelease (
        nameProgram varchar(256) NOT NULL,
        releaseNumber integer NOT NULL,
        premiere date NOT NULL,
        CONSTRAINT ProgramRelease_pkey PRIMARY KEY (nameProgram, releaseNumber),
        );

        CREATE TABLE People (
        fullname varchar(256) NOT NULL,
        born date NOT NULL,
        nameProgram varchar(256) NOT NULL,
        releaseNumber integer NOT NULL,
        CONSTRAINT People_pkey PRIMARY KEY (nameProgram, releaseNumber, fullname, born),
        );"""
    return SQLQuery(query)


if __name__ == '__main__':
    print(parametrs)



