import sys

with open(sys.argv[1]) as inFile:
    next(inFile)
    for i, line in enumerate(inFile, 1):
        numOfItems = int(line)
        items = []
        for x in xrange(0,numOfItems):
            items.append(int(next(inFile)))
        # print 'items before sort', items
        items.sort(key=int, reverse=True)
        numOfTrips = 0

        while len(items) > 0:
            topItemWeight = items.pop(0)
            apparentWeightSum = 0
            apparentWeightSum += topItemWeight
            while apparentWeightSum < 50:
                if len(items) == 0 and apparentWeightSum < 50:
                    numOfTrips -= 1
                    break
                items.pop()
                apparentWeightSum += topItemWeight
            numOfTrips += 1

            # print 'items', items
        print "Case #{}: {}".format(i, numOfTrips)