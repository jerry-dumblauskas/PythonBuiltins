"""
convenience method to calc a score from a bowling frame.
the method expects a List of tuples or bowling scores, like so:
6,4     'FRAME 1
7,2     'FRAME 2
10,0    'FRAME 3
etc
Here, a spare is inferred in frame one, as 6 + 4 = 10
a strike is defined as in frame 3.

in bowling there are 10 frames.  With a caveat that on the 10th frame if you score a spare you get an extra
roll, if a strike you get 2 extra rolls (which can be 1 or two more frames)

"""


def calc_score(scoring_frames):
    if len(scoring_frames) not in (10, 11, 12):
        raise Exception("Wrong number of frames!  Need 10 or 11 0r 12.  You have {}".format(len(scoring_frames)))

    rtn = 0

    for cnt, frm in enumerate(scoring_frames):
        if cnt < 10:
            rtn = rtn + sum(frm)

            if sum(frm) == 10:  # A spare or strike
                if frm[0] == 10:  # strike
                    nf = scoring_frames[cnt + 1]
                    rtn = rtn + sum(nf)
                    if nf[0] == 10:
                        nf2 = scoring_frames[cnt + 1]
                        rtn = rtn + nf2[0]
                else:
                    rtn = rtn + scoring_frames[cnt + 1][0]

    return rtn


if __name__ == "__main__":
    print(calc_score([]))
