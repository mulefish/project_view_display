class Node {
    constructor(name, generation, id) {
        this.name = name;
        this.generation = generation;
        this.id = id;
        this.chilren = new Set();
        this.pid = undefined;
    }
    put(child) {
        this.chilren.add(child)
    }
}
function convertRawData_toReadyData(data) {
    let matrix = [];
    let nodes = [];
    let most = 0;
    data.forEach((entry, i) => {
        console.log(i, entry)
        const ary = entry.dir.split("|");
        if (ary.length > most) {
            most = ary.length;
        }
        matrix.push(ary);
    })
    for (let i = 0; i < most; i++) {
        nodes[i] = {};
    }
    matrix.forEach((ary) => {
        for (let j = 0; j < ary.length; j++) {
            let id = ary[j];
            const a = ary[j];
            if (!nodes[j].hasOwnProperty(a)) {
                nodes[j][a].put(b)
            }
        }
    })
    return nodes;
}

if (require.main === module) {
    // SELF TEST
    //
    const path = "../../../public/client_app_03_20.json";
    const data = require(path);
    let nodes = convertRawData_toReadyData(data); // Map of Objects
    nodes.forEach((H, i) => {
        for (let k in H) {
            let obj = H[k];
            console.log(obj)
        }
    })
}
try {
    module.exports = { convertRawData_toReadyData };
} catch (boom) {
    console.log(boom);
}