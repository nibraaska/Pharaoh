import axios from 'axios';

import { GET_ALL_BLOGS, GET_BLOG } from './types';

// GET ALL BLOGS
export const getAllBlogs = () => (dispatch) => {
    axios.get('http://127.0.0.1:8000/api/blog')
        .then(res => {
            dispatch({
                type: GET_ALL_BLOGS,
                payload: res.data
            });
        }).catch(
            err => console.log('Error')
        );
};

// GET ONE BLOG
export const getBlog = (id) => (dispatch) => {
    axios.get(`http://127.0.0.1:8000/api/blog/${id}`)
        .then(res => {
            dispatch({
                type: GET_BLOG,
                payload: res.data
            });
        }).catch(
            err => console.log('Error')
        );
};