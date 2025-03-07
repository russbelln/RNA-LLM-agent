import React, { useState } from 'react';
import { Alert, Button, Upload, message, Card, Collapse, Typography, Modal, Spin, Skeleton } from 'antd';
import { InboxOutlined, LoadingOutlined } from '@ant-design/icons';
import ReactMarkdown from 'react-markdown';
import fetchData from '../services/Api';
import './Home.css';

const { Dragger } = Upload;
const { Title, Paragraph } = Typography;
const { Panel } = Collapse;

const Home = () => {
  const [file, setFile] = useState(null);
  const [response, setResponse] = useState(null);
  const [error, setError] = useState('');
  const [useGemini, setUseGemini] = useState(true);
  const [geminiApiKey, setGeminiApiKey] = useState('AIzaSyB5UdWTJSjIvJ0v2ybesu4aH_-CyOQULU8');
  const [isModalVisible, setIsModalVisible] = useState(false);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!file) {
      message.error('Por favor, sube un archivo antes de enviar.');
      return;
    }

    setLoading(true);

    const formData = new FormData();
    formData.append('file', file);
    formData.append('use_gemini', useGemini);
    formData.append('gemini_api_key', geminiApiKey);

    try {
      const result = await fetchData.post('/generate-materials/', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });

      setResponse(result.data);
      setIsModalVisible(true);
    } catch (error) {
      console.error('Error:', error);
      message.error('Error al generar materiales');
    } finally {
      setLoading(false);
    }
  };

  const handleCancel = () => {
    setIsModalVisible(false);
  };

  const uploadProps = {
    name: 'file',
    multiple: false,
    accept: '.pdf,.docx,.txt',
    maxCount: 1,
    beforeUpload: (file) => {
      const acceptedFormats = ['pdf', 'doc', 'docx', 'txt'];
      if (acceptedFormats.includes(file.name.split('.').pop())) {
        setFile(file);
        return false;
      } else {
        message.error('Formato no permitido.');
        return Upload.LIST_IGNORE;
      }
    },
  };

  return (
    <div className="video-background">
      <video autoPlay muted loop>
        <source src="/tmoney.mp4" type="video/mp4" />
        Your browser does not support the video tag.
      </video>

      <div className="home-container">
        <div className="content">
          {!loading ? (
            <>
              <p>Ingresa o arrastra tu archivo para generar contenido educativo</p>
              <Dragger {...uploadProps} className="dragger">
                <p className="ant-upload-drag-icon">
                  <InboxOutlined />
                </p>
                <p className="ant-upload-text">Haz clic o arrastra un archivo a esta área para subirlo</p>
                <p className="ant-upload-hint">
                  Soporte para una carga única. Solo se permiten archivos de tipo .pdf, .docx o .txt
                </p>
              </Dragger>

              <Button type="primary" className="sent-button" onClick={handleSubmit} disabled={loading}>
                Enviar
              </Button>
            </>
          ) : (
            <div className="loading-container">
              <Spin indicator={<LoadingOutlined style={{ fontSize: 80 }} spin />} />
              <p className="generating-text">Generando...</p>
            </div>
          )}

          {error && <Alert message={error} type="error" showIcon />}

          {/* Modal para mostrar la respuesta */}
          <Modal
            title={response?.course_name || "Generando contenido..."}
            visible={isModalVisible}
            onCancel={handleCancel}
            footer={[
              <Button key="close" type="primary" onClick={handleCancel} disabled={loading}>
                Cerrar
              </Button>,
            ]}
            width={800}
            centered
          >
            {loading ? (
              <>
                <p>IA generando contenido, por favor espera...</p>
                <Skeleton active />
                <Skeleton active />
                <Skeleton active />
              </>
            ) : (
              <Collapse accordion>
                {response &&
                  Object.entries(response.materials).map(([tema, contenido]) => (
                    <Panel header={tema} key={tema}>
                      <Collapse accordion>
                        {Object.entries(contenido).map(([seccion, texto]) => (
                          <Panel header={seccion.toUpperCase()} key={seccion}>
                            <div className="scrollable-content markdown-content">
                              <ReactMarkdown>{texto}</ReactMarkdown>
                            </div>
                          </Panel>
                        ))}
                      </Collapse>
                    </Panel>
                  ))}
              </Collapse>
            )}
          </Modal>
        </div>
      </div>
    </div>
  );
};

export default Home;
