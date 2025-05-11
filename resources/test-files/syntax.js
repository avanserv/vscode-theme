// Variables and Constants
let variable = "I can change";
const constant = "I cannot change";

// Data Types
let number = 42;
let string = "Hello, World!";
let boolean = true;
let array = [1, 2, 3];
let object = { key: "value" };
let func = function() { return "I'm a function"; };
let undefinedVar;
let nullVar = null;

// Functions
function add(a, b) {
    return a + b;
}
const arrowFunction = (a, b) => a * b;

// Control Flow
if (boolean) {
    console.log("Boolean is true");
} else {
    console.log("Boolean is false");
}

for (let i = 0; i < array.length; i++) {
    console.log(array[i]);
}

while (number > 0) {
    console.log(number--);
}

// Classes
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    greet() {
        return `Hello, my name is ${this.name}`;
    }
}
const person = new Person("Alice", 30);
console.log(person.greet());

// Promises and Async/Await
const asyncFunction = async () => {
    const promise = new Promise((resolve) => setTimeout(() => resolve("Done!"), 1000));
    const result = await promise;
    console.log(result);
};
asyncFunction();

// Modules (ES6+)
// export const exportedFunction = () => "I'm exported!";
// import { exportedFunction } from './module.js';

// Error Handling
try {
    throw new Error("Something went wrong!");
} catch (error) {
    console.error(error.message);
}

// Destructuring
const { key } = object;
const [first, second] = array;

// Spread and Rest Operators
const newArray = [...array, 4, 5];
const newObject = { ...object, newKey: "newValue" };
const sum = (...args) => args.reduce((acc, val) => acc + val, 0);

// Template Literals
const templateLiteral = `Number: ${number}, String: ${string}`;

// Map, Filter, Reduce
const mappedArray = array.map(x => x * 2);
const filteredArray = array.filter(x => x > 1);
const reducedValue = array.reduce((acc, val) => acc + val, 0);

// Date and Time
const now = new Date();
console.log(now.toISOString());

// Regular Expressions
const regex = /hello/i;
console.log(regex.test("Hello, World!"));

// JSON
const jsonString = JSON.stringify(object);
const parsedObject = JSON.parse(jsonString);

console.log("JavaScript features demonstrated!");
