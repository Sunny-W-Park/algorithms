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




