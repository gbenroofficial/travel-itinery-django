import React, { useState } from "react";
// import ReactDOM from 'react-dom';
import CardDeck from "./components/cardDeck";
// import TravInfo from './components/home_components/travelInfo.js'
import Nav from "./components/nav";
import Home from "./components/home";
 
import { MyContext } from "./context/context";

const App = () => {
  const [state, setState] = useState({
    events:[]
  });

  return (
    // <div>hello world</div>
    //
    <div>
    <Nav/>
      <MyContext.Provider value={{ value: [state, setState] }}>
       <Home/>
      </MyContext.Provider>
    </div>
  );
};

export {App, MyContext};
