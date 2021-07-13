import { BrowserRouter as Router, Switch, Route } from 'react-router-dom'
import Home from './pages/Home/index.js'
import SecondPass from './pages/SecondPass/index.js'
import ABCDocuments from './pages/ABCDocuments/index.js'

const App = () => {

  return (
    <>
      <Router>
        <Switch>
          <Route exact path="/">
            <Home />
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
        </Switch>
      </Router>

    </>
  )
}
export default App;
