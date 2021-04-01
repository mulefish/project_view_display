import React, { useState } from "react";

import { Graphviz } from 'graphviz-react';
import { Memory } from './memory.js';
import './style.css';

function Diagram() {
    const mem = new Memory()
    const [graf, setGraf] = useState(mem.getDrawing(5))
    const [held, setHeld] = useState(mem.getDrawing(5))
    function getDrawing(id) {
        const x = mem.getDrawing(id);
        document.getElementById("input").value = x;
        setGraf(x);
    }
    function setDrawing(id) {
        const x = document.getElementById("input").value;
        mem.setDrawing(id, x)
        setGraf(mem.getDrawing(id));
    }
    function holding() {
        setHeld(document.getElementById("input").value);
        console.log("SET " + held)
    }
    function revert() {
        document.getElementById("input").value = held;
        console.log("GET " + held)
    }

    return (
        <>
            Display
            <button onClick={() => getDrawing(0)}>0</button>
            <button onClick={() => getDrawing(1)}>1</button>
            <button onClick={() => getDrawing(2)}>2</button>
            <button onClick={() => getDrawing(3)}>3</button>
            <button onClick={() => getDrawing(4)}>4</button>
            <button onClick={() => getDrawing(5)}>5</button>

            Save
            <button onClick={() => setDrawing(0)}>0</button>
            <button onClick={() => setDrawing(1)}>1</button>
            <button onClick={() => setDrawing(2)}>2</button>
            <button onClick={() => setDrawing(3)}>3</button>
            <button onClick={() => setDrawing(4)}>4</button>
            <button onClick={() => setDrawing(5)}>5</button>

            Temp
            <button onClick={holding}>Holding</button>
            <button onClick={revert}>Revert</button>

            <hr></hr>
            <table border='1'>
                <tbody>
                    <tr>
                        <td valign='top'>
                            <Graphviz
                                className='viewport'
                                dot={graf}
                                zoom={true}
                            />
                        </td>
                        <td valign='top'>
                            <textarea rows='100' cols='80' id='input' text></textarea>
                        </td>
                    </tr>
                </tbody>
            </table>
        </>
    );
};
export default Diagram