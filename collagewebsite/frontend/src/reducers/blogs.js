import { GET_ALL_BLOGS, GET_BLOG } from '../actions/types';

const initialState = {
    blogs: []
}

export default function(state = initialState, action){
    switch(action.type){
        case GET_ALL_BLOGS:
            return {
                ...state,
                blogs: action.payload
            };
        case GET_BLOG:
            return {
                ...state,
                blogs: action.payload
            };
        default:
            return state;
    }
}