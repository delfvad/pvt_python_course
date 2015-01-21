from twisted.internet import reactor
from twisted.enterprise import adbapi 

dbpool = adbapi.ConnectionPool("MySQLdb", host="dbhost", db='dbname', user='username', passwd='password')
def getNickname(player_id):
    return dbpool.runQuery("SELECT nickname FROM players WHERE id=%(id)s", {"id": player_id})

def printResult(l):
    if l:
        print "Players nickname is ", l[0][0]
    else:
        print "No such player"
getNickname(1).addCallback(printResult)
reactor.run()
