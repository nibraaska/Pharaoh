import React, { Component } from 'react'
import { MDBMask, MDBView, MDBContainer, MDBRow, MDBCol } from "mdbreact";

export class issue extends Component {

    render() {
        const { title, link_img, link_pdf, youtube, soundcloud } = this.props;

        return (
            <div className="container">
                <div className="card flex-row flex-wrap col-sm-4">
                    <div className="card-header border-0">
                        <img className="img-fluid" src={link_img} alt=""/>
                    </div>
                    <div className="card-block px-2">
                        <h4 className="card-title">{title}</h4>
                        <h4>{link_pdf}</h4>
                        <h4>{youtube}</h4>
                        <h4>{soundcloud}</h4>
                        <a href={link_pdf} className="btn btn-primary">BUTTON</a>
                    </div>
                    <div className="w-100"></div>
                </div>
            </div>
        )
    }
}

export default issue
