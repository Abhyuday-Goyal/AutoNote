// NotesUploadPage.js
import React, { useState } from 'react';

const NotesUploadPage = () => {
  const [pdfLink, setPdfLink] = useState('');
  const [isProcessing, setIsProcessing] = useState(false);

  const handleUpload = (event) => {
    const file = event.target.files[0];
    console.log('Uploading file for Handwritten Notes OCR', file);

    setIsProcessing(true);
    
    // TODO: Upload file to backend and handle response
    // Use the response from the backend to set the PDF link
    // Example:
    // fetch('YOUR_BACKEND_ENDPOINT', {
    //   method: 'POST',
    //   body: formData,
    // })
    // .then(response => response.json())
    // .then(data => {
    //   setPdfLink(data.pdfLink); // Set the PDF link from backend response
    //   setIsProcessing(false);
    // })
    // .catch(error => {
    //   console.error('Error:', error);
    //   setIsProcessing(false);
    // });
  };

  return (
    <div className="file-upload-container">
      <h2 style={{ marginTop: '30px' }}>Handwritten Notes Video Upload</h2>
      <label htmlFor="notes-upload" className="file-upload-button">
        Select Video
      </label>
      <input
        type="file"
        id="notes-upload"
        className="file-upload-input"
        accept="video/*"
        onChange={handleUpload}
      />
      {isProcessing && <p style={{ marginTop: '20px' }}>Processing...</p>}
      {pdfLink && !isProcessing && <a href={pdfLink} style={{ display: 'block', marginTop: '20px' }}>Download Processed PDF</a>}
    </div>
  );
};

export default NotesUploadPage;
