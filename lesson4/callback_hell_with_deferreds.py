from twisted.internet import reactor, defer

def runQuery(sql_query, sql_args):
    print "sql_query is {}, sql_args are {}".format(sql_query, sql_args)
    d = defer.Deferred()
    reactor.callLater(0.5, d.callback, "DATA")
    return d

def load_player(player_id):
    print "load_player begin"
    d = runQuery("select person profile", player_id)
    d.addCallback(load_player_step2, player_id)
    print "load_player end"

def load_player_step2(res, player_id):
    print "load_player_step2 begin"
    #do something with selected player data in res...
    #continue loading
    print "load_player_step2: res is {}".format(res)

    d = load_achievements(player_id)
    d.addCallback(finish_loading, player_id)
    print "load_player end"
    print "load_player_step2 end"

def load_achievements(player_id):
    print "load_achievements begin"
    d = runQuery("select person achievements", player_id)
    print "load_achievements end"
    return d


def finish_loading(res, player_id):
    #do something with selected player achievements in res...
    print "finish_loading: res is {}".format(res)
    print "Yehoo, done with loading player {}".format(player_id)
    reactor.stop()

reactor.callWhenRunning(load_player, 1)
reactor.run()
