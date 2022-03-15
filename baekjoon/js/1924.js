//1924

var input = [];
var month = 0;
var day = 0;
var count = 0;
var result = 0;
const readline = require("readline");
const rl = readline.createInterface({
    input : process.stdin,
    output : process.stdout,
});
rl.on("line", function(line){
    input = line.split(' ').map((el) => parseInt(el));
    month = input[0];
    day = input[1];
    rl.close();
});
rl.on("close", function(){
    var start_month = 1;
    var start_day = 1;
    while(start_month != month | start_day != day){
        if(start_month === 1 || start_month === 3 || start_month === 5 || start_month === 7 || start_month === 8 || start_month === 10 || start_month === 12){
            if(start_day < 31){
                count += 1;
                start_day += 1;
            }
            if(start_day == 31){
                if(start_month === 12){
                    break
                }
                else{
                    count += 1;
                    start_day = 1;
                    start_month += 1;
                }
            }
        }
        else if(start_month === 2){
            if(start_day < 28){
                count += 1;
                start_day += 1;
            }
            if(start_day == 28){
                count += 1;
                start_day = 1;
                start_month += 1;
                
            }
        }
        else if(start_month === 4 || start_month === 6 || start_month === 9 || start_month  === 11){
            if(start_day < 30){
                count += 1;
                start_day += 1;
            }
            if(start_day == 30){
                count += 1;
                start_day = 1;
                start_month += 1;
            }
        }
    }
    result = count % 7;
    if(result == 0){
        console.log("MON");
    }
    else if(result == 1){
        console.log("TUE");
    }
    else if(result == 2){
        console.log("WED");
    }
    else if(result == 3){
        console.log("THU");
    }
    else if(result == 4){
        console.log("FRI");
    }
    else if(result == 5){
        console.log("SAT"); 
    }
    else if(result == 6){
        console.log("SUN");
    }

});

