import axios from 'axios';

import { GET_ALL_ISSUES } from './types';

// GET ALL ISSUES
export const getAllIssues = () => (dispatch, getState) => {
    axios.get("http://127.0.0.1:8000/api/issues")
        .then(res => {
            dispatch({
                type: GET_ALL_ISSUES,
                payload: res.data
            });
        }).catch(
            console.log("Error")
        );
};