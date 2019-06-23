import axios from 'axios';

import { GET_ALL_ISSUES, GET_ISSUE } from './types';

// GET ALL ISSUES
export const getAllIssues = () => (dispatch) => {
    axios.get("http://127.0.0.1:8000/api/issues")
        .then(res => {
            dispatch({
                type: GET_ALL_ISSUES,
                payload: res.data
            });
        }).catch(
            err => console.log('Error')
        );
};

export const getIssue = (id) => (dispatch) => {
    axios.get(`http://127.0.0.1:8000/api/issues/${id}`)
        .then(res => {
            dispatch({
                type: GET_ISSUE,
                payload: res.data
            });
        }).catch(
            err => console.log('Error')
        )
}