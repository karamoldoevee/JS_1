var nums_1 = [1, 5, 12, 4, 3];

var nums_2 = [2, 3, 4, 5, 6, 7, 8, 9, 10];

var nums_3 = [3, 10, 17];

function average(nums) {
    return nums.reduce((a, b) => (a + b)) / nums.length;
}

console.log(average(nums_1));
console.log(average(nums_2));
console.log(average(nums_3));