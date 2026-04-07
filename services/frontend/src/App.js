import { useState, useEffect } from 'react';

const API_BASE = process.env.REACT_APP_API_URL || '';

function App() {
  const [activeTab, setActiveTab] = useState('users');
  const [health, setHealth] = useState(null);

  useEffect(() => {
    fetch(`${API_BASE}/health`)
      .then(r => r.json())
      .then(setHealth)
      .catch(() => setHealth({ status: 'unreachable' }));
  }, []);

  return (
    <div>
      <h1>Microservices Demo</h1>
      {health && <p>Gateway: {health.status}</p>}
      <button onClick={() => setActiveTab('users')}>Users</button>
      <button onClick={() => setActiveTab('orders')}>Orders</button>
      <p>Active tab: {activeTab}</p>
    </div>
  );
}

export default App;