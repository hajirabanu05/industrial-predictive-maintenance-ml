import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer
} from "recharts";

function MachineChart({
  title,
  data
}) {
  return (
    <div className="chart-card">

      <h2>{title}</h2>

      <ResponsiveContainer
        width="100%"
        height={300}
      >

        <LineChart data={data}>

          <CartesianGrid strokeDasharray="3 3" />

          <XAxis
            dataKey="timestamp"
          />

          <YAxis
            domain={[0, 1]}
          />

          <Tooltip />

          <Line
            type="monotone"
            dataKey="probability"
          />

        </LineChart>

      </ResponsiveContainer>

    </div>
  );
}

export default MachineChart;