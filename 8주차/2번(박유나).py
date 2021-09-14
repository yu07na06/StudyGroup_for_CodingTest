def solution(scores):
    result=""
    for i in range(len(scores[0])):
        temp=[]
        for j in range(len(scores)):
            temp.append(scores[j][i])
            
        if (temp[i]==min(temp) or temp[i]==max(temp)) and temp.count(temp[i])==1: del temp[i]
        
        number=sum(temp)/len(temp)
        
        if number>=90:
            result+="A"
        elif number>=80:
            result+="B"
        elif number>=70:
            result+="C"
        elif number>=50:
            result+="D"
        else:
            result+="F"
    return result
