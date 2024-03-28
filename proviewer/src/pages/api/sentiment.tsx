import type { NextApiRequest, NextApiResponse } from 'next';

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
    if (req.method === 'POST') {
        try {
            const response = await fetch('https://api-inference.huggingface.co/models/thomas628/my_awesome_model', {
                method: 'POST',
                headers: {
                    "Authorization": `Bearer ${process.env.SECRET_API_KEY}`
                },
                body: req.body
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const result = await response.json();
            res.status(200).json(result);
        } 
        catch (error) {
            if (error instanceof Error) {
                // 'error' is now narrowed down to type 'Error', so accessing 'message' is safe
                res.status(500).json({ message: error.message });
            } else {
                // Handle cases where 'error' is not an Error instance
                res.status(500).json({ message: 'An unknown error occurred' });
            }
        }
        
    } else {
        res.setHeader('Allow', ['POST']);
        res.status(405).end(`Method ${req.method} Not Allowed`);
    }
}