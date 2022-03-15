//12917

function solution(s) {
    var answer = '';
    var s_arr = [];
    var c_arr = [];
    for(var i = 0; i <= s.length-1; i++){
        if(s[i] === s[i].toUpperCase()){
            c_arr.push(s[i]);
        } 
        else{
        s_arr.push(s[i]);
        }
    };
    s_arr.sort(function(a, b){
        if(b > a){
            return 1;
        }
        else if(a === b){
            return 0;
        }
        else if(b < a){
            return -1;
        }
    });
    c_arr.sort(function(a, b){
        if(b > a){
            return 1;
        }
        else if(b === a){
            return 1;
        }
        else if(b < a){
            return -1;
        }
    });
    answer = s_arr.join('') + c_arr.join('');
    return answer;
}
