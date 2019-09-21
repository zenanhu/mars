import React, { Component } from "react"
import window from "global"
import posed from "react-pose"
import _ from "lodash"

import Grid from "@material-ui/core/Grid"

import "../styles/Home.scss"

function Home(props) {
  return (
    <Grid container justify="center" alignItems="center" className="home">
      <span>Hello, I'm Zenan</span>
    </Grid>
  )
}

export default Home
