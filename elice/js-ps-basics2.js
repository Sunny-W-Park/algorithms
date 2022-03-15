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

//10. 타격왕이 될거야
//11. 문자열은 빼달라구
//12. 합격 여부 확인하기
//13. 짝수 판별기
//14. 점심 메뉴 찾기
//15. B로 시작하는 과일을 찾아줘
//16. 특정 학생 정보 바꾸기


