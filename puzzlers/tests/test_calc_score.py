import unittest
import puzzlers.bowling


class TestCalcScore(unittest.TestCase):
    def test_calc_score_wrong_length(self):
        with self.assertRaises(Exception):
            puzzlers.bowling.calc_score([0])

    def test_calc_score_right_length_zero_score(self):
        self.assertEquals(0, puzzlers.bowling.calc_score([(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                                                          (0, 0), (0, 0), (0, 0), ]))

    def test_calc_score_no_spares(self):
        self.assertEquals(80, puzzlers.bowling.calc_score([(8, 0), (8, 0), (8, 0), (8, 0), (8, 0), (8, 0), (8, 0),
                                                           (8, 0), (8, 0), (8, 0), ]))

    def test_calc_score_spares(self):
        self.assertEquals(110, puzzlers.bowling.calc_score([(8, 2), (8, 2), (8, 0), (8, 0), (8, 0), (8, 0), (8, 0),
                                                            (8, 0), (8, 0), (8, 2), (8, 55)]))

    def test_calc_score_spares_high(self):
        self.assertEquals(191, puzzlers.bowling.calc_score([(9, 1), (9, 1), (9, 1), (9, 1), (9, 1), (9, 1), (9, 1),
                                                            (9, 1), (9, 1), (9, 1), (10, 88)]))

    def test_calc_score_strikes(self):
        self.assertEquals(300, puzzlers.bowling.calc_score([(10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0),
                                                            (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0)]))

    def test_calc_score_strikes_perfect(self):
        self.assertEquals(290, puzzlers.bowling.calc_score([(10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0),
                                                            (10, 0), (10, 0), (10, 0), (10, 0), (8, 2)]))
