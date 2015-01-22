from twisted.internet.defer import Deferred

def do_login(res):
    print 'Before login processing..'
    print res
    print 'Done.'

def handle_errors(err):
    print 'Login error.'

d = Deferred()

# add a callback/errback pair to the chain
d.addCallbacks(do_login, handle_errors)

# fire the chain with a normal result
d.callback('Please authorize me')

print "Finished"
