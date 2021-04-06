import { connect } from 'react-redux'
import SecondPass from './layout'
import { ABCDocumentsThunks } from '../ABCDocuments/redux';

const mapStateToProps = ({ abcReducer }) => ({
    abcValue:
        abcReducer.abcValue,
});

const mapDispatchToProps = {
    getABCFunc:
        ABCDocumentsThunks.getABCFunc,
};

export default connect(mapStateToProps, mapDispatchToProps)(SecondPass)

