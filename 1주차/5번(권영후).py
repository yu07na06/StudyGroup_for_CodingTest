# 테스트 1 〉	통과 (1.37ms, 7.7MB)
# 테스트 2 〉	통과 (0.94ms, 7.86MB)
# 테스트 3 〉	통과 (0.26ms, 7.72MB)
# 테스트 4 〉	통과 (0.33ms, 7.8MB)
# 테스트 5 〉	통과 (0.57ms, 7.74MB)
# 테스트 6 〉	통과 (1.08ms, 7.75MB)
# 테스트 7 〉	통과 (1.52ms, 7.77MB)
# 테스트 8 〉	통과 (7.06ms, 7.75MB)
# 테스트 9 〉	통과 (11.68ms, 7.95MB)
# 테스트 10 〉	통과 (441.64ms, 27.7MB)
# 테스트 11 〉	통과 (289.95ms, 23.6MB)
# 테스트 12 〉	통과 (439.00ms, 27.5MB)
# 테스트 13 〉	실패 (시간 초과)
# 테스트 14 〉	실패 (시간 초과)
# 테스트 15 〉	실패 (시간 초과)
# 테스트 16 〉	통과 (14.49ms, 8.28MB)
# 테스트 17 〉	통과 (132.24ms, 10.3MB)
# 테스트 18 〉	통과 (78.19ms, 9.28MB)
# 테스트 19 〉	통과 (0.72ms, 7.69MB)
# 테스트 20 〉	통과 (7.95ms, 7.98MB)

from itertools import combinations

def solution(orders, course_list):
    answer = []

    # 현재 입력된 메뉴의 종류를 오름차순으로 정렬
    # [A, B, C, D...]
    menu_list = sorted(set(list(''.join(orders))))
    
    # 코스 요리 메뉴의 갯수 별 loop
    for course in course_list:
        
        # 코스로 만들어 질 수 있는 case를 생성, combinations  사용
        match_course = {}
        course_case_list = list(combinations(menu_list, course))
        # print(course_case_list)
    
        for course_case in course_case_list:
            course_count = 0
            course_case_str = ''.join(course_case)
    
            for order in orders:
                # print("코스 = " + ''.join(course_case))
                # print("주문 = " + str(order))
                match_count = 0
                
                # 특정 메뉴가 course 케이스에 있으면, match_count 증감
                for menu in course_case:
                    if menu in order:
                        match_count += 1
                if match_count == len(course_case):
                    # print("Best course = " + course_case_str)
                    # print("주문 = " + str(order))
                    course_count += 1

            match_course[course_case_str] = course_count
            # print("[" + course_case_str + "]count -> " + str(course_count)) 
    
        # 코스 max 값 확인
        max_val = max(match_course.values())

        # max 값이 0일시, best menu 없음
        if max_val < 2:
            continue

        for key, val in match_course.items():
            if val == max_val:
                answer.append(key)

    # print("answer = " + str(answer))
    # 리스트 사전순으로 정렬하여 return
    return sorted(answer)

# ====================================================================
orders1 = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course1 = [2,3,4]
print(solution(orders1, course1))

orders2 = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course2 = [2, 3, 5]
print(solution(orders2, course2))

orders3 = ["XYZ", "XWY", "WXA"]
course3 = [2, 3, 4]
print(solution(orders3, course3))
