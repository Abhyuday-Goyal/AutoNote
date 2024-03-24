import React from 'react';

const WhiteboardUploadPage = () => {
  const handleUpload = (event) => {
    const file = event.target.files[0];
    console.log('Uploading file for Whiteboard OCR', file);
    // Add your file upload logic here
  };

  return (
    <div className="file-upload-container">
      <h2 style={{ marginTop: '30px' }}>Whiteboard File Upload</h2>
      <label htmlFor="whiteboard-upload" className="file-upload-button">
        Select File
      </label>
      <input
        type="file"
        id="whiteboard-upload"
        className="file-upload-input"
        onChange={handleUpload}
      />
    </div>
  );
};

export default WhiteboardUploadPage;