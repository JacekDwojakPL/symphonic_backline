import React from "react";

const Section = props => (
  <div className={`row ${props.nazwa}`}>
    <div className="col">
      {" "}
      <h1>{props.nazwa}</h1>
    </div>
    <div className="col">
      {" "}
      <p>{props.opis}</p>
    </div>
  </div>
);

export default Section;
