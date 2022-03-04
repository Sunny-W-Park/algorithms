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


// 04. 자바스크립트의 프로퍼티와 메서드

// 문자열 프로퍼티와 메서드
var str1 = "Hello World";
str1.length;
str1.charAt(0);
str1.split(" ");

// 배열의 프로퍼티와 메서드
var fruit = ["a", "b", "c"];
fruit.length;
fruit.push("딸기"); // 배열 뒤 삽입 (python append)
fruit.unshift("레몬"); // 배열 앞 삽입
fruit.pop(); // 배열 뒤 데이터 제거 (python pop)
fruit.shift(); // 배열 앞 데이터 제거

// math의 수학 연산 메서드
Math.abs(-3); //절대값
Math.ceil(0.3); //올림
Math.floor(10.9) //내림
Math.random(); //임의의 숫자 출력

// 문자의 숫자 전환
parseInt("20.6"); // 문자 -> 정수
parseFloat("20.6"); // 문자 -> 실수

// 실습 9. 프로퍼티와 메서드 - 문자열
var str1 = "Hello World";
a = str1.length;
b = str1.charAt(0);
c = str1.split(" ");
document.write(a, b, c); 

// 실습 10. 프로퍼티와 메서드 - 배열
var fruit = ["Apple", "Banana", "Tomato"];
a = fruit.length;
fruit.push("A");
fruit.unshift("B");
document.write(a, fruit);
fruit.pop();
fruit.shift();
document.write(fruit);

// 실습 11. 프로퍼티와 메서드 - Math
document.write(Math.abs(-3), Math.ceil(0.3), Math.floor(0.9), Math.random());

// 실습 12. 프로퍼티와 메서드 - 문자의 숫자 변환
var str1 = "20.14";
a = parseInt(str1);
b = parseFloat(str1);
document.write(a, b);

// 보조자료 - 삼각형의 넓이를 구하는 함수 생성
function triangle(width, height){
    return width * height / 2;
}
document.write(triangle(width, height));

// 보조자료 - 배열 안의 배열 데이터에 접근
document.write(arrTest[1][2])


