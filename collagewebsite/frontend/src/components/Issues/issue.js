import React, { Component } from 'react'
import { MDBMask, MDBView, MDBContainer, MDBRow, MDBCol } from "mdbreact";

export class issue extends Component {

    render() {
        var { title, link_img, link_pdf, youtube, soundcloud } = this.props;

        if(link_img === null){
            link_img = "media/issues/no_image.jpg"
        }

        return (
                <div className="card flex-row flex-wrap col-md-4 border-2 my-auto mx-auto d-block">
                    <div className="border-2">
                        <a href={link_pdf}>
                            <img className="img-fluid mx-auto my-auto d-block" src={link_img} alt=""/>
                        </a>
                    </div>
                </div>

        )
    }
}

export default issue
