const dimensions = {
    width: window.innerWidth + 'px',
    height: window.innerHeight * 0.61 + '500px'
};

function findNewPoint(x, y, angle, distance) {
    var result = {};

    result.x = Math.round(Math.cos(angle * Math.PI / 180) * distance + x);
    result.y = Math.round(Math.sin(angle * Math.PI / 180) * distance + y);

    return result;
}


// Not JSX, just vanilla javascript
class Dot {
    constructor(id, x, y) {
        this.x = x;
        this.y = y;
        this.id = id;
        this.r = 20
    }
}


export {
    dimensions, Dot, findNewPoint
}