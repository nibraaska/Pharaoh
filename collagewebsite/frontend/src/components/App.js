import React, { Component, Fragment } from 'react';
import ReactDOM from 'react-dom';

import register from './Accounts/register';
import login from './Accounts/login';
import submit from './Submit/submit';
import contact from './Contact/contact';
import blogs from './Blogs/blogs';
import issues from './Issues/issues';
import Header from './Layout/Header';
import home from './Home/home';

import { Provider } from 'react-redux';
import store from '../store';

import { HashRouter as Router, Route, Switch } from 'react-router-dom';

export class App extends Component {
    render() {
        return (
            <div style={{backgroundColor: "#F8F8FF"}}>
                <Provider store={store}>
                    <Router>
                        <Fragment>
                            <Header />
                                <Switch>
                                    <Route exact path='/' component={home} />
                                    <Route path='/issues' component={issues} />
                                    <Route path='/blogs' component={blogs} />
                                    <Route path='/contact' component={contact} />
                                    <Route path='/submit' component={submit} />
                                    <Route path='/login' component={login} />
                                    <Route path='/register' component={register} />
                                </Switch>
                        </Fragment>
                    </Router>
                </Provider>
            </div>
        )
    }
}

ReactDOM.render(<App />, document.getElementById('app'))