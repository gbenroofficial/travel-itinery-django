import React, { useEffect, useContext } from "react";
import axios from "axios";
import Card from "./card";
import { MyContext } from "../context/context";

const CardDeck = () => {
  let arr = null;
  let context = useContext(MyContext);

  useEffect(() => {
    getEvents();
  }, []);

  function getEvents() {
    // console.log("yyy");
    axios({
      method: "GET",
      url: "showIndex/",
    })
      .then((response) => {
        const data = response.data;
        arr = data.data;
        context.value[0].events = arr;
        console.log(context);

        // console.log(arr);
      })
      .catch((error) => {
        if (error.response) {
          console.log(error.response);
          console.log(error.response.status);
          console.log(error.response.headers);
        }
      });
  }

  return (
    // <Card/>
    <div className="container">
      <div className="row">
        <div className="col-lg-start">
          <br />

          {context.value[0].events.map((item) => (
            <div id={item.id}>
              <Card props={item} />
            </div>
          ))}
        </div>

        <div className="col col-lg-2">2 of 2</div>
      </div>
    </div>
  );
};

export default CardDeck;
