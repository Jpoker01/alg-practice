#WILL BE DONE USING STACK
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []

        for operation in operations:
            print(scores)
            print(operation)
            if operation == "+":
                if len(scores) >= 2:
                    top_value = scores.pop()
                    second_top_value = scores[-1]
                    scores.append(top_value)
                    scores.append(top_value + second_top_value)
            elif operation == "C":
                scores.pop()
            elif operation == "D":
                if scores:
                    scores.append(scores[-1]*2)
            else:
                scores.append(int(operation))
            print(scores)



        return sum(scores)