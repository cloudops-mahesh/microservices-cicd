import { useState, useEffect } from 'react';

export default function UserList({ apiBase }) {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(`${apiBase}/api/users`)
      .then(r => r.json())
      .then(data => { setUsers(data); setLoading(false); })
      .catch(() => setLoading(false));
  }, [apiBase]);

  if (loading) return <p>Loading users...</p>;

  return (
    <section>
      <h2>Users</h2>
      <table border="1">
        <thead><tr><th>ID</th><th>Name</th><th>Email</th></tr></thead>
        <tbody>
          {users.map(u => (
            <tr key={u.id}>
              <td>{u.id}</td>
              <td>{u.name}</td>
              <td>{u.email}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </section>
  );
}