def solution(participant, completion):
    part_cnt = {name: 0 for name in set(participant)}
    for name in participant:
        part_cnt[name] += 1

    for name in completion:
        part_cnt[name] -= 1

    for name in part_cnt:
        if part_cnt[name] != 0:
            return name