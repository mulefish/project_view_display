import React from "react";
// import * as d3 from "d3";
// import { Dot } from './logic.js'
import { dimensions, Dot, findNewPoint } from './guilogic.js'

const FauxForce = () => {



    return (

        <>
            <div className='wrapper' style={dimensions}>
                <canvas id='background' style={dimensions}></canvas>
                <canvas id='foreground' style={dimensions}></canvas>
            </div>

        </>
    );
};
export default FauxForce