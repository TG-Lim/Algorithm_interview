def solution(progresses, speeds):
    progress_length = len(progresses)
    end_dates = []
    for i in range(progress_length):
        if (100 - progresses[i]) % speeds[i] == 0:
            end_dates.append((100-progresses[i])//speeds[i])
        else:
            end_dates.append((100-progresses[i])//speeds[i]+1)
    
    action_index = 0
    now_index = 0
    answer = []
    cnt = 0
    while now_index < progress_length:
        if end_dates[now_index] <= end_dates[action_index]: # 배포할 수 있음
            cnt += 1
            now_index += 1
        else: # 배포못하고 새로 기다려야함
            action_index = now_index
            answer.append(cnt)
            cnt = 0
    if cnt != 0:
        answer.append(cnt)
    
    return answer
if __name__ == "__main__":
    cases = [
        ([93, 30, 55], [1, 30, 5], [2, 1]),
        ([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1], [1, 3, 2]),
        ([98, 97, 96, 95], [1, 1, 1, 1], [1, 1, 1, 1]),
        ([50], [1], [1]),
        ([90, 95, 99, 95, 60], [1, 1, 1, 1, 1], [4, 1])
    ]
    
    for case in cases:
        answer = solution(case[0], case[1])
        print(f"result: {answer} / answer: {case[2]}")