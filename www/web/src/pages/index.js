import React from "react"
import ReactDOM from "react-dom"

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect,
} from "react-router-dom"

import { Transition, animated } from "react-spring/renderprops"

import "../styles/App.scss"

import Home from "./Home"

function App() {
  return (
    <Router>
      <Route
        render={({ location, rest }) => (
          <div>
            <Route exact path="/" render={() => <Redirect to="/home" />} />
            <Transition
              native
              items={location}
              keys={location.pathname}
              from={{ number: 0 }}
              enter={{ number: 300 }}
              leave={{ number: 0 }}
              config={{ duration: 300 }}
            >
              {(loc, state) => style => (
                <Switch location={state === "update" ? location : loc}>
                  <Route
                    path="/home"
                    render={props => (
                      <animated.div style={{ ...style }}>
                        <div>
                          <Home />
                        </div>
                      </animated.div>
                    )}
                  />
                </Switch>
              )}
            </Transition>
          </div>
        )}
      />
    </Router>
  )
}

ReactDOM.render(<App />, document.getElementById("app"))
