import React, { Component } from "react";
import axios from "axios";
import Separator from "./Separator.jsx";

class Landing extends Component {
  state = {
    results: []
  };

  componentDidMount() {
    axios.get("/api/get_landing").then(response => {
      const return_data = response.data;
      this.setState({
        results: response.data[0]
      });
    });
  }

  render() {
    return (
      <div id="landing">
        <div className={`container pt-6 pb-6`}>
          <div className="row">
            <div className="col-md-6 col-sm-12">
              <h4 className="text-uppercase text-center text-md-left main_header">
                {this.props.currentLang === "Polski"
                  ? `${this.state.results.nazwa}`
                  : `${this.state.results.name}`}
              </h4>
            </div>
          </div>
          <p className="text-center text-md-left pt-5 pb-5">
            {this.props.currentLang === "Polski"
              ? `${this.state.results.opis}`
              : `${this.state.results.description}`}
          </p>
        </div>
      </div>
    );
  }
}

export default Landing;
