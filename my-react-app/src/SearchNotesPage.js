import React, { useState } from 'react';

const SearchNotesPage = () => {
  const [query, setQuery] = useState('');
  const [backendOutput, setBackendOutput] = useState('');

  const handleChange = (event) => {
    setQuery(event.target.value);
  };

  const handleSubmit = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/pdf_chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 'query': query }),
      });
      
      if (!response.ok) {
        throw new Error('Failed to fetch data');
      }
      console.log(response)
      // const data = await response.json();
      // setBackendOutput(data); // Assuming the response is a string or can be converted to one
    } catch (error) {
      console.log("it doesn't work ")
      console.error('Error:', error);
    }
  };

  return (
    <div className="search-notes-container">
      <div className="search-notes-content">
        <h1 className="search-notes-title fade-in">Chat with your notes</h1>
        <div className="search-notes-input-container fade-in">
          <input
            type="text"
            className="search-notes-input"
            placeholder="Type your question here"
            value={query}
            onChange={handleChange}
          />
          <button className="App-button" onClick={handleSubmit}>
            Submit
          </button>
        </div>
      </div>
      <div className="backend-output-box fade-in">
        {backendOutput && <p>{backendOutput}</p>}
      </div>
    </div>
  );
};

export default SearchNotesPage;
