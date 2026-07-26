function AlertsTable({ alerts }) {
  return (
    <div className="table-container">

      <h2>Recent Alerts</h2>

      <table>

        <thead>
          <tr>
            <th>Machine</th>
            <th>Severity</th>
            <th>Probability</th>
            <th>Root Cause</th>
            <th>Recommendation</th>
          </tr>
        </thead>

        <tbody>

          {alerts.map((alert) => (
            <tr key={alert.id}>

              <td>
                {alert.machine_id}
              </td>

              <td>
                {alert.severity}
              </td>

              <td>
                {(alert.probability * 100).toFixed(2)}%
              </td>

              <td>
                {alert.root_cause}
              </td>

              <td>
                {alert.recommendation}
              </td>

            </tr>
          ))}

        </tbody>

      </table>

    </div>
  );
}

export default AlertsTable;