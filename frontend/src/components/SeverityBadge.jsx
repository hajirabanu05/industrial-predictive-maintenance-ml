function SeverityBadge({ severity }) {
  let className = "badge";

  if (severity === "CRITICAL")
    className += " critical";

  else if (severity === "HIGH")
    className += " high";

  else if (severity === "MEDIUM")
    className += " medium";

  else
    className += " low";

  return (
    <span className={className}>
      {severity}
    </span>
  );
}

export default SeverityBadge;