import React, { useState } from 'react';
import './AboutUs.css';
import { Button } from 'antd';
import ReactPlayer from 'react-player';

const githubUsers = [
  { username: 'russbelln', profileUrl: 'https://github.com/russbelln' },
  { username: 'fmunoze', profileUrl: 'https://github.com/fmunoze' },
  { username: 'Rypsor', profileUrl: 'https://github.com/Rypsor' },
  { username: 'psga', profileUrl: 'https://github.com/psga' },
];

const AboutUs = () => {
  const [showVideo, setShowVideo] = useState(false);
  const handleAboutClick = () => {
    window.location.href = 'https://online.fliphtml5.com/rpiit/jkej/'; // Cambia este enlace al que desees
  };
  const handleSourceCodeClick = () => {
    window.location.href = 'https://github.com/russbelln/RNA-LLM-agent'; // Cambia este enlace al que desees
  };

  return (
    <div className="about-us-container">
      <h1>Acerca del proyecto</h1>
      <p>This project is dedicated to providing personalized recommendations using advanced AI algorithms. Our goal is to help users make smarter choices by leveraging the power of deep learning.</p>
      
      <div className="button-container">
        <Button
          shape="round"
          className="watch-video-button"
          onClick={() => setShowVideo(true)}
        >
          Ver video
        </Button>
        <Button 
          className='about-button'
          shape="round"
          onClick={handleAboutClick} 
          style={{ marginLeft: '10px' }}
        >
          Acerca del proyecto
        </Button>
        <Button 
          className='source-code-button'
          shape="round"
          onClick={handleSourceCodeClick} 
          style={{ marginLeft: '10px' }}
        >
          Código fuente
        </Button>
      </div>

      <div className="avatar-container">
        <p className="creators-text">Maintainers:</p>
        <div className="avatar-row">
          {githubUsers.map((user) => (
            <a
              href={user.profileUrl}
              target="_blank"
              rel="noopener noreferrer"
              key={user.username}
              className="avatar-link"
            >
              <img
                src={`https://github.com/${user.username}.png`}
                alt={user.username}
                className="avatar-img"
              />
            </a>
          ))}
        </div>
      </div>

      {/* Modal del video */}
      {showVideo && (
        <div className="overlay">
          <div className="video-container">
            <button className="close-button" onClick={() => setShowVideo(false)}>
              ✖
            </button>
            <ReactPlayer
              url="https://youtu.be/5KymhNlCQR8"
              controls
              playing
              width="100%"
              height="100%"
            />
          </div>
        </div>
      )}
    </div>
  );
};

export default AboutUs;