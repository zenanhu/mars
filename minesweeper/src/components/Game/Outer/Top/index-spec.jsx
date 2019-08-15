import React from 'react';
import Top from './index.jsx';
import Lcd from '../../../Lcd/index.jsx';
import Status from './Status/index.jsx';
import styles from './styles.css';

describe('Top', () => {
  it('should render', () => {
    const game = {
      onRemainingMineCountChange: () => { },
      onTimerChange: () => { },
      remainingMineCount: () => 99
    };
    styles.top = 'top';
    styles.minesRemaining = 'minesRemaining';
    styles.timer = 'timer';

    const tree = sd.shallowRender(<Top />, { game: game });
    expect(tree.getRenderOutput()).toEqualJSX(
      <div className='top'>
        <Lcd number={99} className='minesRemaining' />
        <Status game={game} />
        <Lcd number={0} className='timer' />
      </div>
    );
  });
});
