import React, { Component } from "react";
import axios from "axios";
import Section from "./Section.jsx";

class Sections extends Component {
  state = {
    sections: []
  };
  componentDidMount() {
    axios.get("/api/get_sections").then(response => {
      const sections = response.data;
      this.setState({ sections: sections });
    });
  }
  render() {
    return (
      <div className="sections-div">
        {this.state.sections.map(element => (
          <Section key={element.id} nazwa={element.nazwa} opis={element.opis} />
        ))}
      </div>
    );
  }
}
export default Sections;
