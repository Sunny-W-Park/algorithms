//1. 비가 오는 날엔
var p = 0;
var result = '';
const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})
rl.on("line", function(line){
    p = line;
    if(p >= 50){
        result = '우산을 챙긴다.';
    }
    else{
        result = '그냥 간다.';
    }
    rl.close()
})
rl.on("close", function(){
    console.log(result);
    process.exit();
})

//2. 집에 가는 길
var m = 0;
var result = '';
const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})
rl.on("line", function(line){
    m = line;
    if(m >= 1000){
        result = '택시';
    }
    else if(m >= 500){
        result = '버스';
    }
    else if(m >= 300){
        result = '지하철';
    }
    else{
        result = '도보';
    }
    rl.close()
})
rl.on("close", function(){
    console.log(result);
    process.exit();
})

//3. 조건에 맞는 암호 
var code = [];
var result = false;
const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})
rl.on("line", function(line){
    code = line.split(" ").map((el) => parseInt(el));
    var a = code[0]
    var b = code[1]
    var c = code[2]
    var d = code[3]

    var cond_a = false;
    if(a <= b){
        cond_a = true;
    }
    var cond_b = false;
    if(a === d){
        cond_b = true;
    }
    var cond_c = false;
    if(b > c){
        cond_c = true;
    }
    var cond_d = false;
    if(c < 6){
        cond_d = true;
    }
    var cond_e = false;
    if(a === b){
        cond_e = true;
    }
    var cond_f = false;
    if(a === c){
        cond_f = true;
    }
    var cond_g = false;
    if(a === d){
        cond_g = true;
    }
    if((cond_a == true & cond_b == true & cond_c == true & cond_d == true) | (cond_e == true & cond_f == true & cond_g == true)){
        result = true;
    }
    rl.close();
})
rl.on("close", function(){
    console.log(result);
    process.exit();
})

//4. 약수 출력하기
var target = 0;
var result = [];
const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});
rl.on("line", function(line){
    target = line;
    for(i = 1; i <= target; i++){
        if(target % i == 0){
            result.push(i);
        }
    }
    rl.close();
});
rl.on("close", function(){
    process.stdout.write(result.join(" "));
});
//한줄에 10개씩 출력하기
var target = 0;
var result = [];
const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});
rl.on("line", function(line){
    target = line;
    for(i = 1; i <= target; i++){
        if(result.length === 10){
            process.stdout.write(result.join(" "));
            console.log('');
            result = [];
        }
        if(target % i == 0){
            result.push(i);
        }
    }
    process.stdout.write(result.join(" "));
    rl.close();
});
rl.on("close", function(){
    process.exit();
});

// 5. 3, 6, 9 게임
for(i = 1; i <= 30; i++){
    var confirm = ''
    var clap = false;
    confirm += i
    for(j = 0; j <= confirm.length-1; j++){
        if(confirm[j] == '3' || confirm[j] == '6' || confirm[j] == '9'){
            clap = true;
        }
    }
    if(clap === true){
        console.log('짝!');
        }
    else{
        console.log(parseInt(confirm));
        }
}

// 6. 숫자 출력
var N = 0;
var str = '';
const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});
rl.on("line", function(line){
    N = line;
    for(i = 1; i <= N; i++){
        if(i < N){
            str += i;
            str += ', ';
        }
        if(i == N){
            str += i;
        }
    }
    rl.close();
});
rl.on("close", function(){
    console.log(str);
    process.exit();
});

// 7. 피보나치 수열 출력하기
var N = 0;
var arr = [];
const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});
rl.on("line", function(line){
    N = line;
    rl.close();
});
rl.on("close", function(){
    arr.push(0)
    arr.push(1)
    if(N == 1){
        var zero = arr.slice(0, 1);
        console.log(zero);
    }
    else{
        while(arr[arr.length-1] + arr[arr.length-2] < N){
            arr.push(arr[arr.length-1] + arr[arr.length-2]);
        }
        console.log(arr);
    }
    process.exit();
});

//8. 촉촉한 초코칩
var str = '';
var result = 0;
const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});
rl.on("line", function(line){
    str = line;
    rl.close();
});
rl.on("close", function(){
    if(str.includes('촉촉한 초코칩')){
        var start = 0;
        var end = 7;
        while(end <= str.length){
            var check = str.slice(start, end);
            if (check === '촉촉한 초코칩'){
                result += 1;
            }
            start += 1;
            end += 1;
        }
    }
    console.log(result);
    process.exit();
});

