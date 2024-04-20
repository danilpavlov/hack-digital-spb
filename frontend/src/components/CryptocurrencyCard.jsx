import { useState } from 'react'
import {Card} from "antd";

function CryptocurrencyCard(props) {
    const { currency } = props

    console.log(currency)

    const price = Math.round(currency.quote.USD.price)
    const name = currency.name
    const id = currency.id

    return (
        <div>
            <Card
                title={
                    <div className='flex items-center gap-3'>
                        <img src={"https://s2.coinmarketcap.com/static/img/coins/64x64/" + id + '.png'} alt={''}/>
                        <span>{name}</span>
                    </div>
                }
                bordered={false}
                style={{
                    width: 300,
                }}
            >
                <p>Текущая цена: {price}</p>
                <p>Card content</p>
                <p>Card content</p>
            </Card>
        </div>
    )

}

export default CryptocurrencyCard
