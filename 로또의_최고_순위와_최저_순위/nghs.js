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

//블로그 풀이 참조
// function solution(lottos, win_nums) {
//     var answer = [];
    
//     const correct = lottos.filter(lotto => win_nums.includes(lotto)).length;
    
//     const zeros = lottos.filter(lotto => lotto === 0).length;
//     console.log(correct, zeros);
    
//     let min = 7-correct >= 6 ? 6 : 7-correct;
//     let max = min-zeros < 1 ? 1 : min-zeros;
    
//     answer = [max, min]
//     return answer;
// }
