const ss = require("./secret_sharing.js");
const big = require("./bigint_utils.js");

const key = "Transactions fundamentally change the state of the network. A transaction can be as simple as sending Ether to another account, or as complicated as executing a contract function or adding a new contract to the network. The defining characteristic of a transaction is that it writes (or changes) data. Transactions cost Ether to run, known as, and transactions take time to process. When you execute a contract's function via a transaction, you cannot receive that function's return value because the transaction isn't processed immediately. In general, functions meant to be executed via a transaction will not return a value; they will return a transaction id instead. So in summary, transactions:";
// const key = "test";
//console.log(utils.sqrt_bigint(4444444944444444444444444n));
// console.log(utils.signed_mod(4n,(-7n)));
// console.log(utils.signed_mod(-4n,(-7n)));
// console.log(utils.signed_mod(-4n,(7n)));
// console.log(big.encodeStr(key));

shares = ss.createShares(big.encodeStr(key), 4, 4);
// console.log(shares);
// console.log(ss.recoverKey(shares))
console.log(big.decode(ss.recoverKey(shares)));

// console.log(big.encodeStr(key).toString(16))
// console.log(big.decode(big.encodeStr(key)))