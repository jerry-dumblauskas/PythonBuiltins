__author__ = 'jerrydumblauskas'

class Worker():
    '''
    doing some tests on relative importing.....ugh pycharm
    if I call from the shell from the root of this project like so
    python -m rel_imp_work.mod_that_does_the_rel_import
    works fine -- but I get a ValueError: Attempted relative import in non-package
    error in Pycharm
    '''
    def __init__(self):
        self.A = "test"

    def caller(self):
        return self.A

