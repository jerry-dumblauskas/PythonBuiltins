import sys
"""
basics of a script to start scraping data to get from our site
TODO
    1) add in call to site-- download data
    2) update code below
    3) store
"""
fi_read = open(sys.argv[1])
fi_write = open(sys.argv[2], 'w')

for line in fi_read:
    line2 = line.split('\t')
    nms = line2[0].split(" ")
    if len(nms) <=1 :
        nms.append(" ")
    xxx = nms[0] + "~" + nms[1] + "~" + line2[1]
    fi_write.write(xxx)