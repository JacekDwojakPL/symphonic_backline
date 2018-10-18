import React, { Component } from "react";
import Instruments from "./Instruments.jsx";
import Separator from "./Separator.jsx";

class Section extends Component {
  state = {
    name: this.props.name,
    description: "",
    instrument_name: "",
    showInstrument: false
  };

  handleChangeDescription = instrument => {
    const result = () => {
      if (this.props.currentLang === "Polski")
        return {
          name: this.props.name,
          description: instrument[0].opis,
          instrument_name: instrument[0].nazwa,
          showInstrument: true
        };
      else {
        return {
          name: this.props.name,
          description: instrument[0].description,
          instrument_name: instrument[0].name,
          showInstrument: true
        };
      }
    };
    this.setState(result);
  };

  render() {
    return (
      <div id={`${this.props.sectionId}`}>
        <Separator />
        <div
          className="pt-5 pb-5 pt-md-6 pb-md-6"
          id={`section${this.props.sectionId}`}
        >
          <div className="container text-sm-center">
            <div className="row pt-0 pb-0 pb-md-5 justify-content-center">
              <h2 className="text-uppercase mb-4 mb-sm-1 text-center">
                {this.props.name}
              </h2>
            </div>
            <div className="row mt-sm-4 mt-md-0">
              <div className="col-sm-12 col-md-6 order-1 text-center text-md-left pt-5 pb-5 pb-md-0 pt-md-0">
                <h4 className="text-uppercase text-center text-md-left mb-4 mb-sm-1">
                  {this.state.instrument_name}
                </h4>
                <p className="text-center text-md-left pt-4 pb-4">
                  {this.state.showInstrument === true
                    ? `${this.state.description}`
                    : `${this.props.description}`}
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
      </div>
    );
  }
}

export default Section;
