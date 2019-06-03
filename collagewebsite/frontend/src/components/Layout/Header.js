import React, { Component } from 'react';

import { Link } from 'react-router-dom';

export class Header extends Component {
    render() {
        return (
            <nav className="navbar navbar-expand-sm navbar-dark bg-dark">
                <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarTogglerDemo01">
                    <Link to="/" className="navbar-brand">Collage</Link>
                    <ul className="navbar-nav navbar-right ml-auto mt-2 mt-lg-0">
                        <li className="nav-item">
                            <Link to="/issues" className="nav-link">Issues </Link>
                        </li>
                        <li className="nav-item">
                            <Link to="/blogs" className="nav-link" >Blogs </Link>
                        </li>
                        <li className="nav-item">
                            <Link to="/contact" className="nav-link">Contact </Link>
                        </li>
                        <li className="nav-item">
                            <Link to="/submit" className="nav-link">Submit </Link>
                        </li>
                        <li className="nav-item">
                            <Link to="/register" className="nav-link" href="#">Register </Link>
                        </li>
                        <li className="nav-item">
                            <Link to="/login" className="nav-link">Login</Link>
                        </li>
                    </ul>
                </div>
            </nav>
        )
    }
}

export default Header
