"use client";

import React, { useState, useEffect, ChangeEvent, FormEvent } from 'react';

interface LabelScore {
    label: string;
    score: number;
}

interface ProcessingSentimentProps {
    submittedValue: string
    returnthing: string;
}

type ApiResponse = LabelScore[][];

const ProcessingSentiment: React.FC<ProcessingSentimentProps> = ({returnthing}) => {
    const [sentimentClassificationResult, setSentimentClassificationResult] = useState<string[]>([]);
    const [submitStatus, setSubmitStatus] = useState('');
    const addSentimentClassificationResult = (newResult: string) => {
        setSentimentClassificationResult(prevResults => [...prevResults, newResult]);
    };



    useEffect(() => {
        const fetchData = async () => {
            if (returnthing !== ''){   //Prevent from showing "Submission fail" before anybody gives a fuck


            for (const sentence of returnthing) {
                try {
                    const response = await fetch('http://127.0.0.1:5000/call_sentiment', {

                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ "text": sentence })

                    });


                    if (!response.ok) {
                        throw new Error(`Error: ${response.status}`);
                    }

                    const result: LabelScore[][] = await response.json();

                    if (result.length > 0 && result[0].length > 0) {
                        const highestScoreLabel = result[0].reduce((highest, current) => {
                            return (current.score > highest.score) ? current : highest;
                        }).label;
                    

                        console.log(sentence);
                        console.log(result);
                        addSentimentClassificationResult(highestScoreLabel);


                    } else {
                        console.log("No data available");
                    }
                    
                    setSubmitStatus('Submitted Successfully!');
                } catch (error) {
                    console.error('Error during form submission:', error);
                    setSubmitStatus('Submission failed.');
                }

            }


        }
        };
        fetchData();

    }, [returnthing]);

    return (
        <div>
            {submitStatus && <p>{submitStatus}</p>}
            {sentimentClassificationResult && (submitStatus == 'Submitted Successfully!') && <p>{sentimentClassificationResult.map((result, index) => (<p key={index}>{result}</p> ))}</p>}
            
        </div>
    ); 
};

export default ProcessingSentiment;





