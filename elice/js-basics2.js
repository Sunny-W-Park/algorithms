//1. 연산자

//증감 연산자
var num = 10;
console.log(++num); // num+1 후 num 출력
console.log(--num); // num-1 후 num 출력
console.log(num++); // num 출력 후 num+1
console.log(num--); // num 출력 후 num-1

//비교 연산자
// == : 값이 같다 
// !== :  값이 같지 않다
// === :  값 and 데이터 타입이 같다

//실습1. 산술 연산자
document.write(20 + 10);
document.write(20 - 10);
document.write(20 * 10);
document.write(20 / 10);
document.write(20 % 10);

document.write("20" + "10");
document.write("20" - "10");
document.write("20" * "10");
document.write("20" / "10");
document.write("20" % "10");

document.write("Elice " + "Lee");

//실습2. 증감 연산자
var num = 20;
document.write(++num);
document.write(--num);
document.write(num++);
document.write(num);
document.write(++num);
document.write(num);

//실습3. 비교 연산자
document.writeln(10 == 10, 10 === 10);
document.writeln(10 == "10", 10 === "10");
document.writeln(10 !== 20);
document.writeln(10 > 20, 10 >= 20, 10 < 20, 10 <= 20);

//실습4. 논리 연산자
document.write(10 === 10  && 20 === 30);
document.write(10 === 10 || 20 === 30);

//2. 조건문
// if () {} else {}
// if () {} else if {} else {}

//실습5. 조건문 - if문

var a = 20;
var b = 40;

if (a < b){
    document.write("a < b");
}

//실습6. 조건문 - if~else 문

var a = 40;
var b = 20;

if (a < b){
    document.write("a < b");
}
else{
    document.write("a > b");
}

//실습7. 조건문 - else if 문

var a = 20;
var b = 40;
var c = 60;

if (a > b){
    document.write("a > b");
]                                                                     
else if (b > c){
    document.write("b > c");
}
else if (a < c){
    document.write("a < c");
}
else if (b < c){
    document.write("b < c");
}
else {
    document.write("모든 조건을 만족하지 않는다.");
}

//실습8. 조건문 - 중첩 if문

var a = 3;
var b = 6;

if (a != b){
    if (a > b){
        document.write("a > b");
    }
    else {
        document.write("a < b");
    }
}
else {
    document.write("a == b");
}

//3. 반복문

//for문
//for(초기화한 변수값; 조건; 증감표시){수행 명령}
for (var i = 0; i < 10; i++){
    console.log(i);
}
//0, 1, 2, 3.. 9

//while문
//while(조건){ 수행 명령 }
var num = 0;
while (var < 10){
    console.log(num);
    num++;
}
//0, 1, 2, 3.. 9

//do~while문
//do{수행할 명령} while(조건);
//while 조건과 관계 없이, do 명령을 무조건 실행부터 한다.
var i = 12;
do {
    console.log(i);
    i++;
}
while (i < 10);

//실습9. 반복문 - while 문
var num = 0;
while (num < 10){
    document.write(num);
    num++;
}

//실습10. 조건문- do~while 문
var i = 12;
do {
    document.write(i);
    i++;
}
while (i < 10)

//실습11. for문
for(var i = 1; i < 10; i++){
    document.write(2*i);
}

//4. 자바스크립트의 활용
//주사위 게임
//Math.random(): 0에서 1사이에 있는 난수 출력
var dice = Math.floor(Math.random() * 6) + 1

//소수 출력
function isPrime(n){
    var divisor = 2;
    while(n > divisor){
        if(n % divisor === 0){
            return false;
        } else {
            divisor++;
        }
    } return true;
}

//문자열 거꾸로 출력하기
function reverse(str){
    var reverStr = '';
    for (var i = str.length-1; i >= 0; i--){
        reverStr = reverStr + str.charAt(i);
    }
    return reverStr;
}
//str.charAt(idx): 문자열의 idx번째 문자
console.log(reverse('Hello'));


//실습12 - 주사위 게임 만들기
document.write(Math.floor(Math.random() * 6) + 1)

//실습13 - 소수 출력하기
function isPrime(n){
    if(n === 1){
        return false;
    }
    else{
        var divisor = 2;
        while(divisor < n){
            if(n % divisor === 0){
                return false;
            }
            else{
                divisor++;
            }
        }
        return true;
    }
}
for(var i = 1; i <= 10; i++) {
    document.writeln(i, isPrime(i));
}

//실습14 - 문자열 거꾸로 출력하기
function reverse(str){
    var reverStr = "";
    for(var i = str.length-1; i >= 0; i--){
        reverStr = reverStr + str.charAt(i);
    }
    return reverStr;
}

//보조자료 - 구구단 만들기
function timesTable(n){
    for(var i = 1; i < 10; i++){
        document.writeln(n, "\n", "x", "\n", i, "\n", "=", "\n", n*i);
        document.write('<br>');
    }
}
timesTable(2); // 2단만 출력
timesTable(3); // 3단만 출력

//보조자료 - 반복문으로 구구단 완성하기
for(var i = 2; i < 10; i++){
    for(var j = 1; j < 10; j++){
        document.writeln(i, "\n", "x", "\n", j, "\n", "=", "\n", i*j);
        document.write('<br>');
    }
}
