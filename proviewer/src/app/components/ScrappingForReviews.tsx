"use client";

import React, { useState, useEffect, ChangeEvent, FormEvent } from 'react';

interface LabelScore {
    label: string;
    score: number;
}

interface ScrappingForReviewsProps {
    submittedValue: string;
    returnthing: string;
    updateReturning: (newValue: string) => void;
}

const ScrappingForReviews: React.FC<ScrappingForReviewsProps> = ({ submittedValue, returnthing, updateReturning}) => {
    
    const [submitStatus, setSubmitStatus] = useState('');

    useEffect(() => {
        const fetchData = async () => {
            if (submittedValue !== '') {
            try {

                const response = await fetch('http://127.0.0.1:5000/scrap_puma', {
                    method: 'GET'
                });

                if (!response.ok) {
                    throw new Error(`Error: ${response.status}`);
                }

                const result = await response.json();
                console.log(result)
                if (result) {
                    console.log(result);
                    updateReturning(result);
                } else {
                    console.log("No data available");
                }
                
                setSubmitStatus('Scrapped Successfully!');
                //setSubmitting(false);

            } catch (error) {
                console.error('Error during form submission:', error);
                setSubmitStatus('Scrapped failed.');
                
            }
        }};
        fetchData();        
    }, [submittedValue]);

    return (
        <div>
            {submitStatus && <p>{submitStatus}</p>}
            {returnthing && (submitStatus == 'Scrapped Successfully!') && <p>{returnthing}</p>}
        </div>
    );
};

export default ScrappingForReviews;

