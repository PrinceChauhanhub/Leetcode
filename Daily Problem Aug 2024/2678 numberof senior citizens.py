
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0 
        for x in details:
            if int(x[11]) > 6 :
                count+=1
            elif int(x[11])==6 and int(x[12])!=0:
                count+=1
        return count