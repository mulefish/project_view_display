import { connect } from 'react-redux';

import ABCDocuments from './layout';
import { ABCDocumentsThunks } from './redux';


const mapStateToProps = ({ abcReducer }) => ({
    abcValue:
        abcReducer.abcValue,
});

const mapDispatchToProps = {
    getABCFunc:
        ABCDocumentsThunks.getABCFunc,
};

export default connect(mapStateToProps, mapDispatchToProps)(ABCDocuments);