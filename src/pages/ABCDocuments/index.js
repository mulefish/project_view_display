import { connect } from 'react-redux';
// import { ABCDocumentsThunks, ABC DocumentsActions } from './redux';
import ABCDocuments from './layout';
import { ABCDocumentsThunks } from './redux';


const mapStateToProps = ({ abcDocuments }) => ({
    abcValue:
        abcDocuments.abcValue,
});

const mapDispatchToProps = {
    getABCFunc:
        ABCDocumentsThunks.getABCFunc,
};

export default connect(mapStateToProps, mapDispatchToProps)(ABCDocuments);