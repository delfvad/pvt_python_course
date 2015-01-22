from twisted.internet import defer, reactor

def g():
    d = defer.Deferred()
    reactor.callLater(0.5, d.callback, 1)
    return d

@defer.inlineCallbacks
def f():
    res = yield g()
    print 'f, res is {}'.format(res) 
    res2 = yield 2
    print 'f, res2 is {}'.format(res2) 
    reactor.stop()

reactor.callWhenRunning(f)
reactor.run()
