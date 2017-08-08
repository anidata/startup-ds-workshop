import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import Printer from './App';
import registerServiceWorker from './registerServiceWorker';

ReactDOM.render(<Printer subreddit='reactjs'/>, document.getElementById('root'));
registerServiceWorker();
