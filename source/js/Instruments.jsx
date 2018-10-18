import React, { Component } from "react";
import axios from "axios";

class Instruments extends Component {
  state = {
    instruments: [],
    instrumentId: null
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

    this.setState({ instrumentId: single_instrument[0].id });
    this.props.handleChangeDescription(single_instrument);
  }
  componentDidUpdate(prevProps) {
    if (
      this.props.currentLang !== prevProps.currentLang &&
      this.state.instrumentId != null
    ) {
      this.handleChangeDescription(this.state.instrumentId);
    }
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
              href="#"
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
