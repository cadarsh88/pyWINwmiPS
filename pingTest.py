import os
def ping(address):
    return not os.system('ping %s -n 1' % (address,))