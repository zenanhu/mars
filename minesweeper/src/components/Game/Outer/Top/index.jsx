import React from 'react';
import Lcd from '../../../Lcd/index.jsx';
import Status from './Status/index.jsx';
import styles from './styles.css';

class Top extends React.Component {
  constructor(props, context) {
    super(props, context);
    const game = context.game;
    context.game.onRemainingMineCountChange(
      (count) => { this.setState({mineCount: count}); }
    );
    context.game.onTimerChange(
      (ms) => { this.setState({seconds: Math.floor(ms / 1000)}); }
    );

    this.state = {
      mineCount: game.remainingMineCount(),
      seconds: 0
    };
  }

  render() {
    const state = this.state;

    return (
      <div className={styles.top}>
        <Lcd number={state.mineCount} className={styles.minesRemaining} />
        <Status game={this.context.game} />
        <Lcd number={state.seconds} className={styles.timer} />
      </div>
    );
  }
}

Top.contextTypes = {
  game: React.PropTypes.object
};

export default Top;
