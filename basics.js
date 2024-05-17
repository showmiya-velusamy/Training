
let t1 = [80, 90];
let t2 = [50, 60];
let t3 = [...t1, ...t2];
console.log(t3);
//   [80, 90, 50, 60]

//   Math operation
console.log(Math.max(6, 7, 4)); // Accepts n no. of argument

let heights = [120, 140, 190, 80, 170]; // object
//   console.log(
//     Math.max(heights[0], heights[1], heights[2], heights[3], heights[4])
//   );
console.log(Math.max(heights)); // NaN
console.log(Math.max(...heights)); // 190

//   ... rest
function own_max(...nums) {
    // code
    return nums;
}
console.log(own_max(5, 6, 10));
console.log(own_max(5, 6, 10, 7, 80, 60));