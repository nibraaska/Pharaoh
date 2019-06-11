import React, { Component } from 'react'
import { MDBMask, MDBView, MDBContainer, MDBRow, MDBCol } from "mdbreact";

export class issue extends Component {

    render() {
        const { title, link_img, link_pdf, youtube, soundcloud } = this.props;

        return (
            <div className="card flex-row flex-wrap col-md-4">
                <div className="card-header border-0">
                    <img className="img-fluid" src={link_img} alt=""/>
                </div>
                <div className="card-block px-2">
                    <h4 className="card-title">{title}</h4>
                    <a href={link_pdf} className="btn btn-primary">BUTTON</a>
                </div>
                <div className="w-100"></div>
            </div>
        )
    }
}

export default issue
