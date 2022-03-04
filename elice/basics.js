// 02. 자바스크립트의 변수

var fruit; // 변수 선언
fruit = "apple" // 변수 초기화
var fruit = "apple" // 변수 선언 + 초기화
console.log(fruit) // 변수 안의 데이터 확인

// 실습1. 변수 생성

var fruit = "apple";
var box = "banana";
document.write(fruit);
document.write(box);
var box = "tomato";
document.write(box);

document.writeln(변수명); // 출력값 사이에 공백 삽입

// 03. 자바스크립트 데이터 타입

var str1 = "Hello World"
var str2 = "20" // 문자 데이터
var str3 = "He\'s a boy" // 특수문자 입력

var func1 = function() {
    console.log("This is function 1");
} // 함수 생성
func1(); // 함수 호출

function func1() {
    console.log("This is function 1 as well");
}
func1();

function area(w, h){
    return w * h;
}
area(10, 20);

var result = area(10, 20);
console.log(result);
console.log(area(10, 20));

var fruit = ["사과", "배", "수박"];
console.log(fruit);
fruit[0] = "포도";

var student = {
    name: "sunwoo",
    age: 26,
    skills: ["js", "python"],
    sum: function(num1, num2){
        return num1 + num2;
    }
}

console.log(student[name]); // name 데이터 출력
student.name = "Park"; // name 데이터 입력

var unde; // undefined: 변수 안에 데이터를 입력하지 않은 상태
var empty = null; // null: 임의로 변수 안에 빈 데이터를 삽입

var t = true; // Boolean
var f = false;

// 실습 2. 데이터 타입 - 문자열

var str1 = "Hello World";
var str2 = "Nice to meet you";
var str3 = "She\'s a girl";
document.write(str1);
document.write(str2);
document.write(str3);

// 실습 3. 데이터 타입 - 숫자

var num1 = 10;
var num2 = 3.14;
document.write(num1+num2);

// 실습 4. 데이터 타입 - 함수

var sum = function(num1, num2){
    return num1+num2;
}
document.write(sum(10, 20));

function mul(num3, num4){
    return num3*num4;
}
document.write(mul(3, 4));

// 실습 5. 데이터 타입 - 배열

var fruit = ["Apple", "Banana"];
document.write(fruit);
document.write(fruit[0]);
fruit[0] = "Tomato"
document.write(fruit);

// 실습 6. 데이터 타입 - 객체

var student = {
    name: "Elice",
    age: 20,
    skills: ["Java", "HTML", "CSS", "JavaScript"],
    sum: function(num1, num2){
        return num1 + num2;
    }
}

student.name = "park";
document.write(student.name);
document.write(student.sum(10, 20));

// 실습 7. 데이터 타입 - undefined, null

var str1;
document.write(str1);
var empty = null;
document.write(empty);

// 실습 8. 데이터 타입 - Boolean

var t = true;
var f = false;
document.write(t, f);


