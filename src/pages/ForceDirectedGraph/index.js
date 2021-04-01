import { connect } from 'react-redux'
import ForceDirectedGraph from './layout'
import { ABCDocumentsThunks } from './../ABCDocuments/redux/';

const mapStateToProps = ({ abcDocuments }) => ({
    abcValue:
        abcDocuments.abcValue,
});

const mapDispatchToProps = {
    getABCFunc:
        ABCDocumentsThunks.getABCFunc,
};

// const mapStateToProps = ({ }) => ({
// })
// const mapDispatchToProps = {}
export default connect(mapStateToProps, mapDispatchToProps)(ForceDirectedGraph)


/*
import { connect } from 'react-redux';

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
*/