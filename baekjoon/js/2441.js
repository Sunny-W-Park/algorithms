// 2441

var N = 0;
var blank = 0;
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
    while(N > 0){
        var star = '';
        for(var b = 0; b < blank; b++){
            star += ' ';
        }
        for(var i = 0; i < N; i++){
            star += '*'
        }
        console.log(star);
        N -= 1;
        blank += 1;
    }
});
