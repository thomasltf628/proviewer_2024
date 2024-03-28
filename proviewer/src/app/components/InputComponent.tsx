"use client";

import React, { ChangeEvent, FormEvent } from 'react';

interface InputComponentProps {
    inputValue: string;
    onInputChange: (e: ChangeEvent<HTMLInputElement>) => void;
    onFormSubmit: (e: FormEvent<HTMLFormElement>) => void;
}

const InputComponent: React.FC<InputComponentProps> = ({ inputValue, onInputChange, onFormSubmit }) => {
    return (
        <form onSubmit={onFormSubmit}>
            <label htmlFor="inputField">Enter Text!!!:</label>
            <input 
                type="text" 
                id="inputField" 
                value={inputValue} 
                onChange={onInputChange} 
            />
            <button type="submit">Submit</button>
        </form>
    );
};

export default InputComponent;
