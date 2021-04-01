//import { useEffect } from 'react';
import { PropTypes } from 'prop-types';

const SearchMechanism = ({
    getABCFunc,
    abcValue,
}) => {

    function showValue() {
        getABCFunc()
    }


    // useEffect(() => {
    //     (async () => {

    //         await getABCFunc();
    //         console.log(
    //             JSON.stringify(abcValue, null, 20)
    //         );
    //     })();
    // }, [getABCFunc]);

    return <>Hello
        <button onClick={showValue}>showValue</button>

        { JSON.stringify(abcValue, null, 10)}

    </>;
};

SearchMechanism.propTypes = {
    abcValue: PropTypes.array,
    getABCFunc: PropTypes.func,
};

export default SearchMechanism;