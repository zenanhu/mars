import Minesweeper from "./widgets/games.jsx";
import "./widgets/controllers.jsx";

// import React from "react";
// import ReactDOM from "react-dom";
// import styles from "./index.css";
// console.log("loading styles...");
// console.log(styles);
// const Index = () => {
//   return <div className={styles.helloworld}>Hello World!</div>;
// };
// ReactDOM.render(<Index />, document.getElementById("index"));

import React from "react";
import ReactDOM from "react-dom";

const App = () => {
  return (
    <div>
      <Minesweeper preset="expert" name="expert" />
    </div>
  );
};
ReactDOM.render(<App />, document.getElementById("app"));
