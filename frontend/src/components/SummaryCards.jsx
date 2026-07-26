function SummaryCards({ data }) {
  return (
    <div className="summary-grid">

      <div className="summary-card">
        <h3>Machines</h3>
        <p>{data.machines}</p>
      </div>

      <div className="summary-card">
        <h3>Healthy</h3>
        <p>{data.healthy}</p>
      </div>

      <div className="summary-card">
        <h3>Warning</h3>
        <p>{data.warning}</p>
      </div>

      <div className="summary-card">
        <h3>High Risk</h3>
        <p>{data.high_risk}</p>
      </div>

      <div className="summary-card">
        <h3>Critical</h3>
        <p>{data.critical}</p>
      </div>

      <div className="summary-card">
        <h3>Alerts</h3>
        <p>{data.alerts}</p>
      </div>

    </div>
  );
}

export default SummaryCards;