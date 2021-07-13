import React, { useEffect, useState } from "react";
const SecondPass = ({
    getABCFunc,
    abcValue,
    kittyValue,
    setKittyCat

}) => {
    const [points, setPoints] = useState([])
    function showValue() {
        getABCFunc()
    }

    function setKittyCatValue() {
        let tmp = [
            'a',
            'b',
            Math.random()
        ]
        setKittyCat(tmp)
    }


    return (
        <>
            SecondPass
            <hr></hr>
            <button onClick={showValue}>showValue</button>
            {JSON.stringify(abcValue, null, 10)}

            <br></br>
            kittyValue
            <button onClick={setKittyCatValue}>setKittyCatValue</button>
            {JSON.stringify(kittyValue, null, 10)}


        </>

    );
};
export default SecondPass





