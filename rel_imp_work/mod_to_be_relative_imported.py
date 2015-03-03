__author__ = 'jerrydumblauskas'

class Worker():
    '''
    doing some tests on relative importing.....
    if I call from the shell from the root of this project like so
    python -m rel_imp_work.mod_that_does_the_rel_import
    works fine -- because of peo 366
    '''
    def __init__(self):
        self.A = "test"

    def caller(self):
        return self.A

