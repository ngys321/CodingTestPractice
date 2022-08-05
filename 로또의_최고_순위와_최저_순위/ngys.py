def solution(lottos, win_nums):  
    count_correct = 0
    count_zero = 0
    
    answer = []
    
    for num in lottos:
        if num in win_nums:
            count_correct = count_correct + 1
        if num == 0:
            count_zero = count_zero + 1
    # 교훈 : 두 리스트를 비교해서 서로 동일한 원소를 가졌는지 카운트할땐, 두 리스트 중 아무거나를 기준으로 반복문을 작성해도 된다.
    # 여기선 lottos를 기준으로 for문 작성하거나, win_nums 를 기준으로 for문 작성하거나 해도 되나, lottos에 0 를 카운트 해야 하므로 이 문제 풀이에서는 lottos 를 기준으로 반복문을 작성했다. 
    worst_rank = 7 - count_correct
    
    best_rank = 7 - (count_correct + count_zero)
    if worst_rank >= 6:
        worst_rank = 6
    if best_rank >= 6:
        best_rank = 6
    
    answer.append(best_rank)
    answer.append(worst_rank)
    
    return answer