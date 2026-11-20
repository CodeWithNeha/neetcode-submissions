class Solution:
    def helper(self, operator, first, second):
        if operator == "+":
            return second + first
        elif operator == "-":
            return second - first
        elif operator == "*":
            return second*first
        else:
            return int(second/first)

    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+","-","*","/"]
        st = []
        for i in tokens:
            if i not in operators:
                st.append(int(i))
            else:
                first = st.pop()
                second = st.pop()
                st.append(self.helper(i, first, second))
        return st[0]
                    

        