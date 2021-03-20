import React, { useRef, useEffect, useState } from "react";
import * as d3 from "d3";

let pieces = []
class Dot {
    constructor(id, x, y) {
        this.x = x;
        this.y = y;
        this.id = id;
        this.r = 20
    }
}

let showLetter = true
let ids = []
function addPieceIntoDom(piece) {
    alert(" hello showLetter \n" + JSON.stringify(piece, null, 2))
    ids.push(piece.id)
    let p = d3.select('#graph')
        .append('svg:g')
        .data([{
            'id': piece.id,
        }])
        .attr('transform', 'translate(' + piece.x + ',' + piece.y + ')')
        .attr('id', piece.id)
        .call(d3.drag()
            .on("start", dragstarted)
            .on("drag", dragged)
            .on("end", dragended));

    let background = p.append('svg:circle')
        .attr('fill-opacity', 0.1)
        .attr('stroke', '#000')
        .attr('stroke-width', 2)
        .attr('r', piece.r)
    if (showLetter == true) {
        let foreground = p.append('svg:text')
            .text(piece.id)
            .attr('y', '.1em')
            .style("font-size", piece.size + "px")
            // .attr('transform', 'translate(' + [0, piece.r / 4] + ')')
            .attr('transform', 'translate(' + [10, 10] + ')')
            .attr('text-anchor', 'middle')
            .attr('font-weight', 700)
            .attr('font-family', 'Helvetica')
            .attr('fill', '#000000')
            .attr('stroke', 'none')
            .attr('pointer-events', 'none')
    }
}

function dragstarted(d) {
    let piece = pieces[d.id]
    piece.sx = piece.x // d3.event.x // needed for snap back ability
    piece.sy = piece.y // d3.event.y // needed for snap back ability
}

function dragged(d) {
    d3.select(this).attr("transform", "translate(" + (d.x = d3.event.x) + ',' + (d.y = d3.event.y) + ')');
}

function dragended(d) {
    const x = d3.event.x
    const y = d3.event.y
    d3.select(this).classed("active", false);
    let piece = pieces[d.id]
    d3.select(this).attr("transform", "translate(" + (d.x = piece.sx) + ',' + (d.y = piece.sy) + ')');
}




export default () => {
    const container = useRef(null);
    const [num, setNum] = useState(1);


    useEffect(() => {



        let points = []
        points.push({ "x": 120, "y": 120 })

        for (let key in points) {
            let p = new Dot(key, points[key].x, points[key].y)
            pieces[key] = p
            addPieceIntoDom(p)

        }
    })

    useEffect(() => {
        const d = new Dot("hello", 20, 20)
        pieces.push(d)
        let p = new Dot(d.id, d.x, d.y)

        if (container.current) {
            const data = new Array(num).fill(20);
            const root = d3.select(container.current);

            //const render = root.selectAll("rect").data(data);

            // render
            //     .enter()
            //     .append("rect")
            //     .attr("fill", "red")
            //     .attr("width", 20)
            //     .attr("height", 20)
            //     .attr("x", (d, i) => d * i)
            //     .attr("y", (d, i) => d * i)
            //     .text(d => d);



            //render.exit().remove();
        }
    }, [container, num]);

    return (
        <div>
            <input
                type="number"
                max="15"
                min="0"
                onChange={e => setNum(parseInt(e.target.value, 0))}
                value={num}
            />{" "}
      Add or remove to test
            <br />
            <svg id="graph"
                style={{
                    marginTop: 20, width: '100%', height: 300, background: "#eee"
                }}
                ref={container}
            />
        </div>
    );
};
