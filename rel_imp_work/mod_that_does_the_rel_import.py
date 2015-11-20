__author__ = 'jerrydumblauskas'

from .mod_to_be_relative_imported import Worker

'''
why doesn't this work? -- cause -- you can't call in the same directory see pep 366
'''

print (Worker().caller())

def junk():
    print ("done")


if __name__ == "__main__":
    print ("boom")
