"use client";

import React, { useEffect, useState, ChangeEvent, FormEvent } from 'react';

interface LabelScore {
    label: string;
    score: number;
}

type ApiResponse = LabelScore[][];

const InputPreview = () => {
    const [inputValue, setInputValue] = useState('');
    const [submitStatus, setSubmitStatus] = useState('');
    const [classReturn, setClassReturn] = useState('');

    const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        setSubmitStatus('Submitting...');

        // API call
        try {
            const response = await fetch('https://api-inference.huggingface.co/models/thomas628/my_finefuned_model', {
                method: 'POST',
                headers: {
                    "Authorization": "Bearer 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"
                },
                body: JSON.stringify({ "inputs": inputValue })
            });

            if (!response.ok) {
                throw new Error(`Error: ${response.status}`);
            }

            const result: LabelScore[][] = await response.json();

            if (result.length > 0 && result[0].length > 0) {
                const highestScoreLabel = result[0].reduce((highest, current) => {
                    return (current.score > highest.score) ? current : highest;
                }).label;
            
                console.log(highestScoreLabel);
                setClassReturn(highestScoreLabel);
            } else {
                console.log("No data available");
            }
            
            setSubmitStatus('Submitted Successfully!');
        } catch (error) {
            console.error('Error during form submission:', error);
            setSubmitStatus('Submission failed.');
        }
    };

    const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
        setInputValue(e.target.value);
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <label htmlFor="inputField">Enter Text!!!:</label>
                <input 
                    type="text" 
                    id="inputField" 
                    value={inputValue} 
                    onChange={handleChange} 
                />
                <button type="submit">Submit</button>
            </form>
            {submitStatus && <p>{submitStatus}</p>}
            {classReturn && <p>{classReturn}</p>}
        </div>
    );
};

export default InputPreview;



