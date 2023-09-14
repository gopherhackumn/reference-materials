const randRange = (hi) => {
  hi = BigInt(hi);
  const numDigits = (hi-1n).toString().length;
  let multiplier = '';
  while (multiplier.length < numDigits) {
    multiplier += Math.random().toString().split('.')[1];
  }
  multiplier = multiplier.slice(0, numDigits);
  const divisor = '1' + '0'.repeat(numDigits);
  const randomNum = (hi * BigInt(multiplier)) / BigInt(divisor);
  return 1n + randomNum;
}


const sqrt = (value) => {
    if (value < 0n) throw 'negative number is not supported'
    let x = value;
    let lastX = 0;
    for (let limit = 100; x !== lastX && limit; limit--) {
        lastX = x;
        x = (x + value / x) / 2n;
    }
    return x;
}

const pair = (int1, int2) => {
  var added = int1 + int2;
  return int2 + (added * (added + 1n)) / 2n;
};

const unpair = (num) => {
  var w = (sqrt(8n * BigInt(num) + 1n) - 1n)/ 2n;
  var t = (w * w + w) / 2n;
  var y = BigInt(num) - t;
  var x = w - y;
  return {x:x, y:y};
};

// return a new data type [ [0, 10**18], [0, 10**18]...]
function encodeStr(string) {
    var numberList = []; 
    var number = 0x0n, place = 0x1n;
    for (let i = 0; i < string.length; i++){
        number += BigInt(string.charCodeAt(i)) * place;
        place *= 0x1000n;
        if (place >= 10**18) {
            numberList.push(number);
            number = 0x0n;
            place = 0x1n; 
        }
    }
    if (number > 0x0n) numberList.push(number);
    return numberList;
}

function pad(num, size) {
    num = num.toString();
    while (num.length < size) num = "0" + num;
    return num;
}

// takes in data type [ [0, 10**18], [0, 10**18]...]
const decode = (keys) => {
  var output = "";
  for (let i = 0; i < keys.length; i++) {
    let key = keys[i]; 
    var bytes = []; 
    var mask = 0xffn;
    for (; key > 0n; key /= 0x1000n)
      bytes.push(Number(key & mask));
    output += String.fromCharCode.apply(null, bytes);
  }

  return output; 
  
};



module.exports = {
  randRange,
  sqrt,
  pair,
  unpair,
  encodeStr,
  decode,
};