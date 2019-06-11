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
            <div className="row">
                {Array.from(this.props.issues).map(issue => 
                    <Issue title={issue.title} link_img={issue.image} link_pdf={issue.issue} key={issue.id} />
                )}
            </div>
        )
    }
}

const mapStateToProps = state => ({
    issues: state.issues.issues
})

export default connect(mapStateToProps, { getAllIssues })(issues);
