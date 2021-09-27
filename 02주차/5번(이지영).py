def solution(words, queries):
    answer = []
    for _ in queries:
        fronted = False
        count = 0
        if _.find('?') != 0:
            fronted = True
        for w in words:
            r = w
            word = _.replace("?", "")   #key
            if r.replace(word, "", 1).find(word) > -1:  #동일한 가사 책정
                idx = r.find(word)
                r = r.replace(word, "")
                r = r[0:idx]+word+r[idx:len(r)]
            if not fronted:
                r = r[::-1]
            if r.find(word) < 0:    #같은 가사 없으면 카운트 x
                break
            if len(r.replace(word, "")) == len(_.replace(word, "")):
                count += 1
        answer.append(count)
            
    return answer