//2747

var N = 0;
const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});
rl.on("line", function(line){
    N = parseInt(line);
    rl.close();
});
rl.on("close", function(){
    var fibo = [];
    fibo.push(0);
    fibo.push(1);
    for(var i = 2; i <= 45; i++){
        fibo.push(fibo[fibo.length-1]+fibo[fibo.length-2]);
    }
    console.log(fibo[N]);
    process.exit();
});

