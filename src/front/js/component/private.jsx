import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Private = () => {
    const [message, setMessage] = useState('');
    const navigate = useNavigate();

    useEffect(() => {
        const token = sessionStorage.getItem('token');
        if (!token) return navigate('/login');

        fetch('/private', {
            headers: { Authorization: `Bearer ${token}` },
        })
            .then((response) => {
                if (!response.ok) throw new Error('User without permision');
                return response.json();
            })
            .then((data) => setMessage(data.message))
            .catch(() => navigate('/login'));
    }, [navigate]);

    return <div>{message}</div>;
};

export default Private;
