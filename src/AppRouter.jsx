import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Navbar from "./components/NavBar";
import Header from "./components/Header";
import General from "./components/General";
import Companies from "./components/Companies";

export const routes = [
  { path: "/", name: "Home", component: <Header /> },
  { path: "/General", name: "General", component: <General /> },
  { path: "/Companies", name: " ESG Companies", component: <Companies /> },
];

const AppRouter = () => {
  return (
    <>
      <Router>
        <Navbar />

        <Routes>
          {routes.map((route) => {
            return <Route path={route.path} exact element={route.component} />;
          })}
        </Routes>
      </Router>
    </>
  );
};

export default AppRouter;
