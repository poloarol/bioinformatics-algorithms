function calc_square_hypothenus(base, height) {
    var square_base = Math.pow(base, 2);
    var square_height = Math.pow(height, 2);
    var square_hypothenus = square_base + square_height;
    return square_hypothenus;
}
var square_hypothenus = calc_square_hypothenus(3, 5);
console.log(square_hypothenus);
