import React from 'react';
import './AboutUsPage.css'; // Import CSS file for animations

function AboutUsPage() {
  return (
    <div className="about-us-page animation-fade-in" style={{ textAlign: 'left', padding: '20px' }}>
      <h1>About Us</h1>
      <p>
        This is a powerful application that utilizes Optical Character Recognition (OCR) technology to help you convert various document formats, including whiteboards and handwritten notes, into digital text. It streamlines your workflow by making information easily accessible and searchable.
      </p>
      <h2>Key Features</h2>
      <ul>
        <li>Accurate OCR: Leverages advanced OCR algorithms to ensure high accuracy in text recognition.</li>
        <li>Multiple Format Support: Handles whiteboards, handwritten notes, and potentially PDFs (if implemented).</li>
        <li>User-Friendly Interface: Provides a clear and intuitive interface for easy navigation and task completion.</li>
        {/* Add more features as applicable */}
      </ul>
      <p>
        This application is brought to you by a dedicated team of developers passionate about creating tools that empower users. We are constantly working on improvements and new features to make your experience even better.
      </p>
      <p>
        {/* Include contact information or links for further interaction (optional) */}
        {/* (Optional) Feel free to add contact details, social media links, or a feedback form to encourage user engagement. */}
      </p>
    </div>
  );
}

export default AboutUsPage;