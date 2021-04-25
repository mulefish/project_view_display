import { connect } from 'react-redux'
import { ABCDocumentsThunks } from '../ABCDocuments/redux';
import FauxForce from './layout'
import './index.css';

const mapStateToProps = ({ abcReducer }) => ({
    abcValue:
        abcReducer.abcValue,
});

const mapDispatchToProps = {
    getABCFunc:
        ABCDocumentsThunks.getABCFunc,
};

export default connect(mapStateToProps, mapDispatchToProps)(FauxForce)

