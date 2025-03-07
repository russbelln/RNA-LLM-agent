import React from 'react';
import { Button } from 'antd';
import { MenuFoldOutlined, MenuUnfoldOutlined } from '@ant-design/icons';

const Header = ({ collapsed, onToggle }) => {
  return (
    <div
      style={{
        padding: 0,
        background: '#f0f2f5',
        display: 'flex',
        alignItems: 'center',
        height: '64px',
        paddingLeft: '16px',
      }}
    >
      <Button
        type="text"
        icon={collapsed ? <MenuUnfoldOutlined /> : <MenuFoldOutlined />}
        onClick={onToggle}
        style={{
          fontSize: '16px',
        }}
      />
    </div>
  );
};

export default Header;
