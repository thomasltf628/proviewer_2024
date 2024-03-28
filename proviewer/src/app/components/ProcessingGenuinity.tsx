"use client";

import React, { useState, useEffect, ChangeEvent, FormEvent } from 'react';

interface LabelScore {
    label: string;
    score: number;
}

interface ProcessingGenuinityProps {
    submittedValue: string;
    returnthing: string;
}

type ApiResponse = LabelScore[][];

const ProcessingGenuinity: React.FC<ProcessingGenuinityProps> = ({ returnthing }) => {
    const [classificationResult, setClassificationResult] = useState('');
    const [submitStatus, setSubmitStatus] = useState('');

    useEffect(() => {
        const fetchData = async () => {
            if (returnthing !== '') {
            try {

                const response = await fetch('../api/classify', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ "inputs": returnthing })
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
                    setClassificationResult(highestScoreLabel);
                } else {
                    console.log("No data available");
                }
                
                setSubmitStatus('Submitted Successfully!');
                //setSubmitting(false);

            } catch (error) {
                console.error('Error during form submission:', error);
                setSubmitStatus('Submission failed.');
                
            }
        }};
        fetchData();        
    }, [returnthing]);

    return (
        <div>
            {submitStatus && <p>{submitStatus}</p>}
            {classificationResult && (submitStatus == 'Submitted Successfully!') && <p>{classificationResult}</p>}
        </div>
    );
};

export default ProcessingGenuinity;

