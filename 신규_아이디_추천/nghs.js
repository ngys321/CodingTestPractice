
//블로그 참조 https://velog.io/@scriptkid/%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8JS-%EC%8B%A0%EA%B7%9C-%EC%95%84%EC%9D%B4%EB%94%94-%EC%B6%94%EC%B2%9C

function solution(new_id) {
  let answer = new_id.toLowerCase()
    .replace(/[^a-z0-9-_.]/gi, '')
    .replace(/[.]{2,}/gi, '.')
    .replace(/^[.]|[.]$/gi,'');
  if(answer==='') answer = 'a';
  if(answer.length > 15){
    answer = answer.substring(0, 15);
    answer = answer.replace(/[.]$/gi,'');
  }
  while(answer.length < 3){
    answer += answer[answer.length-1];
  }
  return answer;
}
