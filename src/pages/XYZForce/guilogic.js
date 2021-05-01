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

const NOT_SET = -99999
// Not JSX, just vanilla javascript
class Dot {
    constructor(id, parent, path) {
        this.id = id;
        this.parent = parent;
        this.path = path;
        this.sy = NOT_SET;
        this.sx = NOT_SET;
        this.angle = NOT_SET;
        this.x = NOT_SET;
        this.y = NOT_SET;
    }
}

//'sy': 0, 'sx': 0, 'angle': 0, 'parent': '_N', 'x': 0, 'y': 0, 'path': '..|src|redux|reducers.js', 'id': 'AF'

export {
    dimensions, Dot, findNewPoint
}