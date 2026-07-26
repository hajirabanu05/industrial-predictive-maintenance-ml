import { useEffect, useState } from "react";

import API from "../api/api";

import MachineCard from "../components/MachineCard";

import "../styles/machines.css";

function Machines() {

  const [machines, setMachines] =
    useState([]);

  const loadMachines = async () => {

    try {

      const res =
        await API.get("/live-status");

      setMachines(res.data);

    } catch (error) {

      console.error(error);

    }
  };

  useEffect(() => {

    loadMachines();

    const interval = setInterval(
      loadMachines,
      10000
    );

    return () => clearInterval(interval);

  }, []);

  return (
    <div className="machines-container">

      <h1>
        Machine Monitoring
      </h1>

      <div className="machines-grid">

        {machines.map((machine) => (

          <MachineCard
            key={machine.machine_id}
            machine={machine}
          />

        ))}

      </div>

    </div>
  );
}

export default Machines;