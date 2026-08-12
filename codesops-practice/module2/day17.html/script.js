function myfunc() {
  console.log("hello");
}

myfunc();

function myfunc1(name) {
  console.log(`hello ${name}`);
}

console.log(myfunc1("henok", "heran"));

function myfunc2(...name) {
  console.log(`hello ${name}`);
}

console.log(myfunc1("henok", "heran"));

// ... give an input in array form

// function expression

let greeting = function greeting() {
  console.log("hello world ");
};

console.log(greeting());

let sum = function sum(num1, num2) {
  return num1 + num2;
};
console.log(sum(55, 63));

// arrow function

let sum2 = (num1, num2) => {
  return num1 + num2;
};

console.log(sum2(65, 89));


function parent() {
    let name = "gudeta"
    return function child() {
        console.log(`my name ${name}`)
    }
}
let myname=parent()
console.log(myname())


// Definition of the higher-order function
function adder(num1, num2, fun) { 
    return fun(num1, num2); 
}

// Definition of the callback function
function summation(num1, num2) { 
    return num1 + num2; 
}

// Execution and logging
console.log(adder(6, 4, summation)); //


console.log(1=="1" || !{3})


// // let x= 10
// // y = x++
// // y = xx+

// console.log(typeof("15"))

// let isActive = false
// console.log("alazaconsole.log("hello")
// console.log("hello")
// r is active student")

// const total = 1200;
// if / else — four lines let fee; if (total >= 1000) { fee = 0; } else { fee = 60; }
// ternary — one line const fee2 = total >= 1000 
// let ishidden = true 
// let type = hidden?"password: "text"

// const score = 74;  // module mark
// if (score >= 70) { console.log("Pass — progress"); } else if (score >= 50) { console.log("Remedial plan"); } else { console
    
//     let paymentmethod = "CBE"




