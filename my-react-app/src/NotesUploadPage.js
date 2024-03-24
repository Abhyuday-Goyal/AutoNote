// NotesUploadPage.js
import React, { useState } from 'react';

const NotesUploadPage = () => {
  const [pdfLink, setPdfLink] = useState('');
  const [isProcessing, setIsProcessing] = useState(false);

  const handleUpload = async (event) => {
    const file = event.target.files[0];
    console.log('Uploading file for Handwritten Notes OCR', file);

    setIsProcessing(true);
    const formData = new FormData();
    formData.append('file', file);
    try {
      // Send the POST request to your custom API
      const response = await fetch('http://127.0.0.1:5000/hand_upload', {
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
<<<<<<< HEAD
    <h2>Handwritten Notes Video Upload</h2>
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
=======
      <h2>Handwritten Notes Video Upload</h2>
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
      {isProcessing && <div className="loader"></div>}
      {pdfLink && !isProcessing && (
        <div className="pdf-download-link">
          <a href={pdfLink} target="_blank" rel="noopener noreferrer" className="pdf-download-link">
            Download Processed PDF
          </a>
        </div>
      )}
    </div>
  );
>>>>>>> rag-int
};

export default NotesUploadPage;


// // SearchNotesPage.js
// import React, { useState } from 'react';

// const SearchNotesPage = () => {
//   const [file, setFile] = useState(null);
//   const [pdfUrl, setPdfUrl] = useState('');

//   const handleFileChange = (event) => {
//     setFile(event.target.files[0]);
//   };

//   const handleUpload = async () => {
//     if (file && file.type === "video/mp4") {
//       const formData = new FormData();
//       formData.append('file', file);

//       try {
//         // Determine whether it's a hand or whiteboard upload based on file naming or other logic
//         const uploadEndpoint = file.name.includes('hand') ? '/hand_upload' : '/whiteboard_upload';

//         const response = await fetch(http://localhost:5000${uploadEndpoint}, {
//           method: 'POST',
//           body: formData,
//         });

//         if (response.ok) {
//           const blob = await response.blob();
//           const pdfUrl = URL.createObjectURL(blob);
//           setPdfUrl(pdfUrl);
//         } else {
//           console.error('Upload failed', await response.text());
//         }
//       } catch (error) {
//         console.error('Error uploading file:', error);
//       }
//     } else {
//       alert('Please select a .mp4 file.');
//     }
//   };

//   return (
//     <div className="search-notes-container">
//       <div className="search-notes-content">
//         <h1 className="search-notes-title fade-in">Chat with your notes</h1>
//         <div className="search-notes-input-container fade-in">
//           <input
//             type="file"
//             accept=".mp4"
//             onChange={handleFileChange}
//           />
//           <button onClick={handleUpload}>Upload</button>
//         </div>
//       </div>
//       {pdfUrl && (
//         <div className="backend-output-box fade-in">
//           <iframe
//             title="PDF Output"
//             src={pdfUrl}
//             frameBorder="0"
//             width="100%"
//             height="100%"
//           ></iframe>
//         </div>
//       )}
//     </div>
//   );
// };

// export default SearchNotesPage;