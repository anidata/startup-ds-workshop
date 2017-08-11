import React, { Component } from 'react';
import C3Chart from 'react-c3js';
import logo from './logo.svg';
import './App.css';
import 'c3/c3.css';

class App extends Component {
  constructor(props) {
    super(props);
    this.data = {
      columns: [
        ["First Class", 15],
        ["Second Class", 35],
        ["Third Class", 25]
      ],
      type: 'bar'
    };
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
        <C3Chart data={this.data} />
      </div>
    );
  }
}

export default App;
