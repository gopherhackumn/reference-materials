const polynomial = (x, coefficients, mod) => {
  var result = 0n;
  for (const coefficient of coefficients.slice().reverse()) {
    result *= x;
    result += coefficient;
    result %= mod;
  }
  return result;
};

const x_gcd = (a, b) => {
  // console.log("xgcd");
  var x = 0n, lastX = 1n;
  while (b != 0n) {
    // console.log(b)
    let quot = a / b;
    let tempa = a;
    a = b;
    b = tempa % b;
    let tempx = x;
    x = (lastX - quot * x);
    lastX = tempx;
  }
  return lastX;
};

const interpolate = (points, mod, x = 0n) => {
  var mod_div = (num, den) => num * x_gcd(den, mod);
  // mod_div finds num / den modulo prime p
  // return satisfies: den * _divmod(num, den, p) % p == num
  var x_arr = points.map((point) => point.x);
  var y_arr = points.map((point) => point.y);
  var nums = [];
  var dens = [];
  for (const [idx, cur] of x_arr.entries()) {
    const others = x_arr.filter((_, i) => i != idx);
    nums.push(others.map(other => x - other).reduce((x, y) => x * y));
    dens.push(others.map(other => cur - other).reduce((x, y) => x * y));
  }
  var den = dens.reduce((x, y) => x * y);
  var num = y_arr
    .map((y, i) => mod_div(nums[i] * den * y % mod, dens[i])).reduce((x, y) => x + y);
  return mod_div(num, den) % mod + mod;
};

module.exports = {polynomial, interpolate};