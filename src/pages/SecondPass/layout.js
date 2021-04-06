// import React, { useEffect, useState } from "react";
// import * as d3 from "d3";
// const SecondPass = ({
//     getABCFunc,
//     abcValue,
// }) => {
//     return (
//         <>
//             Second pass
//         </>
//     );
// };
// export default SecondPass


import React, { Component } from 'react';
import * as d3 from 'd3'
import * as d3Graphviz from 'd3-graphviz';

var dotSrc = 'digraph  {a -> b}';

class SecondPass extends Component {
    setGraph() {
        console.log('DOT source =', dotSrc);
        d3.select(".graph").graphviz().renderDot(dotSrc);
    }

    render() {
        return (
            <div className="App">
                <header className="App-header">
                    <h1 className="App-title">Welcome to magjac&#39;s React hack</h1>
                </header>
                <script src="https://unpkg.com/viz.js@1.8.0/viz.js" type="javascript/worker"></script>

                <div className="graph">
                </div>
                <button className="square" onClick={() => this.setGraph()}>
                    {'Click me'}
                </button>
            </div>
        );
    }
}

export default SecondPass;