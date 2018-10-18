import React, { Component } from "react";
import axios from "axios";

class Links extends Component {
  state = {
    content: []
  };
  componentDidMount() {
    axios.get("/api/get_links").then(response => {
      this.setState({ content: response.data });
    });
  }

  scroll_to_section(id) {
    const target_element = document.getElementById(`section${id}`);
    target_element.scrollIntoView({ behavior: "smooth" });
  }

  render() {
    const list = this.state.content
      .filter(element => {
        return element.instrumentSection === false;
      })
      .map(element => {
        return (
          <li className="nav-item">
            <span
              className="nav-link active"
              onClick={() => {
                this.scroll_to_section(element.id);
              }}
            >
              {this.props.currentLang === "Polski"
                ? `${element.nazwa}`
                : `${element.name}`}
            </span>
          </li>
        );
      });

    const dropdown = this.state.content
      .filter(element => {
        return element.instrumentSection === true;
      })
      .map(element => {
        return (
          <span
            className="dropdown-item"
            onClick={event => {
              this.scroll_to_section(element.id);
            }}
          >
            {this.props.currentLang === "Polski"
              ? `${element.nazwa}`
              : `${element.name}`}
          </span>
        );
      });

    return (
      <nav className="navbar navbar-expand-lg navbar-dark">
        <a className="navbar-brand" href="/">
          Symphonic Backline
        </a>
        <button
          className="navbar-toggler"
          type="button"
          data-toggle="collapse"
          data-target="#symphonic_backline_navbar"
        >
          <span className="navbar-toggler-icon" />
        </button>
        <div
          className="collapse navbar-collapse"
          id="symphonic_backline_navbar"
        >
          <ul className="navbar-nav ml-auto">
            <li className="nav-item dropdown">
              <a
                className="nav-link active dropdown-toggle"
                href="#"
                id="symphonic_backline_navbar_dropdown"
                role="button"
                data-toggle="dropdown"
              >
                {this.props.currentLang === "Polski"
                  ? "Instrumenty"
                  : "Instruments"}
              </a>
              <div className="dropdown-menu">{dropdown}</div>
            </li>
            {list}
            <li className="nav-item">
              <a
                className="nav-link active"
                href="#"
                onClick={this.props.changeLanguage}
              >
                {this.props.nextLang}
              </a>
            </li>
          </ul>
        </div>
      </nav>
    );
  }
}

export default Links;
