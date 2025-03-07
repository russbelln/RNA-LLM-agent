import React from 'react';
import { Button } from 'antd';
import { useNavigate } from 'react-router-dom';
import './HomeButton.css';

const HomeButton = () => {
  const navigate = useNavigate();

  return (
    <Button
      type="primary"
      ghost
      onClick={() => navigate('/')}
      className="custom-home-button"
      shape="round"
    >
      <img src="/icon.png" alt="Home Icon" />
      EduGen
    </Button>
  );
};

export default HomeButton;
