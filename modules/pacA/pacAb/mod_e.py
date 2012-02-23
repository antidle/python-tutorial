from .pacAa import mod_d

print 'module e initialized'

def funcE(str):
    print str

if __name__ == '__main__':
    import sys
    mod_d('from e')
