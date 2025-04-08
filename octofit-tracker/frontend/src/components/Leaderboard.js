import React, { useEffect, useState } from 'react';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);

  useEffect(() => {
    fetch('https://didactic-doodle-xv75pp7vq72p7gp-3000.app.github.dev/api/leaderboard/')
      .then(response => response.json())
      .then(data => {
        console.log('Fetched leaderboard:', data); // Log the response
        setLeaderboard(data);
      })
      .catch(error => console.error('Error fetching leaderboard:', error));
  }, []);

  return (
    <div className="card">
      <div className="card-body">
        <h1 className="card-title">Leaderboard</h1>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>User</th>
              <th>Score</th>
            </tr>
          </thead>
          <tbody>
            {leaderboard.map(entry => (
              <tr key={entry._id}>
                <td>{entry.user.username || entry.user}</td>
                <td>{entry.score}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Leaderboard;
