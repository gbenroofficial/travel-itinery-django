import React from "react";

class TravInfo extends React.Component{
    render(){

        return(
            <div id="travel">
                <form id="travelForm" className="form-inline mx-sm-2 mt-2">
                    <div id="location" className="form-group">
                        <div className="form-group mx-sm-2 mb-2">
                            <label></label>
                            <input id="from" className="form-control" placeholder="From"></input>
                        </div>
                        <div className="form-group mx-sm-3 mb-2">
                            <label></label>
                            <input id="to" className="form-control" placeholder="To"></input>
                        </div>
                    </div>
                    <div id="duration" className="form-group mx-sm-5">
                        <div className="form-group mx-sm-3 mb-2">
                            <label></label>
                            <input id="startDate" className="form-control" placeholder="Start date"></input>
                        </div>
                        <div className="form-group mx-sm-3 mb-2">
                            <label></label>
                            <input id="endDate" className="form-control" placeholder="End date"></input>
                        </div>
                    </div>
                    
                    
                        <button type="submit" className="btn btn-primary mb-2">Submit</button>
                    
                </form>

            </div>
        )
    }
}

export default TravInfo