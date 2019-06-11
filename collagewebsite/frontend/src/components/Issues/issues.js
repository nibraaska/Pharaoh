import React, { Component } from 'react';
import { issue as Issue} from './issue';

import { connect } from 'react-redux';
import PropTypes from 'prop-types';

import { getAllIssues } from '../../actions/issues';


export class issues extends Component {
    static propTypes = {
        issues: PropTypes.array.isRequired,
        getAllIssues: PropTypes.func.isRequired
    }

    componentDidMount(){
        this.props.getAllIssues()
    }

    render() {
        return (
            <div>
                <Issue title={"1969"} link_img={"media/issues/1969/1969.jpg"} link_pdf="media/issues/1969/1969.pdf"/>
            </div>
        )
    }
}

const mapStateToProps = state => ({
    issues: state.issues.issues
})

export default connect(mapStateToProps, { getAllIssues })(issues);
