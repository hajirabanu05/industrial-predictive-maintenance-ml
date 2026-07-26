import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="navbar">
      <div className="logo">
        Predictive Maintenance
      </div>

      <div className="nav-links">
        <Link to="/">Dashboard</Link>
        <Link to="/machines">Machines</Link>
        <Link to="/history">History</Link>
      </div>
    </nav>
  );
}

export default Navbar;