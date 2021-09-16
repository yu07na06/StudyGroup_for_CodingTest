def solution(table, languages, preference):
    length = len(languages)
    pref = []

    for i in table:
        tmp = i.split()
        total = 0
        for j in range(length):
            if languages[j] in tmp[1:]:
                total += abs(tmp.index(languages[j]) - 6) * preference[j]
        pref.append([total, tmp[0]])
    # print(pref)
    return sorted(pref, key=lambda x: (-x[0], x[1]))[0][1]


if __name__ == '__main__':
    table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
             "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
             "GAME C++ C# JAVASCRIPT C JAVA"]
    languages = ["PYTHON", "C++", "SQL"]
    preference = [7, 5, 5]
    result = "HARDWARE"
    print(solution(table, languages, preference))

    table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
             "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
             "GAME C++ C# JAVASCRIPT C JAVA"]
    languages = ["JAVA", "JAVASCRIPT"]
    preference = [7, 5]
    result = "PORTAL"
    print(solution(table, languages, preference))
