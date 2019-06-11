import { GET_ALL_ISSUES } from '../actions/types';

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
        default:
            return state;
    }
}