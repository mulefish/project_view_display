import Viewport from "./pages/Viewport/Viewport.js";



function App() {
  const height = window.innerHeight * 0.6
  const width = window.innerWidth
  return (
    <div>
      <Viewport height={height} width={width} />
      <hr />
    hello world
    </div>
  );
}

export default App;
