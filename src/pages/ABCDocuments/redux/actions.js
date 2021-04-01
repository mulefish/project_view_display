import TYPES from './types';

function ABC_SUCCESS(abcDoc) {
    return {
        type: TYPES.ABC_SUCCESS,
        abcDoc
    }
}

// const abc_Failbot = () => ({
//     type: TYPES.ABC_ERROR,
//     error: 'It failed.',
// });

export default {
    ABC_SUCCESS,
    // abc_Failbot,
};