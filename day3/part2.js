const fs = require('fs');

const lines = fs.readFileSync('input1.txt', 'utf8');

const re = /:?mul\((?<num1>\d{1,3})\,(?<num2>\d{1,3})\)|(?<command>do\(\)|don't\(\))/gm;

const matches = Array.from(lines.matchAll(re));

let sum = 0;
let toggle_compute = true;

matches.forEach(match => {
    if (match.groups.num1 && match.groups.num2 && toggle_compute) {
        sum += parseInt(match.groups.num1) * parseInt(match.groups.num2);
    } else if (match.groups.command === "do()") {
        toggle_compute = true;
    } else if (match.groups.command === "don't()") {
        toggle_compute = false;
    }
});

console.log(sum);
