import React, { Component } from 'react';

export class carousel extends Component {
    render() {
        var { three } = this.props;

        var link_img_1 = "media/issues/no_image.jpg"
        var link_img_2 = "media/issues/no_image.jpg"
        var link_img_3 = "media/issues/no_image.jpg"

        if(three.length === 3){
            link_img_1 = three[0].image
            link_img_2 = three[1].image
            link_img_3 = three[2].image
        }

        return (
            <div className="container">
                <div id="carouselExampleIndicators" className="carousel slide" data-ride="carousel">
                    <ol className="carousel-indicators">
                        <li data-target="#carouselExampleIndicators" data-slide-to="0" className="active"></li>
                        <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
                        <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
                    </ol>
                    <div className="carousel-inner">
                        <div className="carousel-item active">
                            <img className="d-block w-100" src={link_img_1} alt="First slide"/>
                        </div>
                        <div className="carousel-item">
                            <img className="d-block w-100" src={link_img_2} alt="Second slide"/>
                        </div>
                        <div className="carousel-item">
                            <img className="d-block w-100" src={link_img_3} alt="Third slide"/>
                        </div>
                    </div>
                    <a className="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
                        <span className="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span className="sr-only">Previous</span>
                    </a>
                    <a className="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
                        <span className="carousel-control-next-icon" aria-hidden="true"></span>
                        <span className="sr-only">Next</span>
                    </a>
                </div>
            </div>
        )
    }
}

export default (carousel)
