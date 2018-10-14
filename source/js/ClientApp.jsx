import React, { Component } from "react";
import { render } from "react-dom";
import Sections from "./Sections.jsx";
import Landing from "./Landing.jsx";
import Links from "./Links.jsx";

class App extends Component {
  constructor() {
    super();
    this.state = {
      currentLang: "Polski",
      nextLang: "English"
    };

    this.changeLanguage = this.changeLanguage.bind(this);
  }

  changeLanguage() {
    if (this.state.currentLang === "Polski") {
      this.setState({ currentLang: "English", nextLang: "Polski" });
    } else if (this.state.currentLang === "English") {
      this.setState({ currentLang: "Polski", nextLang: "English" });
    }
  }
  render() {
    return (
      <div className="main">
        <Links
          currentLang={this.state.currentLang}
          nextLang={this.state.nextLang}
          changeLanguage={this.changeLanguage}
        />
        <Landing currentLang={this.state.currentLang} />
        <Sections currentLang={this.state.currentLang} />
      </div>
    );
  }
}
render(<App />, document.getElementById("app"));
