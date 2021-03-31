import TYPES from './types';

const abc_itHasBegan = () => ({
    type: TYPES.ABC_STARTED,
});

// const abc_it_worked = (abcDoc) => ({
//     type: TYPES.ABC_SUCCESS,
//     abcDoc,
// });

function abc_it_worked(abcDoc) {
    console.log("abcDoc: " + JSON.stringify(abcDoc, null, 2))
    return {
        type: TYPES.ABC_SUCCESS,
        abcDoc
    }
}

const abc_Failbot = () => ({
    type: TYPES.ABC_ERROR,
    error: 'Mr. abc_Failbot says Oh No!',
});

export default {
    abc_itHasBegan,
    abc_it_worked,
    abc_Failbot,
};

