class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # collision happens only when top node is + , new one is -
        stack = []

        for item in asteroids:
            print(item)
            while stack and stack[-1] > 0 and item < 0:
                diff = stack[-1] + item
                if diff > 0: # top  > item, no need to append
                    item = 0
                elif diff < 0: # top < item, pop top and add item
                    stack.pop()
                else:
                    stack.pop()
                    item = 0
            # print(stack)
            if item:
                stack.append(item)
        return stack