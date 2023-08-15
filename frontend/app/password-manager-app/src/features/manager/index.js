import { useState, useEffect } from 'react';
import axios from 'axios';

export default function Manager() {
    const [accounts, setAccounts] = useState(Array());

    useEffect(() => {
        const getAccounts = async () => {
            const response = await axios.get('http://localhost:8000/item/login');
            console.log(response.data);
            setAccounts(response.data.results);
        }
        getAccounts();
    }, [])


    return (
        <>
            <div>
                {accounts.map(item => {
                    return (
                        <div key={item.name}>
                            <h2>{item.name}</h2>
                            <h4>username: {item.user_name}</h4>
                            <h4>password: {item.password}</h4>
                            <h4><a href={item.url}>Link</a></h4>
                            <p>{item.description}</p>
                        </div>
                    );
                })}
            </div>

        </>
    );
}