import { useState, useEffect } from 'react';

export default function OrderList({ apiBase }) {
  const [orders, setOrders] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(`${apiBase}/api/orders`)
      .then(r => r.json())
      .then(data => { setOrders(data); setLoading(false); })
      .catch(() => setLoading(false));
  }, [apiBase]);

  if (loading) return <p>Loading orders...</p>;

  return (
    <section>
      <h2>Orders</h2>
      <table border="1">
        <thead><tr><th>ID</th><th>User</th><th>Item</th><th>Amount</th><th>Status</th></tr></thead>
        <tbody>
          {orders.map(o => (
            <tr key={o.id}>
              <td>{o.id}</td>
              <td>{o.user_id}</td>
              <td>{o.item}</td>
              <td>₹{o.amount}</td>
              <td>{o.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </section>
  );
}