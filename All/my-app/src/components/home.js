import React from 'react';
import ReactDOM from 'react-dom';
import TravInfo from './home_components/travelInfo.js'
import CardDeck from './cardDeck';

const Home = () => {
    return (
        <div>
            <div className='container-fluid'>
                <TravInfo/> 
                <br></br>
                <div className="btn-group">
                    <button className="btn btn-link btn-lg" href=''> Hotels in area </button>                
                    <button className="btn btn-link btn-lg" href=''> Transport prices </button>
                </div>  
                <br></br>                     
                <CardDeck/>

            </div>     
        </div>
    )
}

export default Home