import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [code, setCode] = useState('');
  const [feedback, setFeedback] = useState([]);

  const handleSubmit = async () => {
    const res = await axios.post('http://localhost:5000/review', { code });
    setFeedback(res.data.feedback);
  };

  return (
    <div>
      <textarea onChange={(e) => setCode(e.target.value)} />
      <button onClick={handleSubmit}>Analyze</button>
      <ul>
        {feedback.map((f, i) => <li key={i}>{f}</li>)}
      </ul>
    </div>
  );
}

export default App;
