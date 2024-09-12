class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None
    
    def size(self):
        return len(self.items)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = Stack()
        opening = {'{': '}', '[': ']', '(': ')'}
        closing = {'}': '{', ')': '(', ']': '['}

        if len(s) <= 1:
            return False

        for i, char in enumerate(s):
            if i == 0:
                if char not in opening:
                    return False
                else:
                    stack.push(char)

            if i >= 1:
                # if the current char is a closing char
                if char in closing:
                    if closing[char] == stack.peek():
                        stack.pop()
                        continue
                    else:
                        return False
                else:
                    stack.push(char)

        return True if stack.size() < 1 else False
        
        


