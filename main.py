import psycopg2
import db
import queryINSERT
import querySELECT
import queryUPDATE
import queryDELETE
import interface


if __name__ == '__main__':
    # print(queryUPDATE.updateTVchannel("тнт", "цифра", "тнт"))
    # print(querySELECT.selectKeyTVchannel("стс"))
    # print(querySELECT.selectTVchannel())
    # print(queryINSERT.insertTVchannel("рен", "цифа"))
    # print(queryUPDATE.updateTVchannel("рен","цифhа","рен"))
    interface.dbInterface()
