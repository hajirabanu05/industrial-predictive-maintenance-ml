import SeverityBadge from "./SeverityBadge";

function MachineStatusTable({ machines }) {
  return (
    <div className="table-container">

      <h2>Machine Status</h2>

      <table>

        <thead>
          <tr>
            <th>ID</th>
            <th>Status</th>
            <th>Probability</th>
            <th>Health Score</th>
            <th>Severity</th>
          </tr>
        </thead>

        <tbody>

          {machines.map((machine) => (
            <tr key={machine.machine_id}>

              <td>{machine.machine_id}</td>

              <td>{machine.prediction}</td>

              <td>
                {(machine.probability * 100).toFixed(1)}%
              </td>

              <td>
                {machine.health_score}
              </td>

              <td>
                <SeverityBadge
                  severity={machine.severity}
                />
              </td>

            </tr>
          ))}

        </tbody>

      </table>

    </div>
  );
}

export default MachineStatusTable;