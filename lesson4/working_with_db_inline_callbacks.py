from twisted.internet import reactor, defer
from twisted.enterprise import adbapi 

dbpool = adbapi.ConnectionPool("MySQLdb", host="dbhost", db='dbname', user='username', passwd='password')

@defer.inlineCallbacks
def getNickname(player_id):
    l = yield dbpool.runQuery("SELECT nickname FROM players WHERE id=%(id)s", {"id": player_id})
    if l:
        print "Players nickname is ", l[0][0]
    else:
        print "No such player"

reactor.callWhenRunning(getNickname, 1)
reactor.run()
