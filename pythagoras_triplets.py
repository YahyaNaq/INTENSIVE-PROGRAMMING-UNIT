# Python Program to Determine all Pythagorean Triplets in the Range

HypChecker=0
for Hyp in range(1,20):
    for Perp in range(1,20):
        for Base in range(1,20):
            if Hyp**2==Perp**2+Base**2:
                HypChecker=Hyp
                print(Hyp,Perp,Base)
                break
        if HypChecker==Hyp:
            break
