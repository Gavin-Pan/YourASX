import { useState } from "react";
import reactLogo from "./assets/react.svg";
import Navbar from "./components/NavBar";
import Header from "./components/Header";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import AppRouter from "./AppRouter";

function App() {
  return (
    <>
      <AppRouter />
    </>
  );
}

export default App;
