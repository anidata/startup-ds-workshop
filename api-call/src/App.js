import React from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios'; ///import axios library

///subclasses React.Component to create printer class
class Printer extends React.Component {
    constructor(props) {
      super(props); ///initialize state to have an empty array of posts


      this.state = {
        posts: []
      };
    }
    ///where the magic happens. method will be executed when the comoponent 'mounts'
    ///or 'is added to DOM' for first time
    componentDidMount() {
        ///fetch server data
        axios.get('http:/www.reddit.com/r/${this.props.subreddit}.json')
          .then(result=> {
            const posts = result.data.data.children.map(obj => obj.data);
            ///the component's state is updated by calling thsi.setState with
            ///the new array of posts. This triggers a re-render, and then the
            ///posts are visible
            this.setState({ posts })
          });
    }

    render() {
      return (
        <div>
          <h1>{'/r/${this.props.subreddit}'}</h1>
          <ul>
            {this.state.posts.map(post =>
              <li key={post.id}>{post.title}</li>
            )}
          </ul>
        </div>
      );
    }
}

ReactDOM.render(
  <Printer subreddit="reactjs"/>,
  document.getElementById('root')
);
