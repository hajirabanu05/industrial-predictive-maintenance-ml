import { Routes, Route } from "react-router-dom";

import Navbar from "./components/Navbar";

import Dashboard from "./pages/Dashboard";
import Machines from "./pages/Machines";
import History from "./pages/History";

function App() {
  return (
    <>
      <Navbar />

      <Routes>
        <Route
          path="/"
          element={<Dashboard />}
        />

        <Route
          path="/machines"
          element={<Machines />}
        />

        <Route
          path="/history"
          element={<History />}
        />
      </Routes>
    </>
  );
}

export default App;