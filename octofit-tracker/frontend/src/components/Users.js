import React, { useEffect, useState } from 'react';

export default function Users() {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selected, setSelected] = useState(null);
  const [showModal, setShowModal] = useState(false);
  const resource = 'users';
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  const endpoint = `https://super-space-journey-wr4qx9j7xqxgc9j5x-8000.app.github.dev/api/${resource}/`;

  const fetchData = () => {
    setLoading(true);
    fetch(endpoint)
      .then((res) => res.json())
      .then((json) => {
        const data = Array.isArray(json) ? json : (json.results ?? json);
        setItems(data || []);
      })
      .catch((err) => {
        console.error('[Users] Fetch error:', err);
        setItems([]);
      })
      .finally(() => setLoading(false));
  };

  useEffect(() => {
    fetchData();
  }, [endpoint]);

  const columns = items.length > 0
    ? (() => { const ks = Object.keys(items[0]); return ks.includes('id') ? ['id', ...ks.filter(k => k !== 'id')] : ks; })()
    : [];

  const renderCell = (item, key) => {
    const v = item[key];
    if (v === null || v === undefined) return '';
    if (typeof v === 'object') return JSON.stringify(v);
    return String(v);
  };

  return (
    <div className="card mb-4">
      <div className="card-header d-flex justify-content-between align-items-center">
        <h2 className="h5 mb-0">Users</h2>
        <div>
          <button className="btn btn-secondary btn-sm me-2" onClick={fetchData}>Refresh</button>
          <a className="btn btn-link btn-sm" href={endpoint} target="_blank" rel="noreferrer">API</a>
        </div>
      </div>
      <div className="card-body">
        <p className="text-muted endpoint">Endpoint: {endpoint}</p>
        {loading ? (
          <div>Loading users...</div>
        ) : items.length === 0 ? (
          <div>No users found.</div>
        ) : (
          <div className="table-responsive">
            <table className="table table-striped table-hover">
              <thead>
                <tr>
                  {columns.map(col => <th key={col}>{col}</th>)}
                </tr>
              </thead>
              <tbody>
                {items.map((item, idx) => (
                  <tr key={item.id ?? idx} style={{cursor: 'pointer'}} onClick={() => { setSelected(item); setShowModal(true); }}>
                    {columns.map(col => <td key={col}>{renderCell(item, col)}</td>)}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>

      {showModal && (
        <>
          <div className="modal show d-block" tabIndex="-1" role="dialog">
            <div className="modal-dialog modal-lg" role="document">
              <div className="modal-content">
                <div className="modal-header">
                  <h5 className="modal-title">User Details</h5>
                  <button type="button" className="btn-close" aria-label="Close" onClick={() => setShowModal(false)} />
                </div>
                <div className="modal-body">
                  <pre>{JSON.stringify(selected, null, 2)}</pre>
                </div>
                <div className="modal-footer">
                  <button className="btn btn-secondary" onClick={() => setShowModal(false)}>Close</button>
                </div>
              </div>
            </div>
          </div>
          <div className="modal-backdrop show"></div>
        </>
      )}
    </div>
  );
}
