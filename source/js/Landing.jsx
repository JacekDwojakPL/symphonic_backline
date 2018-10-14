import React, { Component } from "react";
import axios from "axios";

class Landing extends Component {
  state = {
    nazwa: "",
    opis: ""
  };

  componentDidMount() {
    axios.get("/api/get_landing").then(response => {
      const return_data = response.data;
      this.setState({
        opis: return_data[0].content,
        nazwa: return_data[0].nazwa
      });
    });
  }

  render() {
    return (
      <div className={`pt-6 pb-6 ${this.state.nazwa}`}>
        <p>{this.state.opis}</p>
      </div>
    );
  }
}

export default Landing;
