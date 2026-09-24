class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        ans = 0
        for i in range(len(operations)):
            if operations[i].isdigit():
                result.append(operations[i])
            elif operations[i] == "+":
                print(result)
                result.append(int(result[-1])+int(result[-2]))
            elif operations[i] == "C":
                result.pop()
            else:
                result.append(int(operations[i-1])*2)

        return sum([int(x) for x in result])
        