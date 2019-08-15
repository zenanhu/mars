import React from "react";
import Title from "./Title/index.jsx";
import Outer from "./Outer/index.jsx";
import styles from "./styles.css";

// console.log(styles);

class Game extends React.Component {
  getChildContext() {
    return { game: this.props.game };
  }

  render() {
    const cols = this.props.game.dimensions[1];
    const width = cols * 16 + 20;

    return (
      <div className={styles.minesweeper} style={{ width: width }}>
        <Title />
        <Outer />
      </div>
    );
  }
}

Game.childContextTypes = {
  game: React.PropTypes.object
};

export default Game;
