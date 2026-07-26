import SeverityBadge from "./SeverityBadge";

function MachineCard({ machine }) {
  return (
    <div className="machine-card">

      <h2>
        Machine {machine.machine_id}
      </h2>

      <p>
        Status:
        <strong>
          {" "}
          {machine.prediction}
        </strong>
      </p>

      <p>
        Probability:
        {" "}
        {(machine.probability * 100).toFixed(2)}%
      </p>

      <p>
        Health Score:
        {" "}
        {machine.health_score}
      </p>

      <SeverityBadge
        severity={machine.severity}
      />

    </div>
  );
}

export default MachineCard;