import datetime


def solution(play_time, adv_time, logs):
    def create_play_time_list():
        h, m, s = map(int, play_time.split(':'))
        sec = int(datetime.timedelta(hours=h, minutes=m, seconds=s).total_seconds())  # 시간, 분, 초 전체를 초로 변환
        return [0] * (sec + 1)  # play_time 리스트 생성

    def adv_time_in_seconds():
        h, m, s = map(int, adv_time.split(':'))
        sec = int(datetime.timedelta(hours=h, minutes=m, seconds=s).total_seconds())  # 시간, 분, 초 전체를 초로 변환
        return sec

    def duplicated_time(play_time_list):
        seconds_list = [i.split('-') for i in logs]
        # print(seconds_list)
        for inner_list in seconds_list:
            for i in range(2):
                h, m, s = map(int, inner_list[i].split(':'))
                inner_list[i] = int(datetime.timedelta(hours=h, minutes=m, seconds=s).total_seconds())

        # 하나하나 계속 더해나가면 log값이 많거나 i[0]와 i[1] 사이의 거리가 길 경우 시간초과남
        # for i in seconds_list:
        #     for j in range(i[0], i[1]):
        #         play_time_list[j] += 1
        for i in seconds_list:
            play_time_list[i[0]] += 1
            play_time_list[i[1]] -= 1
        for i in range(1, len(play_time_list)):
            play_time_list[i] = play_time_list[i-1] + play_time_list[i]

    play_time_list = create_play_time_list()
    duplicated_time(play_time_list)
    adv_seconds = adv_time_in_seconds()

    max_sum = float('-inf')
    start = 0
    curr_sum = 0
    for end, val in enumerate(play_time_list):
        curr_sum += val
        if end - start + 1 == adv_seconds:
            if curr_sum > max_sum:
                max_sum = curr_sum
                answer = start
            curr_sum -= play_time_list[start]
            start += 1
    ###############################        timedelta(seconds = 24시간이 넘어가는 초) -> days 런타임에러      ################################
    # hr, m, s = str(datetime.timedelta(seconds=answer)).split(':')
    # hr = int(hr)
    # return '{:02d}'.format(hr) + ':%s:%s' % (m, s)

    # a = str(datetime.timedelta(seconds=answer))
    # return datetime.datetime.strptime(a, '%H:%M:%S').strftime('%H:%M:%S')   # datetime객체로 반환된것(strptime)을 문자열로 반환(strftime)

    hr = answer // 3600
    m = (answer % 3600) // 60
    s = answer % 60
    return '{:02d}:{:02d}:{:02d}'.format(hr, m, s)


# import datetime
#
#
# def into_seconds(time_string):
#     h = int(time_string[0:2]) * 60 * 60
#     m = int(time_string[3:5]) * 60
#     s = int(time_string[6:8])
#     return h + m + s
#
#
# def solution(play_time, adv_time, logs):
#     play_time_seconds = into_seconds(play_time)
#     seconds_list = [0] * (play_time_seconds + 1)
#     adv_time_seconds = into_seconds(adv_time)
#
#     for i in logs:
#         a, b = map(into_seconds, i.split("-"))
#         seconds_list[a] += 1
#         seconds_list[b] -= 1
#         # for j in range(btw[0], btw[1]):
#         #     seconds_list[j] += 1
#     for i in range(1, len(seconds_list)):
#         seconds_list[i] = seconds_list[i-1] + seconds_list[i]
#
#     max_sum = float('-inf')
#     start = 0
#     curr_sum = 0
#     for end, val in enumerate(seconds_list):
#         curr_sum += val
#         if end - start + 1 == adv_time_seconds:
#             if curr_sum > max_sum:
#                 max_sum = curr_sum
#                 answer = start
#             curr_sum -= seconds_list[start]
#             start += 1
#
#     # print(max_sum)
#
#     # hr, m, s = str(datetime.timedelta(seconds=answer)).split(':')
#     # hr = int(hr)
#     # return '{:02d}'.format(hr) + ':%s:%s' % (m, s)
#
#     hr = answer // 3600
#     m = (answer % 3600) // 60
#     s = answer % 60
#     return '{:02d}:{:02d}:{:02d}'.format(hr, m, s)


play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
result = "01:30:59"
print(solution(play_time, adv_time, logs))

# play_time = "99:59:59"
# adv_time = "25:00:00"
# logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
# result = "01:00:00"
# print(solution(play_time, adv_time, logs))
#
# play_time = "50:00:00"
# adv_time = "50:00:00"
# logs = ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]
# result = "00:00:00"
# print(solution(play_time, adv_time, logs))
