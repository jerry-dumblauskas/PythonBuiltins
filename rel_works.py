__author__ = 'jerrydumblauskas'

from rel_imp_work import mod_that_does_the_rel_import

'''
this works -- PEP 366 - Main module explicit relative imports

This pep says you can't call a .py with relative imports from the same directory if it is the __main__
'''
mod_that_does_the_rel_import.junk()