import React, { useEffect, useState } from "react";

//import * as d3 from "d3";
import { Graphviz } from 'graphviz-react';
import { Memory } from './memory.js';

function Diagram() {
    const mem = new Memory()
    let [graf, setGraf] = useState(mem.getNext())
    function nextGraph() {
        setGraf(mem.getNext())
    }
    return (
        <>
            {mem.index}
            <button onClick={() => nextGraph()}>nextGraph s</button>
            <hr></hr>
            <table border='1'>
                <tbody>
                    <tr>
                        <td>
                            <Graphviz
                                dot={graf}
                            />
                        </td>
                    </tr>
                </tbody>
            </table>
        </>
    );
};
export default Diagram