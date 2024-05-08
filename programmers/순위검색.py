# O(N) 시간복잡도

from collections import defaultdict
import bisect

def solution(info, query):
    # info 데이터를 분류하여 저장하기 위한 dictionary
    info_dict = defaultdict(list)

    # info 정보를 파싱하여 dictionary에 저장
    for idx, i in enumerate(info):
        temp = i.split()
        # 모든 가능한 속성 조합을 key로 사용
        keys = [
            temp[0] + ' ' + temp[1] + ' ' + temp[2] + ' ' + temp[3],
            '-' + ' ' + temp[1] + ' ' + temp[2] + ' ' + temp[3],
            temp[0] + ' ' + '-' + ' ' + temp[2] + ' ' + temp[3],
            temp[0] + ' ' + temp[1] + ' ' + '-' + ' ' + temp[3],
            temp[0] + ' ' + temp[1] + ' ' + temp[2] + ' ' + '-',
            '-' + ' ' + '-' + ' ' + temp[2] + ' ' + temp[3],
            '-' + ' ' + temp[1] + ' ' + '-' + ' ' + temp[3],
            '-' + ' ' + temp[1] + ' ' + temp[2] + ' ' + '-',
            temp[0] + ' ' + '-' + ' ' + '-' + ' ' + temp[3],
            temp[0] + ' ' + '-' + ' ' + temp[2] + ' ' + '-',
            temp[0] + ' ' + temp[1] + ' ' + '-' + ' ' + '-',
            '-' + ' ' + '-' + ' ' + '-' + ' ' + temp[3],
            '-' + ' ' + '-' + ' ' + temp[2] + ' ' + '-',
            temp[0] + ' ' + '-' + ' ' + '-' + ' ' + '-',
            '-' + ' ' + temp[1] + ' ' + '-' + ' ' + '-',
            '-' + ' ' + '-' + ' ' + '-' + ' ' + '-'
        ]
        for key in keys:
            info_dict[key].append(int(temp[4]))

    # dictionary의 점수 리스트를 정렬
    for key in info_dict:
        info_dict[key].sort()

    answer = []
    # query를 처리
    for q in query:
        q = q.replace(" and ", " ")
        conditions = q.split()
        key = ' '.join(conditions[:-1])
        score = int(conditions[-1])
        scores = info_dict[key]
        # 이진 검색을 사용하여 조건을 만족하는 점수의 수를 찾기
        count = len(scores) - bisect.bisect_left(scores, score)
        answer.append(count)

    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))