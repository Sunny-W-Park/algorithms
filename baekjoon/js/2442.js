//2442

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
    var len = 2*N-1;
    var front = 0;
    var end = 0;
    for(var i = 1; i <= len; i+=2){
        front = (len-i)/2;
        var result = '';
        for (var f = 0; f < front; f++){
            result += ' ';
        }
        for (var s = 0; s < i; s++){
            result += '*';
        }
        console.log(result);   
    }
    process.exit();
});

