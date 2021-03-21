import { createStore } from 'redux';

export const ACTIONS = {
};

const initialState = {
};

function theReducer(state = initialState, action) {
    switch (action.type) {
        case "THis will never be hit": {
            let x = action['payload']
            return {
                ...state,
                income: x
            }
        }
        default:
            return state;
    }
}
const enableReduxDevTools = window.__REDUX_DEVTOOLS_EXTENSION__?.();
export function createReduxStore() {
    const store = createStore(theReducer, enableReduxDevTools);
    return store;
}
