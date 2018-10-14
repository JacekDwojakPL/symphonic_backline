import React from "react";
import { render } from "react-dom";
import Sections from "./Sections.jsx";
import Landing from "./Landing.jsx";

const App = () => (
  <div className="container">
    <Landing />
    <Sections />
  </div>
);

render(<App />, document.getElementById("app"));
