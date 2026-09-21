class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        arr = []

        for ch in tokens:
            if ch == '+':
                arr.append(arr.pop() + arr.pop())
            elif ch == '-':
                a, b = arr.pop(), arr.pop()
                arr.append(b - a)
            elif ch == '*':
                arr.append(arr.pop() * arr.pop())
            elif ch == '/':
                a, b = arr.pop(), arr.pop()
                arr.append(int(b/a))

            else:
                arr.append(int(ch))

        return arr[0]