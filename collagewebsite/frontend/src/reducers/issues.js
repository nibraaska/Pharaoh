import { GET_ALL_ISSUES, GET_ISSUE } from '../actions/types';

const initialState = {
    issues: []
}

export default function(state = initialState, action){
    switch(action.type){
        case GET_ALL_ISSUES:
            return {
                ...state,
                issues: action.payload
            };
        case GET_ISSUE:
            return {
                ...state,
                issues: action.payload
            };
        default:
            return state;
    }
}