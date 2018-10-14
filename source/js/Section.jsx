import React, { Component } from "react";
import Instruments from "./Instruments.jsx";

class Section extends Component {
  state = {
    name: this.props.name,
    description: this.props.description,
    instrument_name: ""
  };

  handleChangeDescription = instrument => {
    const result =
      this.props.currentLang === "Polski"
        ? instrument[0].nazwa
        : instrument[0].name;
    this.setState({
      instrument_name: result
    });
  };

  render() {
    return (
      <div className="pt-5 pb-5 pt-md-6 pb-md-6">
        <div className="container text-sm-center">
          <div className="row pt-0 pb-0 pb-md-5 justify-content-center">
            <h2 className="text-uppercase mb-4 mb-sm-1 text-center">
              {this.state.name}
            </h2>
          </div>
          <div className="row mt-sm-4 mt-md-0">
            <div className="col-sm-12 col-md-6 order-1 text-center text-md-left pt-5 pb-5 pb-md-0 pt-md-0">
              <h4 className="text-uppercase text-center text-md-left mb-4 mb-sm-1">
                {this.state.instrument_name}
              </h4>
              <p className="text-center text-md-left pt-4 pb-4">
                {this.state.description}
              </p>
            </div>
            <div className="col-sm-12 col-md-6 order-2 text-center text-md-right">
              <h3 className="mb-3 mb-md-4">
                {this.props.currentLang === "Polski" ? "Oferta" : "Our offer"}
              </h3>
              <ul className="nav flex-column nav-pills pb-4 pb-md-0">
                <Instruments
                  currentLang={this.props.currentLang}
                  sectionId={this.props.sectionId}
                  handleChangeDescription={this.handleChangeDescription}
                />
              </ul>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Section;
