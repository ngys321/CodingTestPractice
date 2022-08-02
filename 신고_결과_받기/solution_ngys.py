def solution(id_list, report, k):

    counting_dic = {}
    for id in id_list:
        counting_dic[id] = 0

    report_set = set()
    for report_string in report:
        report_set.add(report_string)

    for id in id_list:
        for reporter_reportee_str in report_set:
            reporter, reportee = reporter_reportee_str.split()
            if reporter == id:
                counting_dic[reportee] = counting_dic[reportee] + 1
    
    answer = []
    for id in id_list:
        num_of_mails_got = 0
        for reporter_reportee_str in report_set:
            reporter, reportee = reporter_reportee_str.split()
            if reporter == id:
                if counting_dic[reportee] >= k:
                    num_of_mails_got = num_of_mails_got + 1
        answer.append(num_of_mails_got)
    
    return answer

# Codes in below are for testing
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

print (solution(id_list, report, k))