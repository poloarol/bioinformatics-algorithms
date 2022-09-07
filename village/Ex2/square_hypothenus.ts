

function calc_square_hypothenus(base: number, height: number): number {
    let square_base: number = Math.pow(base, 2);
    let square_height: number = Math.pow(height, 2);
    let square_hypothenus: number = square_base + square_height

    return square_hypothenus

}

let square_hypothenus = calc_square_hypothenus(3, 5)
console.log(square_hypothenus)
