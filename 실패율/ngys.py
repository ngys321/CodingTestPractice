#실패율을 구하는 코드를 완성하라.

#실패율의 정의
#    스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

#input
#    N : 전체 스테이지의 개수
#    stages : 현재 멈춰있는 스테이지의 번호가 담긴 배열, 배열 내의 각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다. 
#             만약 배열 내의 원소중 N+1 값을 갖고 있으면, 그 플레이어는 모든 스테이지를 클리어한 것임.

#output
#    실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return
#    * 만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록
#    * 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의

def solution(N, stages):
    
    passing_num = [0]*N
    trying_num = [0]*N
    
    for x in stages:
        for y in range(x):
            if (y+1)!=x:
                passing_num[y]+=1
            else:
                if x > N:
                    pass
                else:
                    trying_num[y]+=1
    
    fail_rate = [] #실패율
    for x in range(N):
        if(trying_num[x]==0): # trying_num[x] == 0 and passing_num[x] 모두 영어인 경우를 포함
            fail_rate.append(0.0)
        else:
            fail_rate.append( trying_num[x] / (trying_num[x] + passing_num[x]) ) 
    
    fail_rate_dict = {}
    for idx, fr in enumerate(fail_rate):
        fail_rate_dict[idx] = fr
    sorted_dict = sorted(fail_rate_dict.items(), key = lambda item : item[1], reverse = True)
    
    answer = []
    for key, value in sorted_dict:
        answer.append(key+1)
    
    return answer
