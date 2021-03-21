//import Viewport from "./pages/ForceDirectedGraph/ForceDirectedGraph.js";
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom'
import Home from './pages/Home/index.js'
// import ForceDirectedGraph from './pages/ForceDirectedGraph/ForceDirectedGraph.js'
import ForceDirectedGraph from './pages/ForceDirectedGraph/index.js'
import Diagram from './pages/Diagram/Diagram.js'
// function App() {
//   const height = window.innerHeight * 0.6
//   const width = window.innerWidth
//   return (
//     <div>
//       <Viewport height={height} width={width} />
//       <hr />
//     hello world
//     </div>
//   );
// }

const App = () => {

  // routes.map((route, index) => {
  //   console.table(route.path, route.component, route.exact, index)
  // })

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
