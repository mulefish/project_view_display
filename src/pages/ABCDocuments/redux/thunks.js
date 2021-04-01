import actions from './actions';

const getABCFunc = () => async (dispatch) => {
    let dummy = [
        { r: Math.random() }
    ]
    dispatch(actions.ABC_SUCCESS(dummy));
};

export default {
    getABCFunc,
};