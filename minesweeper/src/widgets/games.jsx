import React from "react";
import ReactDOM from "react-dom";
import { render } from "react-dom";
import Game from "../components/Game/index.jsx";
import { create } from "mines";
import { takeTurn } from "mines-robot";
import { each } from "lodash";
import { gameStates } from "mines";
import * as constants from "../constants.js";

global.minesweeperGames = {};

const firebase = require("firebase");
// Required for side-effects
require("firebase/firestore");

firebase.initializeApp({
  apiKey: constants.FIREBASE_API_KEY,
  authDomain: constants.FIREBASE_AUTH_DOMAIN,
  projectId: constants.FIRESTORE_PROJECT_ID
});

var db = firebase.firestore();

db.collection("users")
  .add({
    first: "Ada",
    last: "Lovelace",
    born: 1815
  })
  .then(function(docRef) {
    console.log("Document written with ID: ", docRef.id);
  })
  .catch(function(error) {
    console.error("Error adding document: ", error);
  });

// db.collection("users")
//   .get()
//   .then(querySnapshot => {
//     querySnapshot.forEach(doc => {
//       console.log(`${doc.id} => ${doc.data()}`);
//     });
//   });


class Minesweeper extends React.Component {
  render() {
    // const renderComponent = element => {
    // const preset = element.getAttribute("data-preset");
    const preset = this.props.preset;
    // console.log(preset);

    const game = create({ preset: preset });

    game.onGameStateChange(function(state, oldState) {
      console.log("game changed", oldState, state);
      console.log(game.renderAsString());
    });
    game.onCellStateChange(function(cell, state, oldState) {
      console.log("cell", cell, "changed from", oldState, "to", state);
    });

    // const name = element.getAttribute("data-name");
    const name = this.props.name;

    if (name) {
      global.minesweeperGames[name] = game;
    }

    // const robot = element.getAttribute("data-robot");
    const robot = this.props.robot || "";
    if (robot) {
      console.log(">>>> data-robot");
      const ms = parseInt(robot);
      const poll = () => {
        if (
          game.state() === gameStates.WON ||
          game.state() === gameStates.LOST
        ) {
          game.reset();
        }
        takeTurn(game);
        setTimeout(poll, ms);
      };
      poll();
    }

    // render(<Game game={game} />, element);
    console.log("Rendering");
    return <Game game={game} />;
  }
}
// };
// each(document.getElementsByClassName("minesweeper-game"), renderComponent);

export default Minesweeper;
