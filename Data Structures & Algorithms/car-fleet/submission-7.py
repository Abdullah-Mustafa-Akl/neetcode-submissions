class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        indices = list(range(len(position)))
        indices.sort(key=lambda i: position[i], reverse=True)
        stack = []
        for i in indices:
            fleet = (target - position[i]) / speed[i]
            if stack and fleet <= stack[-1]:
                continue
            stack.append(fleet)
        return len(stack)