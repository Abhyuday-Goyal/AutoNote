// WhiteboardUploadPage.js
import React, { useState } from 'react';

const WhiteboardUploadPage = () => {
  const [pdfLink, setPdfLink] = useState('');
  const [isProcessing, setIsProcessing] = useState(false);

  const handleUpload = (event) => {
    const file = event.target.files[0];
    console.log('Uploading file for Whiteboard OCR', file);

    setIsProcessing(true);
    
    // TODO: Upload file to backend and handle response
  };

  return (
    <div className="file-upload-container">
      <h2>Whiteboard Video Upload</h2>
      <label htmlFor="whiteboard-upload" className="file-upload-button">
        Select Video
      </label>
      <input
        type="file"
        id="whiteboard-upload"
        className="file-upload-input"
        accept="video/*"
        onChange={handleUpload}
      />
      <br></br>
      {isProcessing && <div className="loader"></div>}
      {pdfLink && !isProcessing && (
        <div className="pdf-download-link">
          <a href={pdfLink} target="_blank" rel="noopener noreferrer" className="App-button">
            Download Processed PDF
          </a>
        </div>
      )}
    </div>
  );
};

export default WhiteboardUploadPage;