// WhiteboardUploadPage.js
import React, { useState } from 'react';

const WhiteboardUploadPage = () => {
  const [pdfLink, setPdfLink] = useState('');
  const [isProcessing, setIsProcessing] = useState(false);

  const handleUpload = async (event) => {
    const file = event.target.files[0];
    console.log('Uploading file for Whiteboard OCR', file);

    setIsProcessing(true);

    const formData = new FormData();
    formData.append('file', file);
    try {
      // Send the POST request to your custom API
      const response = await fetch('http://127.0.0.1:5000/whiteboard_upload', {
          method: 'POST',
          body:formData
      });

      if (!response.ok) {
        throw new Error('Failed to upload video');
      }

      const contentType = response.headers.get('content-type');
      if (contentType && contentType.includes('application/pdf')) {
          // Open the PDF in a new browser tab
          console.log('PDF response:', response);
          const blob = await response.blob();
          const pdfUrl = URL.createObjectURL(blob);
          setPdfLink(pdfUrl);
          // window.open(url, '_blank');
      } else {
          throw new Error('Invalid response content type. Expected application/pdf');
      }

      // Handle the response here (if needed)
      // const data = await response.json();
      // console.log('Response from server:', data);

      // Reset processing state
      setIsProcessing(false);
  } catch (error) {
      console.error('Error uploading video:', error);
      // Handle error state here (if needed)
      setIsProcessing(false);
  }
    
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