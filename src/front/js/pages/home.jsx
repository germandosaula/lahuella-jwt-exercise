import React, { useContext } from "react";
import { Context } from "../store/appContext";

const Home = () => {
    const { store, actions } = useContext(Context);

    return (
        <div className="home-container text-center">
            <div className="jumbotron">
                <h1 className="display-4">¡Welcome to GeekGym!</h1>
                <p className="lead">
                    This is a private Gym for Geeks!.
                </p>
                <hr className="my-4" />
                <p>
                    Start creating your account or login.
                </p>
                <a className="btn btn-primary btn-lg" href="/signup" role="button">
                    SignUp
                </a>
                <a className="btn btn-secondary btn-lg ml-2" href="/login" role="button">
                    Login
                </a>
            </div>
        </div>
    );
};

export default Home;