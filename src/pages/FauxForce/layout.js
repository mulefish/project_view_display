import React from "react";
// import * as d3 from "d3";
// import { Dot } from './logic.js'

const FauxForce = ({
    getABCFunc,
    abcValue,
}) => {
    const dimensions = {
        width: window.innerWidth + 'px',
        height: window.innerHeight * 0.61 + '500px'
    };
    return (
        <>
            <div className='wrapper' style={dimensions}>
                <canvas id='background' width={dimensions.width} height={dimensions.height} style={dimensions}></canvas>
                <canvas id='foreground' width={dimensions.width} height={dimensions.height} style={dimensions}></canvas>
            </div>

        </>

    );
};
export default FauxForce