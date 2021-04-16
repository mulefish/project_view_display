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
    function gotoABCDocument() {
        history.push('/ABCDocuments')
    }

    function gotoSecondPass() {
        history.push('/SecondPass')
    }

    function gotoFauxForce() {
        history.push('/FauxForce')
    }

    const style_big = {
        margin: 10, fontSize: '180px', color: "#000"
    }
    const style_big2 = {
        margin: 10, fontSize: '180px', color: "#000"
    }

    const style_mid = {
        paddingTop: 20, fontSize: '20px', color: "#00ff00", paddingBottom: 20
    }

    return (
        <>
            <center>
                <table border='1'>
                    <tbody>
                        <tr>
                            <td valign='top'>

                                <button onClick={gotoFauxForce}>
                                    <div style={style_big}>
                                        🤖
                                    </div>
                                    <hr></hr>
                                    <div style={style_mid}>
                                        FauxForce
                                    </div>
                                </button>
                            </td>

                            <td valign='top'>
                                <button onClick={gotoForceDirectedGraph}>
                                    <div style={style_big}>
                                        ᛤ
                                        {/* 乒乓 */}
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

                            <td valign='top'>
                                <button onClick={gotoABCDocument}>
                                    <div style={style_big2}>
                                        🚀
                                        {/* 試 */}
                                    </div>
                                    <hr></hr>
                                    <div style={style_mid}>
                                        ABCDoc
                    </div>


                                </button>
                            </td>


                            <td valign='top'>
                                <button onClick={gotoSecondPass}>
                                    <div style={style_big2}>
                                        🐙
                                    </div>
                                    <hr></hr>
                                    <div style={style_mid}>
                                        SecondPass
                    </div>


                                </button>
                            </td>



                        </tr>
                    </tbody>

                </table>
                <a href="https://www.public.asu.edu/~rjansen/glyph_encoding.html">https://www.public.asu.edu/~rjansen/glyph_encoding.html</a>
            </center>
        </>
    )

}

export default Home