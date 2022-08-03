function solution(lottos, win_nums) {
    var answer = [];
    var zero = 0;
    var correctNumber =0; 
    var leastScore = 0;
 
    for(let i = 0; i <6; i++ ) {
        if(lottos[i]===0) {
            zero = zero+1;
            continue;
        }
        for(let j = 0; j <6; j++) {
            if(lottos[i] === win_nums[j]) {
                correctNumber = correctNumber +1;
                break;
                
            }
        }
    }    
    switch (correctNumber) {
        case 2: leastScore = 5;
            break;
        case 3: leastScore = 4;
            break;
        case 4: leastScore = 3;
            break;
        case 5: leastScore = 2;
            break;
        case 6: leastScore = 1;
            break;
        default: leastScore = 6;
            
            
    }
    if(zero === 6 ) {
         answer.push(leastScore-zero+1);
         answer.push(leastScore);
    }else {
        answer.push(leastScore-zero);
        answer.push(leastScore);
    }
    
    return answer;
}
