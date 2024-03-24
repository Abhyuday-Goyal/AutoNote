import React from 'react';

const PdfUploadPage = () => {
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
        onChange={(event) => {
          const file = event.target.files[0];
          console.log('Uploading PDF file', file);
          // Add your file upload logic here
        }}
      />
    </div>
  );
};

export default PdfUploadPage;