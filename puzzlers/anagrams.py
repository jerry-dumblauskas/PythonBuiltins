__author__ = 'jerrydumblauskas'


def check_them(tst1, tst2):
    """
    Anagram interview question
    :param tst1:
    :param tst2:
    :return: True if words are an anagram, False if not
    """
    return sorted(tst1) == sorted(tst2)
