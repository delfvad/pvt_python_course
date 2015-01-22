from twisted.internet import reactor, defer

def runQuery(sql_query, sql_args):
    print "sql_query is {}, sql_args are {}".format(sql_query, sql_args)
    d = defer.Deferred()
    reactor.callLater(0.5, d.callback, "DATA")
    return d


def load_achievements(player_id):
    print "load_achievements begin"
    d = runQuery("select person achievements", player_id)
    print "load_achievements end"
    return d

@defer.inlineCallbacks
def load_player(player_id):
    print "load_player begin"
    res = yield runQuery("select person profile", player_id)
    print "load_player: res is {}".format(res)
    res2 = yield load_achievements(player_id)
    print "load_player: res2 is {}".format(res2)
    print "load_player end"
    print "Yehoo, done with loading player {}".format(player_id)
    reactor.stop()

reactor.callWhenRunning(load_player, 1)
reactor.run()
