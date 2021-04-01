import React, { useState } from "react";

import { Graphviz } from 'graphviz-react';
import { Memory } from './memory.js';
import './style.css';

function Diagram() {
    const mem = new Memory()
    let [graf, setGraf] = useState(mem.getNext())
    function nextGraph() {
        setGraf(mem.getNext())
    }

    function loadFromText() {
        const x = document.getElementById("input").value;
        setGraf(x)
    }

    let working = `
    digraph D {
    
        subgraph cluster_p {
          label = "Parent";
      
          subgraph cluster_c1 {
            label = "Child one";
            a;
      
            subgraph cluster_gc_1 {
              label = "Grand-Child one";
               b;
            }
            subgraph cluster_gc_2 {
              label = "Grand-Child two";
                c;
                d;
            }
      
          }
      
          subgraph cluster_c2 {
            label = "Child two";
            e;
          }
        }
      }
    `
    function loadFromMemoryText() {
        document.getElementById("input").value = working
    }
    function saveToMemory() {
        working = document.getElementById("input").value
    }



    return (
        <>
            <button onClick={nextGraph}>nextGraphs</button>
            <button onClick={loadFromText}>load</button >
            <button onClick={loadFromMemoryText}>loadFromMemoryText</button >
            <button onClick={saveToMemory}>saveToMemory</button >
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
                            <textarea rows='100' cols='70' id='input' text=""></textarea>
                        </td>
                    </tr>
                </tbody>
            </table>
        </>
    );
};
export default Diagram