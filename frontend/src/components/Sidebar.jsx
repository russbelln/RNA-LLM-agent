import React from 'react';
import {
  ContainerOutlined,
  DesktopOutlined,
  MenuFoldOutlined,
  MenuUnfoldOutlined,
  PieChartOutlined,
} from '@ant-design/icons';
import { Button, Menu } from 'antd';
import {Link} from 'react-router-dom';

const items = [
  {
    key: '1',
    icon: <PieChartOutlined />,
    label: <Link to="/">Inicio</Link>,
  },
  {
    key: '2',
    icon: <DesktopOutlined />,
    label: <Link to="/aboutus">Info</Link>,
  },
];

const Sidebar = ({ collapsed, onToggle }) => {
  return (
    <div
      style={{
        width: collapsed ? 80 : 150, // Cambia el ancho según el estado de colapso
        height: '100%',
        background: '#001529',
        transition: 'width 0.3s', // Suaviza la transición
        zIndex: 2
      }}
    >
      <Button
        type="primary"
        onClick={onToggle}
        style={{
          marginBottom: 16,
          marginLeft: collapsed ? 8 : 16,
          transition: 'margin-left 0.3s', // Suaviza la transición del botón
        }}
      >
        {collapsed ? <MenuUnfoldOutlined /> : <MenuFoldOutlined />}
      </Button>
      <Menu
        defaultSelectedKeys={['1']}
        defaultOpenKeys={['sub1']}
        mode="inline"
        theme="dark"
        inlineCollapsed={collapsed}
        items={items}
      />
    </div>
  );
};

export default Sidebar;
