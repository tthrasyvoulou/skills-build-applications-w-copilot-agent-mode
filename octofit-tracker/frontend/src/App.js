import React from 'react';
import './App.css';
import { Routes, Route, NavLink } from 'react-router-dom';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

export default function App() {
  return (
    <div>
      <nav className="navbar navbar-expand-lg navbar-light bg-light">
        <div className="container">
          <NavLink className="navbar-brand" to="/">OctoFit Tracker</NavLink>
          <button
            className="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon" />
          </button>

          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav ms-auto">
              <li className="nav-item">
                <NavLink to="/activities" className={({isActive}) => 'nav-link' + (isActive ? ' active' : '')}>Activities</NavLink>
              </li>
              <li className="nav-item">
                <NavLink to="/workouts" className={({isActive}) => 'nav-link' + (isActive ? ' active' : '')}>Workouts</NavLink>
              </li>
              <li className="nav-item">
                <NavLink to="/teams" className={({isActive}) => 'nav-link' + (isActive ? ' active' : '')}>Teams</NavLink>
              </li>
              <li className="nav-item">
                <NavLink to="/users" className={({isActive}) => 'nav-link' + (isActive ? ' active' : '')}>Users</NavLink>
              </li>
              <li className="nav-item">
                <NavLink to="/leaderboard" className={({isActive}) => 'nav-link' + (isActive ? ' active' : '')}>Leaderboard</NavLink>
              </li>
            </ul>
          </div>
        </div>
      </nav>

      <div className="container py-4">
        <Routes>
          <Route path="/" element={<div className="card"><div className="card-body">Welcome to OctoFit Tracker</div></div>} />
          <Route path="/activities" element={<Activities />} />
          <Route path="/workouts" element={<Workouts />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/users" element={<Users />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
        </Routes>
      </div>
    </div>
  );
}
