/**
 * @Author: helei
 * @Date:   2021-01-28
 * @Email:  v_heleihe@tencent.com
 * @Filename: main16.js
 * @Last modified by:   helei
 * @Last modified time: 2021-01-28
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

function createStatementData (invoice, plays) {
	const statementData = {};
	statementData.customer = invoice.customer;
	statementData.performances = invoice.performances.map(enrichPerformance);
	statementData.totalAmount = totalAmount(statementData);
	statementData.totalVolumeCredits = totalVolumeCredits(statementData);
	return statementData;

	function enrichPerformance (aPerformance) {
		const result = Object.assign({}, aPerformance);
		result.play = playFor(result);
		result.amount = amountFor(result);
		result.volumeCredits = volumeCreditsFor(result);
		return result;

		function playFor(aPerformance) {
			return plays[aPerformance.playID]
		}

		function volumeCreditsFor(perf) {
			let result = 0;
			result += Math.max(perf.audience - 30, 0);
			if ("comedy" === perf.play.type) result += Math.floor(perf.audience / 5);
			return result;
		}

		function amountFor(aPerformance) {
			let result = 0;
			switch (aPerformance.play.type) {
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
					throw new Error(`unknown type: ${aPerformance.play.type}`);
			}
			return result;
		}
	}

	function totalAmount (data) {
		return data.performances.reduce((total, p) => total + p.amount, 0)
	}

	function totalVolumeCredits (data) {
		return data.performances.reduce((total, p) => total + p.volumeCredits, 0);
	}
}

function statement (invoice, plays) {
	return renderPlainText(createStatementData(invoice, plays));
}


function renderPlainText (data) {
	let result = `Statement for ${data.customer}\n`;
	for (let perf of data.performances) {
		result += `  ${perf.play.name}: ${usd(perf.amount)} (${perf.audience} seats)\n`;
	}
	result += `Almount owed is ${usd(data.totalAmount)}\n`;
	result += `You earned ${data.totalVolumeCredits} credits\n`;
	return result;

	function usd(aNumber) {
		return new Intl.NumberFormat("en-US",
			{style: "currency", currency: "USD", miniumFractionDigits: 2}
		).format(aNumber/100);
	}
}

function htmlStatement (invoice, plays) {
	return renderHtml(createStatementData(invoice, plays));
}

function renderHtml (data) {
	let result = `<h1>Statement for ${data.customer}</h1>\n`;
	result += "<table>\n"
	result += "<tr><th>play</th><th>seats</th><th>cost</th>\n";
	for (let perf of data.performances) {
		result += ` <tr><td>${perf.play.name}</td><td>${perf.audience}</td>`;
		result += `<td>${usd(perf.amount)}</td></tr>\n`;
	}
	result += "</table>\n";
	result += `<p>Amount owed is <em>${usd(data.totalAmount)}</em></p>\n`;
	result += `<p>You earned <em>${usd(data.totalVolumeCredits)}</em> credits</p>\n`;
	return result;

	function usd(aNumber) {
		return new Intl.NumberFormat("en-US",
			{style: "currency", currency: "USD", miniumFractionDigits: 2}
		).format(aNumber/100);
	}
}



let res = htmlStatement(invoice, plays);
console.log(res);
