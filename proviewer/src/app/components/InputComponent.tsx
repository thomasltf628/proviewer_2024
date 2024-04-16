"use client";
import styles from '../InputComponent.module.css';
import React, { ChangeEvent, FormEvent } from 'react';

interface InputComponentProps {
    inputValue: string;
    onInputChange: (e: ChangeEvent<HTMLInputElement>) => void;
    onFormSubmit: (e: FormEvent<HTMLFormElement>) => void;
    setPresetInput: (url: string) => void;
}



const InputComponent: React.FC<InputComponentProps> = ({ inputValue, onInputChange, onFormSubmit, setPresetInput  }) => {
    return (
        <div>
        <form onSubmit={onFormSubmit}>
            <p>Input the link of the product from any of the following websites:</p>
            <br></br>
            <p>Adidas | ETSY | Puma | Roots | Shein | Sportchek</p> 
            <br></br>
            <label htmlFor="inputField">The product link:</label>
            <input 
                type="text" 
                id="inputField" 
                value={inputValue} 
                onChange={onInputChange} 
            />
            <button type="submit">Submit</button>
        </form>
        <br></br>
        <div>
                <h2>Demo link:</h2>
                <button type="button" onClick={() => setPresetInput('https://www.adidas.ca/en/gazelle-shoes/IG6212.html')} className={styles.button}>Adidas Link</button>
                <button type="button" onClick={() => setPresetInput('https://www.etsy.com/listing/1666024421/womens-linen-vest-linen-vest-cropped?ref=listing_page_ad_row-3&sts=1&plkey=9871ca7799275aa94fdf1eda173f6e54ee022fc1%3A1666024421&listing_id=1666024421&listing_slug=womens-linen-vest-linen-vest-cropped')} className={styles.button}>ETSY Link</button>
                <button type="button" onClick={() => setPresetInput('https://ca.puma.com/ca/en/pd/cali-wedge-womens-sneakers/373438?swatch=01&referrer-category=womens-shop-all-womens')} className={styles.button}>Puma Link</button>
                <button type="button" onClick={() => setPresetInput('https://www.roots.com/us/en/organic-original-sweatpant-38090375.html?dwvar_38090375_color=001')} className={styles.button}>Roots Link</button>
                <button type="button" onClick={() => setPresetInput('https://ca.shein.com/SHEIN-Frenchy-Ditsy-Floral-Print-Knot-Front-Split-Thigh-Dress-p-16375006.html?mallCode=1&imgRatio=3-4')} className={styles.button}>Shein Link</button>
                <button type="button" onClick={() => setPresetInput('https://www.sportchek.ca/en/pdp/columbia-women-s-arcadia-ii-hooded-rain-jacket-waterproof-breathable-packable-shell-12545911f.html?loc=plp&&colorCode=COLOUR_BLACK')} className={styles.button}>Sportchek Link</button>
        </div>
        </div>

    );
};

export default InputComponent;
