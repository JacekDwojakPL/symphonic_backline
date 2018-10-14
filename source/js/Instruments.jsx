import React, { Component } from "react";
import axios from "axios";

class Instruments extends Component {
  state = {
    instruments: []
  };
  componentDidMount() {
    axios.get("/api/get_instruments").then(response => {
      this.setState({ instruments: response.data });
    });
  }

  handleChangeDescription(id) {
    const single_instrument = this.state.instruments.filter(element => {
      return element.id === parseInt(id);
    });
    this.props.handleChangeDescription(single_instrument);
  }

  render() {
    const List = this.state.instruments
      .filter(element => {
        return element.section_id === this.props.sectionId;
      })
      .map(element => {
        return (
          <li className="nav-item">
            <a
              className="nav-link"
              onClick={() => {
                this.handleChangeDescription(`${element.id}`);
              }}
            >
              {this.props.currentLang === "Polski"
                ? `${element.nazwa}`
                : `${element.name}`}
            </a>
          </li>
        );
      });

    return <ul className="nav flex-column nav-pills pb-4 pb-md-0">{List}</ul>;
  }
}

export default Instruments;
