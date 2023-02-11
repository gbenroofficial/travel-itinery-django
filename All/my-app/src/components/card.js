import React from "react";
import ReactDOM from 'react-dom'

const Card = ({props}) =>{

        return(
            <div>

                <div className="card">
                    <img className="card-img-top" src="..." alt="Card pic"/>
                    <div className="card-body">
                        <h5 className="card-title">{props.name}</h5>
                        <p className="card-text">{props.description}</p>
                        <p className="card-text">
                        <small className="text-muted">Last updated 3 mins ago</small></p>
                    </div>
                </div>
                <br/>
            </div>

        )

}

// const Card = () => {
//   return (
//     <div>
//       <div className="card">
//         <img className="card-img-top" src="..." alt="Card pic" />
//         <div className="card-body">
//           <h5 className="card-title">yyy</h5>
//           <p className="card-text"></p>
//           <p className="card-text">
//             <small className="text-muted">Last updated 3 mins ago</small>
//           </p>
//         </div>
//       </div>
//       <br />
//     </div>
//   );
// };
export default Card;
