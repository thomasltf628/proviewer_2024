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
    const [gentimentClassificationResult, setGentimentClassificationResult] = useState<string[]>([]);
    const [sentimentClassificationResult, setSentimentClassificationResult] = useState<string[]>([]);
    const [gensubmitStatus, setGenSubmitStatus] = useState('');
    const [sensubmitStatus, setSenSubmitStatus] = useState('');
    const addGenClassificationResult = (newResult: string) => {
        setGentimentClassificationResult(prevResults => [...prevResults, newResult]);
    };
    const addSentimentClassificationResult = (newResult: string) => {
        setSentimentClassificationResult(prevResults => [...prevResults, newResult]);
    };    
    useEffect(() => {
        const fetchGenData = async () => {
            if (returnthing !== '') {
            for (const sentence of returnthing)
            {
                try {

                    const response = await fetch('http://127.0.0.1:5000/call_genuinity', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ "text": sentence })
                    });



                    if (!response.ok) {
                        throw new Error(`Error: ${response.status}`);
                    }

                    // change
                    const result: LabelScore[][] = await response.json();

                    if (result.length > 0 && result[0].length > 0) {
                        const highestScoreLabel = result[0].reduce((highest, current) => {
                            return (current.score > highest.score) ? current : highest;
                        }).label;
                        console.log(sentence);
                        console.log(result);
                        addGenClassificationResult(highestScoreLabel);
                    } else {
                        console.log("No data available");
                    }
                    
                    setGenSubmitStatus('Submitted Successfully!');
                    //setSubmitting(false);

                } catch (error) {
                    console.error('Error during form submission:', error);
                    setGenSubmitStatus('Submission failed.');
                    
                }
            }
        }};
        fetchGenData();
        
        const fetchSenData = async () => {
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
                    setSenSubmitStatus('Submitted Successfully!');
                } catch (error) {
                    console.error('Error during form submission:', error);
                    setSenSubmitStatus('Submission failed.');
                }
            }
        }};
        fetchSenData();        
    }, [returnthing]);

    return (
        <div>
            {gensubmitStatus && <p>{gensubmitStatus}</p>}
            {sensubmitStatus && <p>{sensubmitStatus}</p>}
            
            <table style={{ borderCollapse: "collapse" }}>
                <thead>
                    <tr>
                        <th style={{ borderCollapse: "collapse" }}>Sentence</th>
                        <th style={{ borderCollapse: "collapse" }}>Gentiment Classification</th>
                        <th style={{ borderCollapse: "collapse" }}>Sentiment Classification</th>
                    </tr>
                </thead>
                <tbody>
                    {gentimentClassificationResult.map((result, index) => (
                        <tr key={index}>
                            <td style={{ border: "1px solid black" }}>{returnthing[index]}</td>
                            <td style={{ border: "1px solid black" }}>{result}</td>
                            <td style={{ border: "1px solid black" }}>{sentimentClassificationResult[index]}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default ProcessingGenuinity;

