import React, { Component } from 'react'
import { MDBMask, MDBView, MDBContainer, MDBRow, MDBCol } from "mdbreact";

export class issue extends Component {

    render() {
        var { title, link_img, link_pdf, youtube, soundcloud } = this.props;

        if(link_img === null){
            link_img = "media/issues/no_image.jpg"
        }

        return (
                <div className="card flex-row flex-wrap col-md-4 border-0">
                    <div className="border-0">
                        <img className="img-fluid" src={link_img} alt=""/>
                    </div>
                </div>

        )
    }
}

export default issue
