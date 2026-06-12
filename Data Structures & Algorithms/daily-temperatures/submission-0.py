class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result =[]
        for i in range(len(temperatures)):
            if i == len(temperatures) - 1:
                result.append(0)
                break
            stack = []
            for j in range(i,len(temperatures)):
                if i == j:
                    stack.append(temperatures[j])
                else:
                    if temperatures[j] <= temperatures[i]:
                        stack.append(temperatures[j])
                        if j == len(temperatures) - 1:
                            result.append(0)
                            break
                            
                    else:
                        result.append(len(stack))
                        break
        return result

                

        






            
