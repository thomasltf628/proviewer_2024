"use client";

import React, { useState,useEffect, ChangeEvent, FormEvent } from 'react';
import InputComponent from './InputComponent';
import ProcessingGenuinity from './ProcessingGenuinity';
import ProcessingSentiment from './ProcessingSentiment';
import ScrappingForReviews from "./ScrappingForReviews";

interface InputComponentProps {
    inputValue: string;
    warmingUpGen: boolean;
    warmingUpSen: boolean;
    onInputChange: (e: ChangeEvent<HTMLInputElement>) => void;
    onFormSubmit: (e: FormEvent<HTMLFormElement>) => void;
    
}

interface LabelScore {
    label: string;
    score: number;
}

type ApiResponse = LabelScore[][];

const ClassificationComponent = () => {
    const [inputValue, setInputValue] = useState('');
    const [submittedValue, setSubmittedValue] = useState('');
    const [submitting, setSubmitting] = useState(false);
    const [returnthing, setReturnthing] = useState('');
    const updateReturning = (newValue: string) => {
        setReturnthing(newValue);
    };
    const [warmingUpGen, setWarmingUpGen]= useState(false);
    const [warmingUpSen, setWarmingUpSen]= useState(false);        

    const handleInputChange = (e: ChangeEvent<HTMLInputElement>) => {
        setInputValue(e.target.value);    
    };

    const handleFormSubmit = (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault(); // what is that
        setSubmittedValue(inputValue);
    };

    return (
        <div>
            <InputComponent inputValue={inputValue} onInputChange={handleInputChange} onFormSubmit={handleFormSubmit} />
            <ScrappingForReviews submittedValue={submittedValue} returnthing={returnthing} updateReturning={updateReturning}/>
            <ProcessingGenuinity submittedValue={submittedValue} returnthing={returnthing}/>
            <ProcessingSentiment submittedValue={submittedValue} returnthing={returnthing}/> 
        </div>
        
    );
};

export default ClassificationComponent;

// warming up button for api call on serverless api
//             
/*

    const fetchData = async () => {
                
        try {
                    const response = await fetch('https://api-inference.huggingface.co/models/thomas628/my_finefuned_model', {
                        method: 'POST',
                        headers: {
                            "Authorization": "Bearer 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"
                        },
                        body: JSON.stringify({ "inputs": 'dummy input' })
                    });   
                    if (!response.ok) {
                        throw new Error(`Error: ${response.status}`);
                    }    
                    const result: LabelScore[][] = await response.json();
                    setWarmingUpGen(true);
                } catch (error) {
                    console.error('Error during form submission:', error);
                    setWarmingUpGen(false);
                }
                try {
                    const response = await fetch('https://api-inference.huggingface.co/models/thomas628/my_awesome_model', {
                        method: 'POST',
                        headers: {
                            "Authorization": "Bearer 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"
                        },
                        body: JSON.stringify({ "inputs": 'dummy input' })
                    });   
                    if (!response.ok) {
                        throw new Error(`Error: ${response.status}`);
                    }    
                    const result: LabelScore[][] = await response.json();
                    setWarmingUpSen(true);
                } catch (error) {
                    console.error('Error during form submission:', error);
                    setWarmingUpGen(false);
                }
            };
            
    const handleClick = () => {
        fetchData()
        console.log(warmingUpGen, warmingUpSen)
        };

<<<<<<< HEAD

<button onClick={handleClick}>Warming up</button>
*/


