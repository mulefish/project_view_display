import { BrowserRouter as Router, Switch, Route } from 'react-router-dom'
import Home from './pages/Home/index.js'
import ForceDirectedGraph from './pages/ForceDirectedGraph/index.js'
import SecondPass from './pages/SecondPass/index.js'
import Diagram from './pages/Diagram/Diagram.js'
import ABCDocuments from './pages/ABCDocuments/index.js'
import FauxForce from './pages/FauxForce/index.js'

const App = () => {

  return (
    <>
      <Router>
        <Switch>
          <Route exact path="/">
            <Home />
          </Route>
          <Route exact path="/ForceDirectedGraph">
            <ForceDirectedGraph />
          </Route>
          <Route exact path="/Diagram">
            <Diagram />
          </Route>
          <Route exact path="/Home">
            <Home />
          </Route>
          <Route exact path="/ABCDocuments">
            <ABCDocuments />
          </Route>
          <Route exact path="/SecondPass">
            <SecondPass />
          </Route>
          <Route exact path="/FauxForce">
            <FauxForce />
          </Route>


          {/* <Route exact path="/create">
            <CreateAccountInit />
          </Route>
          <Route exact path="/success">
            <SuccessInit />
          </Route>
          <Route exact path="/sorry">
            <SorryInit />
          </Route> */}
        </Switch>
      </Router>

    </>
  )
}
export default App;
