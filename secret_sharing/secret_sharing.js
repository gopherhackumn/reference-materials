const sm = require("./secure_math.js");
const big = require("./bigint_utils.js");

const _PRIME = BigInt(2 ** 127) - 1n;
const _JSCAP = 2**60;

const createShares = (keys, numShares, minimum, mod = _PRIME) => {
  if (minimum === undefined) minimum = numShares;
  var stackedShares = [...Array(numShares)].map((_)=> []);
  
  const _createShares = (key) => {
    // generate a random polynomial with key as y-intercept
    var coefficients = [key];
    for (i = 1n; i < minimum; i++) {
      coefficients.push(big.randRange(_JSCAP));
    }
    // console.log(coefficients);
    // prime mod to evaluate over finite field
    return [...Array(numShares).keys()]
    .map((i) => [big.pair(BigInt(i + 1), sm.polynomial(BigInt(i + 1), coefficients, mod))]);
  }

  for(let i = 0; i < keys.length; i++) {
    let key = keys[i]; 
    const shares = _createShares(key);
    stackedShares = stackedShares.map((arr,i) => arr.concat(shares[i]));
  }

  return stackedShares;
 
};

const recoverKey = (stackedShares, mod = _PRIME) => { 
  const stackCount = stackedShares[0].length; 
  var output = [];
  for (let i = 0; i < stackCount; i++) {
    const shares = stackedShares.map(arr=>arr[i]);
    var points = shares.map(big.unpair);
  
    output.push(sm.interpolate(points, mod));
  }
  return output; 
};

module.exports = {createShares, recoverKey};