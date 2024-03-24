// PdfUploadPage.js
import React from 'react';
import { useNavigate } from 'react-router-dom';

const PdfUploadPage = () => {
  const navigate = useNavigate();

  const handleUpload = (event) => {
    const file = event.target.files[0];
    console.log('Uploading PDF file', file);
    // Handle the file upload

    // Redirect to the processing page after upload
    navigate('/processing-page-url');
  };

  return (
    <div className="file-upload-container">
      <h2 style={{ marginTop: '30px' }}>PDF File Upload</h2>
      <label htmlFor="pdf-upload" className="file-upload-button">
        Select File
      </label>
      <input
        type="file"
        id="pdf-upload"
        className="file-upload-input"
        accept=".pdf"
        onChange={handleUpload}
      />
    </div>
  );
};

export default PdfUploadPage;