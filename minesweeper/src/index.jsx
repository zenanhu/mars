import "./widgets/games.jsx";
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

const firebase = require("firebase");
// Required for side-effects
require("firebase/firestore");

const FIREBASE_API_KEY = "AIzaSyBI-ysMyRU43abjoZNVb_tjmdqJ5wL7Pdk";
const FIREBASE_AUTH_DOMAIN = "www.zenan.xyz";
const FIRESTORE_PROJECT_ID = "minesweeper-7815e";

firebase.initializeApp({
  apiKey: FIREBASE_API_KEY,
  authDomain: FIREBASE_AUTH_DOMAIN,
  projectId: FIRESTORE_PROJECT_ID
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

db.collection("users")
  .get()
  .then(querySnapshot => {
    querySnapshot.forEach(doc => {
      console.log(`${doc.id} => ${doc.data()}`);
    });
  });
