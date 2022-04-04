#!/usr/bin/node

function factorial (n) {
  const answer = 1;
  if (n > 1) {
    return n * factorial(n - 1);
  }
  return answer;
}

console.log(factorial(Number(process.argv[2])));
