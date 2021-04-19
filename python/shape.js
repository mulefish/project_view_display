function findNewPoint(x, y, angle, distance) {
    var result = {};

    result.x = Math.round(Math.cos(angle * Math.PI / 180) * distance + x);
    result.y = Math.round(Math.sin(angle * Math.PI / 180) * distance + y);

    return result;
}

let a = [0, 10, 45, 90, 180, 270, 350, 359, 360, 361, 1]
a.forEach((angle) => {
    const xy = findNewPoint(0, 0, angle, 100)
    console.log(`a: ${angle}\t\t${xy.x}\t\t${xy.y}`)
})

// var newPoint = findNewPoint(0, 0, 10, 200);
// console.log('newPoint:', newPoint);

var angle = 10;
var oppositeAngle = (angle + 180) % 360;
console.log(oppositeAngle);

