__author__ = 'jerrydumblauskas'


def check_them(tst1, tst2):
    """
    Anagram interview question
    :param tst1:
    :param tst2:
    :return: True if words are an anagram, False if not
    """
    if len(tst1) != len(tst2):
        return False

    tst2_sorted = sorted(tst1)

    for pos, item in enumerate(sorted(tst1)):
        if item != tst2_sorted[pos]:
            return False
    return True


