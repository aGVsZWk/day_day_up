/**
 * @Author: helei
 * @Date:   2021-01-25
 * @Email:  v_heleihe@tencent.com
 * @Filename: main2.js
 * @Last modified by:   helei
 * @Last modified time: 2021-01-25
 */
/**
 * @Author: helei
 * @Date:   2021-01-25
 * @Email:  v_heleihe@tencent.com
 * @Filename: main.js
 * @Last modified by:   helei
 * @Last modified time: 2021-01-25
 */
let invoice = {
	"customer": "Bigco",
	"performances": [
		{
			"playID": "hamlet",
			"audience": 55
		},
		{
			"playID": "as-like",
			"audience": 35
		},
		{
			"playID": "othello",
			"audience": 40
		}
	]
};

let plays = {
	"hamlet": {"name": "Hamlet", "type": "tragedy"},
	"as-like": {"name": "As you like it", "type": "comedy"},
	"othello": {"name": "Othello", "type": "tragedy"}
}

function statement (invoice, plays) {
	let totalAmount = 0;
	let volumeCredits = 0;
	let result = `Statement for ${invoice.customer}\n`;
	const format = new Intl.NumberFormat("en-US",
		{style: "currency", currency: "USD", miniumFractionDigits: 2}
	).format;
	for (let perf of invoice.performances) {
		const play = plays[perf.playID];
		let thisAmount = amountFor(perf, play);
		volumeCredits += Math.max(perf.audience - 30, 0);
		if ("comedy" === play.type) volumeCredits += Math.floor(perf.audience / 5);

		result += `  ${play.name}: ${format(thisAmount/100)} (${perf.audience} seats)\n`;
		totalAmount += thisAmount;
	}
	result += `Almount owed is ${format(totalAmount / 100)}\n`;
	result += `You earned ${volumeCredits} credits\n`;
	return result;
}

function amountFor(perf, play) {
	let thisAmount = 0;
	switch (play.type) {
		case "tragedy":
			thisAmount = 40000;
			if (perf.audience > 30) {
				thisAmount += 1000 * (perf.audience - 30);
			}
			break;
		case "comedy":
			thisAmount = 30000;
			if (perf.audience > 20) {
				thisAmount += 10000 + 500 * (perf.audience - 20);
			}
			break;
		default:
			throw new Error(`unknown type: ${play.type}`);
	}
	return thisAmount;
}

let res = statement(invoice, plays);
console.log(res);
