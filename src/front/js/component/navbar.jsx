import React from "react";
import { Link } from "react-router-dom";
import "../../styles/index.css";

const Navbar = () => {
    return (
        <nav className="navbar">
            <Link to="/" className="navbar-brand-link">
                <h1 className="navbar-brand">GeekGym</h1>
            </Link>
            <div className="navbar-links">
                <Link to="/login" className="navbar-link">
                    Login
                </Link>
                <Link to="/signup" className="navbar-link">
                    Signup
                </Link>
            </div>
        </nav>
    );
};

export default Navbar;
