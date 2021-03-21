// TODO: This ought to be called 'layout.js' 
import { useHistory } from 'react-router-dom';
import React from 'react'



const Home = () => {


    const history = useHistory()
    function gotoForceDirectedGraph() {
        history.push('/ForceDirectedGraph')
    }

    function gotoDiagram() {
        history.push('/Diagram')
    }

    const style_big = {
        margin: 10, fontSize: '300px', color: "#000"
    }
    const style_big2 = {
        margin: 10, fontSize: '270px', color: "#000"
    }

    const style_mid = {
        paddingTop: 20, fontSize: '20px', color: "#00ff00", paddingBottom: 20
    }

    return (
        <>
            <center>
                <table border='1'>
                    <tr>
                        <td valign='top'>

                            <button onClick={gotoForceDirectedGraph}>
                                <div style={style_big}>
                                    &#11619;
                    </div>
                                <hr></hr>
                                <div style={style_mid}>
                                    ForceDirectedGraph
                    </div>
                            </button>
                        </td>
                        <td>&nbsp;</td>
                        <td valign='top'>
                            <button onClick={gotoDiagram}>
                                <div style={style_big2}>
                                    &#10730;
                    </div>
                                <hr></hr>
                                <div style={style_mid}>
                                    Diagram/Flowchart
                    </div>


                            </button>
                        </td>
                    </tr>
                </table>

            </center>
        </>
    )

}

export default Home