/**
 * @Author: helei
 * @Date:   2021-01-25
 * @Email:  v_heleihe@tencent.com
 * @Filename: main6.js
 * @Last modified by:   helei
 * @Last modified time: 2021-01-25
 */
/**
 * @Author: helei
 * @Date:   2021-01-25
 * @Email:  v_heleihe@tencent.com
 * @Filename: main5.js
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
		volumeCredits += Math.max(perf.audience - 30, 0);
		if ("comedy" === playFor(perf).type) volumeCredits += Math.floor(perf.audience / 5);

		result += `  ${playFor(perf).name}: ${format(amountFor(perf)/100)} (${perf.audience} seats)\n`;
		totalAmount += amountFor(perf);
	}
	result += `Almount owed is ${format(totalAmount / 100)}\n`;
	result += `You earned ${volumeCredits} credits\n`;
	return result;
}

function playFor(aPerformance) {
	return plays[aPerformance.playID]
}

function amountFor(aPerformance) {
	let result = 0;
	switch (playFor(aPerformance).type) {
		case "tragedy":
			result = 40000;
			if (aPerformance.audience > 30) {
				result += 1000 * (aPerformance.audience - 30);
			}
			break;
		case "comedy":
			result = 30000;
			if (aPerformance.audience > 20) {
				result += 10000 + 500 * (aPerformance.audience - 20);
			}
			break;
		default:
			throw new Error(`unknown type: ${playFor(aPerformance).type}`);
	}
	return result;
}

let res = statement(invoice, plays);
console.log(res);
