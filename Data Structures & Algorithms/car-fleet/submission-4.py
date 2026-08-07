class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position, speed = map(list, zip(*sorted(zip(position, speed))))
        stack = []
        for i in range(len(position)):
            fleet = (target - position[i]) / speed[i]
            while stack and stack[-1] <= fleet:
                stack.pop()
            stack.append(fleet)
        return len(stack)