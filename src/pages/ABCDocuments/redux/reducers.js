import TYPES from './types';
// import { API_STATUS } from 'common/constants';
//import { getListOfClassificationsViaRestfulEndpoint } from '../model/ClassifyDocumentController';

const initialState = {
    listOfClassificationsFromTheBackEnd: [],
};

const API_STATUS = {
    GETTING: "dummy value"
}

export default function classifyDocumentsReducer(state = initialState, action) {
    switch (action.type) {
        case TYPES.ABC_STARTED:
            console.log('%c STARTED', ' color:#ff00ff');

            return {
                ...state,
                status: API_STATUS.GETTING,
                error: null,
            };
        case TYPES.ABC_SUCCESS:
            console.log('%c SUCCESS' + JSON.stringify(action.abcDoc), ' color:#ff00ff');
            return {
                ...state,
                listOfClassificationsFromTheBackEnd: action.abcDoc,
                status: null,
                error: null,
            };
        case TYPES.ABC_ERROR:
            console.log('%c Failbot! ' + action.error, ' color:#ff0000');

            return {
                ...state,
                error: action.error,
                status: null,
            };
        default:
            return state;
    }
}