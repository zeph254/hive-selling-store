import React, { useEffect, useState } from 'react';

const Shop = () => {
    const [users, setUsers] = useState([]);

    useEffect(() => {
        fetch('/api/users')
            .then((response) => response.json())
            .then((result) => setUsers(result))
            .catch((error) => console.log('error', error));
    }, []); // Ensure this array is properly closed

    return (
        <div>
            <h1>Shop</h1>
            {users.map((user) => (
                <p key={user.id}>{user.name}</p>
            ))}
        </div>
    );
};

export default Shop;
cd