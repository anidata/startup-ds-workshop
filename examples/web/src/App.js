import './App.css';
import 'c3/c3.css';
import C3Chart from 'react-c3js';
import React, { Component } from 'react';
import axios from 'axios'; ///import axios library
import logo from './logo.svg';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: {
        columns: []
      }
    };
  }

  componentDidMount() {
    ///fetch server data
    axios.get('http://localhost:8000/titanic/aggregates')
      .then(result => {
        // The response data is not in ideal format for the visualization
        // library, so we have to some manipulation. This is not uncommon to
        // some slightly transformation.
        var transformed_data = result.data.data.map(obj =>
          [obj.pclass, obj.count]
        );
        const data = {
          columns: transformed_data,
          type: "bar"
        };
        this.setState({ data })
      });
  }

  render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Welcome to React</h2>
        </div>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
        <C3Chart data={this.state.data} />
      </div>
    );
  }
}

export default App;
