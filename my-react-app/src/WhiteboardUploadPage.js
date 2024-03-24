// WhiteboardUploadPage.js
import React, { useState } from 'react';
import { ArrowDownFromLine } from 'lucide-react';


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
    <div className="file-upload-container flex-col items-center">
      <p className='px-10 text-center text-2xl mt-5 max-w-[100%]'>WhiteBoard Video Upload</p>
      <label htmlFor="notes-upload" className="mt-5 rounded-sm w-[80px] text-sm h-[50px] md:w-[50%] md:h-[60px] md:text-xl bg-headerColor text-textColor font-semibold hover:bg-sidebar flex items-center justify-center cursor-pointer shadow-md">
        Select Video
      </label>
      <input
        type="file"
        id="notes-upload"
        className="file-upload-input"
        accept="video/*"
        onChange={handleUpload}
      />
      <br></br>
      {isProcessing && <div className="loader"></div>}
      {pdfLink && !isProcessing &&(
        <div className="mt-[-20px] pdf-download-link bg-gray-300 border-dashed border-2 border-gray-300 rounded-lg p-1 w-[4vw] flex justify-center">
          <a href={pdfLink} target="_blank" rel="noopener noreferrer" className="generic-download-link">
          <ArrowDownFromLine color='#c00f0f' size={'38px'} />
          </a>
        </div>
      )}
    </div>
  );
};

export default WhiteboardUploadPage;