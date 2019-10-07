import React, { Component, Fragment } from 'react'
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { getAllBlogs } from '../../actions/blogs';

export class blogs extends Component {

    static propTypes = {
        blogs: PropTypes.array.isRequired,
        getAllBlogs: PropTypes.func.isRequired,
    }

    componentDidMount = () => {
        this.props.getAllBlogs()
    }
    
    render() {
        var { title} = this.props;

        return (
            <Fragment>
                <h1>Blogs</h1>
            </Fragment>
        )
    }
}

const mapStateToProps = state => ({
    blogs: state.blogs.blogs
})

export default connect(mapStateToProps, { getAllBlogs })(blogs);