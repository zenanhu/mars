import React from "react";
import ReactDOM from "react-dom";
import { render } from "react-dom";
import Game from "../components/Game/index.jsx";
import { create } from "mines";
import { takeTurn } from "mines-robot";
import { each } from "lodash";
import { gameStates } from "mines";

global.minesweeperGames = {};

const renderComponent = element => {
  const preset = element.getAttribute("data-preset");
  // console.log(preset);

  const game = create({ preset: preset });

  game.onGameStateChange(function(state, oldState) {
    console.log("game changed", oldState, state);
    console.log(game.renderAsString());
  });
  game.onCellStateChange(function(cell, state, oldState) {
    console.log("cell", cell, "changed from", oldState, "to", state);
  });

  const name = element.getAttribute("data-name");

  if (name) {
    global.minesweeperGames[name] = game;
  }

  if (element.getAttribute("data-robot")) {
    console.log(">>>> data-robot");
    const ms = parseInt(element.getAttribute("data-robot"));
    const poll = () => {
      if (game.state() === gameStates.WON || game.state() === gameStates.LOST) {
        game.reset();
      }
      takeTurn(game);
      setTimeout(poll, ms);
    };
    poll();
  }

  // render(<Game game={game} />, element);
  console.log("Rendering");
  ReactDOM.render(<Game game={game} />, element);
};

each(document.getElementsByClassName("minesweeper-game"), renderComponent);
