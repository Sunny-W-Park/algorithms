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
}
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

