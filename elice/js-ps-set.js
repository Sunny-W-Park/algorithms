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



