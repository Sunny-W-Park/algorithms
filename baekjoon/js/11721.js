//11721

var str = '';
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
    var result = '';
    for(var i = 0; i <= str.length-1; i++){
        result += str[i];
        if(result.length == 10){
            console.log(result);
            result = '';
        }
    }
    console.log(result);
});

