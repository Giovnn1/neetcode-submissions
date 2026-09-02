class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = {n : 0 for n in hand}
        for n in hand:
            count[n] += 1
        hand.sort()
        for n in hand:
            if count[n]:
                for k in range(n, n + groupSize):
                    if k not in count.keys() or count[k] == 0:
                        return False
                    count[k] -= 1
        return True

        


                

        