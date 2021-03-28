import { ABCDocumentsReducer as abcDocuments } from '../pages/ABCDocuments/redux';
import { combineReducers } from 'redux';

const rootReducer = combineReducers({
    abcDocuments
});
export default rootReducer;