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

//11. 용돈 압수(복기 필요)
let arr = [];
const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})
rl.on("line", function(line){
    arr = line.split('500원');
    rl.close();
})
rl.on("close", function(){
    console.log(arr);
    process.exit();
})

//12. 훈민정음
//13. 충성! 입대를 명 받았습니다!
//14. 펜 파인애플 애플 펜

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
