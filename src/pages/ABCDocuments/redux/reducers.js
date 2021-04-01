import TYPES from './types';

const initialState = {
    abcValue: [],
};

const API_STATUS = {
    GETTING: "dummy value"
}

export default function classifyDocumentsReducer(state = initialState, action) {
    switch (action.type) {
        case TYPES.ABC_SUCCESS:
            return {
                ...state,
                abcValue: action.abcDoc,
                status: null,
                error: null,
            };
        case TYPES.ABC_ERROR:
            return {
                ...state,
                error: action.error,
                status: null,
            };
        default:
            return state;
    }
}