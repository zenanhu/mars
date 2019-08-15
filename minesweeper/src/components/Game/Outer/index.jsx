import React from 'react';
import Top from './Top/index.jsx';
import Bottom from './Bottom/index.jsx';
import styles from './styles.css';

const Outer = () => (
  <div className={styles.outer}>
    <Top />
    <Bottom />
  </div>
);

export default Outer;
