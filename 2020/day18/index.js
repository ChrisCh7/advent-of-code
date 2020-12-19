const decimal_eval = require('decimal-eval')

let fs = require('fs');

const multOp = decimal_eval.Operator.create('mult', 13, (left, right) => {
  return left * right;
});
//for part1 set the precedence of addOp to 13, for part2 to 14
const addOp = decimal_eval.Operator.create('add', 14, (left, right) => {
  return left + right;
});

decimal_eval.Parser.useOperator(multOp);
decimal_eval.Parser.useOperator(addOp);

let sum = 0;

fs.readFile('input.txt', 'utf8', function (err,data) {
  if (err) {
    return console.log(err);
  }
  
  let lines = data.split("\n");
  
  lines.forEach(line => {
    let new_line = line.replace(/\*/g, 'mult');
    new_line = new_line.replace(/\+/g, 'add');
    let res = decimal_eval.evaluate(new_line);
    sum+=res;
  });
  
console.log(sum);

});