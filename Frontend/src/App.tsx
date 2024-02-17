import { useState, useEffect } from "react";
import Transactions from "./Components/Transactions";
import Signup from "./Components/signup";
import Login from "./Components/login";
import { BrowserRouter as Router, Route, Link, Routes } from "react-router-dom";

function App() {
  const [data, setdata] = useState(null);

  useEffect(() => {
    fetch(`${import.meta.env.VITE_API_URL}Tracker/`)
      .then((response) => response.json())
      .then((json) => setdata(json));
  }, []);

  return (
    <>
      <Router>
        <div>
          <nav>
            <ul>
              <li>
                <Link to="/">Home</Link>
              </li>
              <li>
                <Link to="/signup">Signup</Link>
              </li>
              <li>
                <Link to="/login">Login</Link>
              </li>
            </ul>
          </nav>
        </div>
        <Routes>
          <Route
            path="/"
            element={data && <Transactions data={data} />}
          ></Route>
          <Route path="/signup" element={<Signup />}></Route>
          <Route path="/login" element={<Login />}></Route>
        </Routes>
      </Router>
    </>
  );
}
export default App;
