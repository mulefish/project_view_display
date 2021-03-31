import actions from './actions';
// import apiClient from 'common/util/api-client';

const getListOfClassificationsViaRestfulEndpoint = () => async (dispatch) => {
    dispatch(actions.abc_itHasBegan());
    let dummy = [
        { id: "one", classification: "kittycat" },
        { id: "two", classification: "dino" },
        { id: "three", classification: "eebboo" },
        { r: Math.random() }
    ]
    dispatch(actions.abc_it_worked(dummy));
    //    dispatch(actions.abc_Failbot(error));
};

export default {
    getListOfClassificationsViaRestfulEndpoint,
};