//9. 노동요
var str = '';
var result = '';
const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});
rl.on("line", function(line){
    str = line;
    rl.close();
});
rl.on("close", function(){
    for(var i = 0; i <= str.length-1; i++){
        if(str[i] === ' '){
            result += '링디기디기' + '\n';
        }
        else if(str[i] === '.'){
            result += '딩딩딩' + '\n';
        }
        else{
            result += '링딩동 '
        }
    }
    console.log(result);
    process.exit();
});

//10. 타격왕이 될거야(복기)
/* 타격왕이 될 거야
야구에서 타수는 선수가 공을 치기 위해 타석에 선 횟수이고 안타는 공을 잘 쳐서 출루한 횟수입니다.
타율은 안타를 타수로 나눈 비율로 만약 8타수 5안타라면 5/8 = 0.625로 야구에서는 6할 2푼 5리라고 읽습니다.
야구선수 엘리스 토끼는 타율이 가장 높은 선수에게 주어지는 상인 타격왕이 되고 싶어 합니다.
엘리스 토끼의 현재 타율은 16타수 6안타로 3할 7푼 5리입니다.
이후의 타수와 안타가 입력으로 주어질 때 엘리스 토끼의 타율을 할푼리로 출력해보세요.
단, 0.101 처럼 가운데 0이 들어가 있는 경우 0은 생략하여 1할 1리라고 출력하며 타율이0.3678 인 경우에는 소수점 넷째자리 이후는 버림을하여 3할 6푼 7리로 출력합니다.
입력 예시
3
2
Copy
출력 예시
4할
2푼
1리
Copy
입력 예시 2
5
2
Copy
출력 예시 2
3할
8푼
Copy
지시사항
0이상의 정수인 타수와 안타를 입력받으세요.
16타수 6안타인 상태에서 입력받은 타수와 안타를 더한 타율을 구하세요.
구한 타율을 할푼리로 출력하세요. 할푼리 아래의 소수점은 모두 버림하며 값이 0인 경우 생략합니다.
Tips!
두 줄에 걸쳐 입력을 받는 방법을 고민해보세요. 간단한 방법으로는 입력되는 line을 배열에 추가하여, 배열의 길이가 2가 되면 rl.close();를 하는 방법입니다.
*/

var input = [];
var a = 6;
var b = 16;

const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});
var count = 0;
rl.on("line", function(line){
    count += 1
    input.push(parseInt(line));
    if(count == 2){
        rl.close();
    }
});
rl.on("close", function(){
    a += input[1];
    b += input[0];
    var result = a/b;
    var h = String(result)[2];
    var p = String(result)[3];
    var l = String(result)[4];
    if(h > 0){
        console.log(h+'할');
    }
    if(p > 0){
        console.log(p+'푼');
    }
    if(l > 0){
        console.log(l+'리');
    }
    process.exit;
});

//11. 문자열은 빼달라구(복기)
var str = '';
var result = '';
const readline = require("readline");
const rl = readline.createInterface({
    input : process.stdin,
    output : process.stdout,
});
rl.on("line", function(line){
    str = line;
    rl.close();
});
rl.on("close", function(){
    for(var i = 0; i <= str.length-1; i++){
        if(str[i] > 0){
            result += str[i];
        }
    }
    console.log(result);
    process.exit;
});


//12. 합격 여부 확인하기(복기)
var pf = false;
var scores = {
    "kor": 55,
    "mat": 75,
    "eng": 50
}
var avg = (scores.kor + scores.mat + scores.eng) / 3;
if(scores.kor >= 40 & scores.mat >= 40 & scores.eng >= 40 & avg >= 60){
    pf = true;
}
if(pf == true){
    console.log("pass");
}
else{
    console.log("fail");
}

//13. 짝수 판별기(복기)
result = ''
for(var i = 1; i < 101; i++){
    if(i % 2 == 0){
        result += i;
    }
}
console.log(result);

//14. 점심 메뉴 찾기(복기)
/*배열에 최근 먹은 음식들이 [점심, 저녁, 점심, 저녁, …] 순으로 들어가 있습니다.
지시사항을 따라 점심 메뉴만 화면에 출력하세요.
배열의 길이를 출력하세요.
*/
var foods = ["hamburger", "pasta", "curry", "chicken", "salad", "tteokbokki", "ramen", "pizza", "gimbap", "sushi"];
var lunch = [];
for(var i = 0; i < foods.length-1; i++){
    if(i % 2 == 0){
        lunch.push(foods[i]);
    }
}
console.log(lunch);
console.log(lunch.length);

//15. B로 시작하는 과일을 찾아줘(복기)

var foods = ['apple', 'banana', 'orange', 'blueberry', 'strawberry'];
var b_foods = foods.filter(f => f[0] === 'b');
console.log(b_foods);

//16. 특정 학생 정보 바꾸기(복기)


