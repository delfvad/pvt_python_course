from twisted.internet.defer import Deferred
from twisted.python.failure import Failure

def do_login(res):
    print 'Before login processing..'
    print res
    print 'Done.'

def handle_errors(err):
    print 'Login error.'
    print err

d = Deferred()

# add a callback/errback pair to the chain
d.addCallbacks(do_login, handle_errors)

# fire the chain with an error result
d.errback(Failure(Exception("bad login or password")))

print "Finished"
