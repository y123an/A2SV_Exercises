class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        A = capacityA
        B = capacityB
        c = 0
        l, r = 0, len(plants)-1

        while l <= r:
            if l == r:
                if A < B:
                    if B >= plants[r]:
                        B = B - plants[r]
                    else:
                        B = capacityB
                        B = B - plants[r]
                        c += 1
                else:
                    if A >= plants[l]:
                        A = A - plants[l]
                    else:
                        A = capacityA
                        A = A - plants[l]
                        c += 1
                l += 1
                r -= 1         
            else:
                if A >= plants[l]:
                    A = A - plants[l]
                else:
                    A = capacityA
                    A = A - plants[l]
                    c += 1 
                if B >= plants[r]:
                    B = B - plants[r]
                else:
                    B = capacityB
                    B = B - plants[r]
                    c += 1 
                r -= 1
                l += 1

        return c