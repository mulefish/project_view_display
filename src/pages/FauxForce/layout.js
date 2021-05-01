import React, { useEffect } from 'react';
import { data } from './data.js'
import { dimensions, Dot, findNewPoint } from './guilogic.js'

const FauxForce = () => {

    useEffect(() => {
        var c = document.getElementById("background");
        var ctx = c.getContext("2d");
        ctx.lineWidth = 1;
        ctx.strokeRect(0, 0, 100, 100);


    }, data)


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