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
    const Sections = this.state.sections.map(element => {
      if (this.props.currentLang === "Polski") {
        return (
          <Section
            key={element.id}
            name={element.nazwa}
            description={element.opis}
            currentLang={this.props.currentLang}
            sectionId={element.id}
          />
        );
      } else {
        return (
          <Section
            key={element.id}
            name={element.name}
            description={element.description}
            currentLang={this.props.currentLang}
            sectionId={element.id}
          />
        );
      }
    });
    return <div className="sections-div">{Sections}</div>;
  }
}
export default Sections;
