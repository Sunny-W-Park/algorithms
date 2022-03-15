//1. 어서와~ 엘리스는 처음이지?
console.log("Welcome to Elice~");

//2. 토끼 그리기
console.log("\(\\\_\/\)\n\(\.\ \. \)\n\|\\\ \/\|");

//3. 변수 다루기
var num = 1030;
var num = num + 204;
var string = 'hello, elice!';
console.log(num);
console.log(string);

//4. 값 입력받기
//readline > readline.createInterface > .on / .close
const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});
rl.on("line", (line) => {
    console.log(line);
    rl.close();
});
rl.on("close", () => {
    process.exit();
});

//5. 음식 가격 계산하기
// 한식 가격
var korean = 7000;
// 중식 가격
var chinese = 6000;
// 양식 가격
var western = 8500;
// 할인된 한식의 가격
var discount_korean = korean * 0.9;
// 전체 예산을 계산하여 저장해 보세요.
var total_price = 55*discount_korean + 43*chinese + 52*western;
// 값을 확인해 보세요!
console.log("한식 : " + korean);
console.log("중식 : " + chinese);
console.log("양식 : " + western);
console.log("할인된 한식 : " + discount_korean);
console.log("전체 예산 : " + total_price);

//6. 화살표 함수
var elice = [
  'rabbit',
  'cheshire',
  'mad hatter',
  'heart queen'
];
// 화살표 함수를 이용해 변경해보세요.
console.log(elice.map(e => e.length));

//7. 과일 장수
// fruits 배열을 만들어 과일들을 입력받고, fruits 배열에서 콩과 무를 제거하세요.
// 과일이 아닌 것을 잘 제거했는지 console.log를 통해 배열을 출력해 확인해봅니다.
var fruits = [];
const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});
rl.on("line", (line) => {
    fruits = line.split(' ');
    rl.close();
});
rl.on("close", () => {
    console.log(fruits.filter((element) => element !== '콩' & element !== '무'));
    process.exit();
});

//8. 몫과 나머지 구하기
// num1과 num2입니다. 수정하지 마세요!
var num1 = 23781367;
var num2 = 1754;
// 지시사항을 참고하여 코드를 작성하세요.
console.log(Math.floor(num1/num2), num1%num2);

//9. 한 번에 여러 입력받기
var input = [];
const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});
rl.on("line", function(line){
    input = line.split(' ');
    rl.close();
});
rl.on("close", function(){
    console.log(input[0]);
    console.log(input[1]);
    console.log(input[2]);
    process.exit();
});

//10.
// 여러 숫자를 입력 받도록 코드를 작성하여, 입력된 숫자의 평균을 구하세요.
function average(arr){
    var result = 0;
    for(var k = 0; k < arr.length; k++){
        result = result + arr[k];
    }
    return result/arr.length;
}
var arr = [];
const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});
rl.on("line", function(line){
    arr = line.split(' ').map((element) => parseInt(element));
    rl.close();
});
rl.on("close", function(){
    console.log(Math.floor((average(arr))));
    process.exit();
})

//11. 용돈 압수(복기)
//money 문자열에서 '500원'을 기준으로 끊어서 배열에 저장
var money = '500원, 엘리스 토끼는 하루 용돈으로 500원. 단돈 500원을 받는다. 부모님이 주시는 500원. 하지만 잘못한 것이 있으면 500원을 받지 못한다.';
var arr = money.split('500원');
console.log(arr);

//12. 훈민정음(복기)
// hangul 배열에는 훈민정음의 서문이 담겨있습니다. 인덱싱을 하여 단어 만들기 게임을 해봅시다.
// hangul 배열의 0번째, 47번째, 23번째 인덱스를 순서대로 붙여 단어를 만들고 출력하세요
var hangul = ['나', '랏', '말', '싸', '미', '듕', '귁', '에', '달', '아', '문', '자', '와', '로', '서', '르', '사', '맛', '띠', '아', '니', '할',
          '쌔', '이', '런', '젼', '차', '로', '어', '린', '백', '셩', '이', '니', '르', '고', '져', '홀', '빼', '이', '셔', '도', '마', '참',
          '내', '제', '뜨', '들', '시', '러', '펴', '디', '못', '할', '노', '미', '하', '니', '라'];
var result = '';
result += hangul[0];
result += hangul[47];
result += hangul[23];
//or
//var result = hangul[0] +  hangul[47] + hangul[23];
console.log(result);

//13. 충성! 입대를 명 받았습니다!(복기)
//solider 배열을 오름차순으로 정렬하세요. solider 배열의 길이를 count 변수에 저장하세요. 
//배열 내 숫자를 그냥 sort()하는 경우 아스키 코드 기준으로 정렬이 되어, 정상적으로 정렬되지 않습니다.
//sort() 내 아래 함수를 매개변수로 넣어, 오름차순으로 정렬할 수 있습니다.
//function compareNumbers(a, b) {
//    return a - b;
//}
var soldier = [12, 2, 5, 3, 7, 4, 10, 8, 1, 9, 13, 11, 6];
var count = soldier.length;
soldier.sort(function(a, b){
    return a - b;
});
console.log(soldier);
console.log(count);

//14. 펜 파인애플 애플 펜(복기)
/*
펜 파인애플 애플 펜
words 배열에 영어 단어들이 들어있습니다.
문자열/배열 함수를 이용해 문장을 한 번 만들어볼까요?

//지시사항
words 배열에서 splice를 이용해 특정 값을 제거하여 아래와 같은 배열로 만드세요.
[ 'i', 'have', 'a', 'pen', 'pineapple', 'apple', 'pen' ]
Copy
join을 이용해서 공백을 기준으로 리스트를 연결하여 lyrics 변수에 문자열로 저장하세요.
lyrics를 출력하세요.
문자 'p'의 개수를 length 함수를 이용해서 출력하세요.

//Tips!
splice()를 이용해 특정 인덱스의 원소를 제거할 수 있습니다. splice(4, 2)와 같이 작성하는 경우, 4번째 부터 2개의 원소를 제거한다는 의미입니다.
배열.join()로 배열의 원소를 이어 붙여 문자열로 만들 수 있습니다. 기본적으로는 콤마를 기준으로 이어 붙이지만, 매개변수에 ' '을 넣으면 공백을 기준으로 이어 붙입니다.
문자열에서 특정 문자의 개수를 세기 위해 match와 정규 표현식을 이용합니다. 문자열.match(/p/g)을 통해 p 문자 리스트를 얻을 수 있습니다. 해당 리스트의 길이가 p 문자의 개수입니다.
링크를 통해 정규 표현식에 대해 더 자세히 알아보세요.
*/
var words = ['i', 'have', 'a', 'pen', 'i', 'have', 'pineapple', 'i', 'have', 'an', 'apple', 'pen'];
words.splice(4, 2);
words.splice(5, 3);
console.log(words.join(' '));
console.log(words);
//method a. 2중 for문
var count = 0;
for(var i = 0; i <= words.length-1; i++){
    for(var j = 0; j <= words[i].length-1; j++){
        if(words[i][j] == 'p'){
            count += 1;
        }
    }
}
//method b. match 정규 표현식
var test = words.join(' ');
var match = test.match(/p/g);
console.log(match.length);

//15. 수업자료(문제x)

//16. 한 번에 여러 입력받기 3
var count = 0;
var N = 0;
var input = '';
const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});
rl.on("line", function(line){
    count += 1;
    if(count === 1){
        N = line;
    }
    else{
        input += line;
    }
    if(count > N){
        rl.close();
    }
});
rl.on("close", function(){
    console.log(input);
    process.exit();
})
