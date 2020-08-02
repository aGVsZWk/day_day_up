import AAA from './index.jsx'


var a = 'Jspang'
// window.onload = function () {
//   var a = "胖"
// }
{
  let a = "胖"
}
console.log(a);



const arr1 = ['www', 'jspang', 'com']
let arr2 = arr1
arr2.push('shengHongYu')
console.log(arr1);



const arr3 = ['www', 'jspang', 'com']
let arr4 = [...arr1]
arr4.push('shengHongYu')
console.log(arr3);

let {a, b, c} = {a:10, b:20, c:30, d:40}

a
b
c
d
let result = `${a+b}`
result

let  json = {
    '0': 'jspang',
    '1': '技术胖',
    '2': '大胖逼逼叨',
    length:3
}

let arr=Array.from(json);
console.log(arr)
let arrr =Array.of('技术胖','jspang','大胖逼逼叨');
console.log(arrr);


let arar=['jspang','技术胖','前端教程'];

let t = arar.forEach((val,index)=>console.log(index,val));
t
console.log(t);


const os = require('os');
os

class Awesome {
  constructor() {
    console.log('yeah!')
  }
}
