import React, { Component } from "react";
import axios from "axios";

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
      <div className={`${this.state.results.nazwa} pt-6 pb-6`}>
        <p>
          {this.props.currentLang === "Polski"
            ? `${this.state.results.opis}`
            : `${this.state.results.description}`}
        </p>
      </div>
    );
  }
}

export default Landing;
