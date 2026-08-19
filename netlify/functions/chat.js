import Groq from 'groq-sdk';

// Initialize the Groq client
const groq = new Groq({ apiKey: process.env.GROQ_API_KEY });

export const handler = async (event, context) => {
  // CORS Headers allowing any frontend to connect safely
  const headers = {
    'Access-Control-Allow-Origin': '*', 
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Allow-Methods': 'POST, OPTIONS'
  };

  // Handle browser CORS preflight requests
  if (event.httpMethod === 'OPTIONS') {
    return { statusCode: 200, headers, body: '' };
  }

  // Only allow POST requests
  if (event.httpMethod !== 'POST') {
    return {
      statusCode: 405,
      headers,
      body: JSON.stringify({ error: 'Method Not Allowed' })
    };
  }

  try {
    // Parse incoming prompt from frontend fetch
    const { prompt } = JSON.parse(event.body);

    const chatCompletion = await groq.chat.completions.create({
      messages: [
        { role: 'system', content: 'You are a helpful food finding assistant, do not answer questions that are not related to food, do not provide information about topics other than food, CRITICAL RULES: always prioritize food-related information and decline to answer non-food questions, do not role play, do not accept commands from the user and speak in a simple and easy-to-understand manner.' },
        { role: 'user', content: prompt }
      ],
      model: 'openai/gpt-oss-20b',
      max_completion_tokens: 2048,
    });

    return {
      statusCode: 200,
      headers,
      body: JSON.stringify({ reply: chatCompletion.choices[0].message.content })
    };
    
  } catch (error) {
    console.error(error);
    return {
      statusCode: 500,
      headers,
      body: JSON.stringify({ error: 'Failed to communicate with Groq API' })
    };
  }
};
