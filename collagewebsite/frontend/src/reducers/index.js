import { combineReducers } from 'redux';
import issues from './issues';
import blogs from './blogs';

export default combineReducers({
    issues,
    blogs
});