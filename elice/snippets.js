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

// 입력 여러 줄

var N = 0; //N개 줄
var count = 0; //입력 횟수
var result = [];
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
        //
    }
    if(count > N){
        rl.close()
    }
})
rl.on("close", function(){
    console.log(result);
    process.quit();
})

