import { useEffect } from 'react';
import { PropTypes } from 'prop-types';
//import { Dropdown, Container } from 'semantic-ui-react';
//https://codesandbox.io/s/ql3q086l5q?file=/index.js

const SearchMechanism = ({
    getListOfClassificationsViaRestfulEndpoint,
    listOfClassificationsFromTheBackEnd,
}) => {

    function DOIT() {
        alert(" doit ")
        getListOfClassificationsViaRestfulEndpoint()
    }


    useEffect(() => {
        (async () => {
            await getListOfClassificationsViaRestfulEndpoint();
            console.log(
                JSON.stringify(listOfClassificationsFromTheBackEnd, null, 2)
            );
        })();
    }, [getListOfClassificationsViaRestfulEndpoint]);

    return <>Hello
        <button onClick={DOIT}>DOIT</button>

    </>;
};

SearchMechanism.propTypes = {
    listOfClassificationsFromTheBackEnd: PropTypes.array,
    getListOfClassificationsViaRestfulEndpoint: PropTypes.func,
};

export default SearchMechanism;