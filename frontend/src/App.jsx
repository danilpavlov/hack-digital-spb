import React, {useEffect, useState} from 'react';
import { AppstoreOutlined, MailOutlined, SettingOutlined } from '@ant-design/icons';
import {Menu, Spin} from 'antd';
import axios from "axios";
import CryptocurrencyCard from "./components/CryptocurrencyCard.jsx";


function getItem(label, key, icon, children, type) {
    return {
        key,
        icon,
        children,
        label,
        type,
    };
}

const App = () => {
    const [currencies, setCurrencies] = useState([]) // Список криптовалют
    const [currencyId, setCurrencyId] = useState(1) // Текущая криптовалюта
    const [currencyData, setCurrencyData] = useState(null) // Информация о текущей криптовалюте

    const fetchCurrencies = () => {
        axios.get('http://127.0.0.1:8000/currencies').then(response => {
            const currenciesResponse = response.data
            const menuItems = [
                getItem('Список криптовалют', 'g1', null,
                    currenciesResponse.map(c => {
                        return {label: c.name, key: c.id}
                        }),
                    'group'
                    )
            ]
        setCurrencies(menuItems)
        })
    }

    const fetchCurrency = () => {
        axios.get(`http://127.0.0.1:8000/currencies/${currencyId}`).then(response => {
            setCurrencyData(response.data)
        })
    }

    useEffect(() => {
        fetchCurrencies()
    }, []);

    useEffect(() => {
        setCurrencyData(null)
        fetchCurrency()
    }, [currencyId]); // Когда меняется currencyId, также вызывается эта функция

    const onClick = (e) => {
        console.log('click ', e.key, e.name);
        setCurrencyId(e.key)
    };

    return (
        <div className='flex'>
            <Menu
            onClick={onClick}
            style={{
                width: 256,
            }}
            defaultSelectedKeys={['1']}
            defaultOpenKeys={['sub1']}
            mode="inline"
            items={currencies}
            className='h-screen overflow-scroll'
        />
            <div className='mx-auto my-auto'>
                {currencyData ? <CryptocurrencyCard currency={currencyData}/> : <Spin/>}
            </div>
        </div>
    );
};
export default App;
