def solution(id_list, report, k):

    id_list.append("0")
    counting_dic = {}
    for i in  id_list:
        counting_dic[i] = 0
    
    report_dic = {}
    for id in id_list:
        report_dic[id] = "0"

    for i in report:
        reporter, reportee = i.split()
        if not reportee in report_dic[reporter]:
            report_dic[reporter] = reportee
            counting_dic[reportee] = counting_dic[reportee] + 1
    
    answer = []    

    id_list.pop()

    for id in id_list:
        num_of_get_mails = 0
        for reporter, reportee in report_dic.items():
            if reporter == id and counting_dic[reportee] >= k:
                num_of_get_mails = num_of_get_mails + 1
        answer.append(num_of_get_mails)
                
    
    
    return answer

# Codes in below are for testing
id_list = ["A", "B", "C", "D"]
report = ["A B", "C B", "B D", "A D", "C A"]
k = 2

print (solution(id_list, report, k))