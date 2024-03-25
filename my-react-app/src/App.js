// App.js
import React from 'react';
import SearchNotesPage from './SearchNotesPage';
import { useNavigate } from 'react-router-dom';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import WhiteboardUploadPage from './WhiteboardUploadPage';
import NotesUploadPage from './NotesUploadPage';
import PdfUploadPage from './PdfUploadPage';
import AboutUsPage from './AboutUsPage';
import TaskBar from './TaskBar';

function App() {
  return (
    <Router>
      <div className="App">
        <TaskBar />
        <Routes>
          <Route path="/" element={<OptionSelector />} />
          <Route path="/whiteboard" element={<WhiteboardUploadPage />} />
          <Route path="/notes" element={<NotesUploadPage />} />
          <Route path="/search-notes" element={<SearchNotesPage />} />
          <Route path="/pdf-upload" element={<PdfUploadPage />} />
          <Route path="/about" element={<AboutUsPage />} />
        </Routes>
      </div>
    </Router>
  );
}

function OptionSelector() {
  const navigate = useNavigate();

  const handleOptionClick = (path) => {
    navigate(path);
  };

  return (
    <header className="App-header  bg-gray-200 h-[50vh] max-h-[25vh] w-[60vw] overflow-y-auto border-dashed border-2 border-gray-300 p-4 m-auto">
       <p style={{ fontSize: '1.7rem' }}>Choose an option to process OCR</p>
       <button className="App-button whiteboard-btn" style={{ fontSize: '1.1rem' }} onClick={() => handleOptionClick('/whiteboard')}>Whiteboard</button>
       <button className="App-button notes-btn" style={{ fontSize: '1.1rem' }} onClick={() => handleOptionClick('/notes')}>Handwritten Notes</button>
    </header>
  );
}

export default App;