import { useEffect, useState } from "react";

import API from "../api/api";

import SummaryCards from "../components/SummaryCards";
import MachineStatusTable from "../components/MachineStatusTable";
import AlertsTable from "../components/AlertsTable";

import "../styles/dashboard.css";

function Dashboard() {

  const [summary, setSummary] = useState({});
  const [machines, setMachines] = useState([]);
  const [alerts, setAlerts] = useState([]);

  const loadData = async () => {

    try {

      const summaryRes =
        await API.get("/dashboard-summary");

      const machineRes =
        await API.get("/live-status");

      const alertRes =
        await API.get("/alerts");

      setSummary(summaryRes.data);
      setMachines(machineRes.data);
      setAlerts(alertRes.data);

    } catch (error) {

      console.error(error);

    }
  };

  useEffect(() => {

    loadData();

    const interval = setInterval(
      loadData,
      10000
    );

    return () => clearInterval(interval);

  }, []);

  return (
    <div className="dashboard-container">

      <h1>
        Predictive Maintenance Dashboard
      </h1>

      <SummaryCards data={summary} />

      <MachineStatusTable
        machines={machines}
      />

      <AlertsTable
        alerts={alerts}
      />

    </div>
  );
}

export default Dashboard;