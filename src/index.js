import React, { StrictMode } from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import { Provider } from 'react-redux';
import { createReduxStore } from './redux';

ReactDOM.render(
  <StrictMode>
    <Provider store={createReduxStore()}>
      <App />
    </Provider>
  </StrictMode>,
  document.getElementById('root')
);