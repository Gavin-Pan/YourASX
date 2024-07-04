import React from "react";
import { NavLink } from "react-router-dom";
import { routes } from "../AppRouter";

function Navbar() {
  return (
    <nav className="bg-gray-800 p-4 font-poppins">
      <div className="container mx-auto flex justify-between items-center">
        <a href="/" className="text-white text-2xl font-bold">
          YOUR ASX
        </a>
        <div className="space-x-4">
          {routes.map((route, index) => {
            return (
              <a className="mt-2" key={index}>
                <NavLink
                  className="text-decoration-none text-white"
                  to={route.path}
                  exact
                  activeClassName="active"
                >
                  {route.name}
                </NavLink>
              </a>
            );
          })}
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
