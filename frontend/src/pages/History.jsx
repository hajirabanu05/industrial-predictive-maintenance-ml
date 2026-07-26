import { useEffect, useState } from "react";

import API from "../api/api";

import MachineChart from "../components/MachineChart";

import "../styles/history.css";

function History() {

  const [machine1, setMachine1] =
    useState([]);

  const [machine2, setMachine2] =
    useState([]);

  const [machine3, setMachine3] =
    useState([]);

  const loadHistory = async () => {

    try {

      const m1 =
        await API.get("/history/1");

      const m2 =
        await API.get("/history/2");

      const m3 =
        await API.get("/history/3");

      setMachine1(m1.data);
      setMachine2(m2.data);
      setMachine3(m3.data);

    } catch (error) {

      console.error(error);

    }
  };

  useEffect(() => {

    loadHistory();

    const interval = setInterval(
      loadHistory,
      10000
    );

    return () => clearInterval(interval);

  }, []);

  return (
    <div className="history-container">

      <h1>
        Machine Failure Trends
      </h1>

      <MachineChart
        title="Machine 1"
        data={machine1}
      />

      <MachineChart
        title="Machine 2"
        data={machine2}
      />

      <MachineChart
        title="Machine 3"
        data={machine3}
      />

    </div>
  );
}

export default History;