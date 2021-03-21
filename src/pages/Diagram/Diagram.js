import React from "react";
import { useHistory } from 'react-router-dom';

function Diagram() {
    const history = useHistory()

    function gotoHome() {
        history.push('/Home')
    }


    return (
        <h1>
            This will be a d3-dataviz dot lang diagram.
            <a href="https://renenyffenegger.ch/notes/tools/Graphviz/examples/index">https://renenyffenegger.ch/notes/tools/Graphviz/examples/index</a>


            <br />
            <button onClick={gotoHome}>gotoHome</button>

        </h1>
    );
};
export default Diagram