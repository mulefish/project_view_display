import { connect } from 'react-redux';
// import { ABCDocumentsThunks, ABC DocumentsActions } from './redux';
import ABCDocuments from './layout';
import { ABCDocumentsThunks } from './redux';


const mapStateToProps = ({ abcDocuments }) => ({
    listOfClassificationsFromTheBackEnd:
        abcDocuments.listOfClassificationsFromTheBackEnd,
});

const mapDispatchToProps = {
    getListOfClassificationsViaRestfulEndpoint:
        ABCDocumentsThunks.getListOfClassificationsViaRestfulEndpoint,
};

export default connect(mapStateToProps, mapDispatchToProps)(ABCDocuments);