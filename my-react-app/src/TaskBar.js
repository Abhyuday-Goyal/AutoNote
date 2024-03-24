import React from 'react';
import { Link, useNavigate } from 'react-router-dom';

const TaskBar = () => {
  const navigate = useNavigate();

  return (
    <header className="task-bar">
      <div className="logo">AUTO</div>
      <nav>
        <Link to="/" className="task-bar-link" style={{ fontSize: '1.1rem' }}>Home</Link>
        <button onClick={() => navigate('/')} className="task-bar-button" style={{ fontSize: '1.1rem' }}>Process OCR</button>
        <button onClick={() => navigate('/pdf-upload') } className="task-bar-button" style={{ fontSize: '1.1rem' }}>Upload PDF</button>
        <Link to="/about" className="task-bar-link" style={{ fontSize: '1.1rem' }}>About Us</Link>
      </nav>
    </header>
  );
};

export default TaskBar;