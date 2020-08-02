let array = [1, 5 ,6 ,7, 4, 2, 3]

for (var i = 0; i < array.length; i++) {
  for (var j = 0; j < array.length; j++) {
    if (array[j] > array[j+1]){
      let t = array[j]
      array[j] = array[j+1]
      array[j+1] = t
    }
  }
}

console.log(array);
