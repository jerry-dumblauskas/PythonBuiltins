__author__ = 'jerrydumblauskas'

from .mod_to_be_relative_imported import Worker

'''
why doesn't this work?
'''

print Worker().caller()

if __name__ == "__main__":
    print "boom"