//입력 한 줄, 공백

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
    console.log(input);
    process.exit();
});

// 정수 리스트 입력

var list = [];
const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});
rl.on("line", function(line){
    list = line.split(" ").map((el) => parseInt(el));
    rl.close();
})
rl.on("close", function(){
    console.log(list);
    process.quit();
})

// 입력 여러 줄
var input = [];
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
    console.log(input);
    process.exit;
});

