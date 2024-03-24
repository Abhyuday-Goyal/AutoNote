import React from 'react';

const NotesUploadPage = () => {
  const handleUpload = (event) => {
    const file = event.target.files[0];
    console.log('Uploading file for Handwritten Notes OCR', file);
    // Add your file upload logic here
  };

  return (
    <div className="file-upload-container">
      <h2 style={{ marginTop: '30px' }}>Handwritten Notes Upload</h2>
      <label htmlFor="notes-upload" className="file-upload-button">
        Select File
      </label>
      <input
        type="file"
        id="notes-upload"
        className="file-upload-input"
        onChange={handleUpload}
      />
    </div>
  );
};

export default NotesUploadPage;