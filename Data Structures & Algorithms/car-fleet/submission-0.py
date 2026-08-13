class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        new_list = sorted(zip(position, speed), key=lambda pair: pair[0], reverse=True)

        fleets = []
        prev_pair = None

        for pos, spd in new_list:
            eta = (target - pos) / spd
            if not fleets:
                fleets.append(eta)
            else:
                if fleets[-1] < eta:
                    fleets.append(eta)
                else:
                    continue
        return len(fleets)
            


        