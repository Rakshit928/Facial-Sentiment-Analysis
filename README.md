# Facial Sentiment Analysis with Real-Time Webcam Integration

## Description
This project is a web-based application that uses a pre-trained deep learning model to analyze facial expressions and determine the sentiment/emotion of a user. Unlike traditional upload-based systems, this project integrates with a webcam to capture real-time images, making it more interactive and engaging.

The application is built using Django for the backend, HTML5 and JavaScript for webcam integration, and TensorFlow/Keras for emotion detection. The project processes the captured image, performs sentiment analysis, and displays the results in a user-friendly interface.

## Features
- Real-time webcam integration for capturing user expressions.
- Automatic emotion analysis using a pre-trained deep learning model.
- User-friendly interface with responsive design.
- Built-in preprocessing for captured images.

## Prerequisites
- Python 3.8 or later
- Django
- TensorFlow/Keras
- OpenCV
- A modern web browser that supports webcam access.

## How It Works
1. The user accesses the application through a web browser.
2. The webcam captures the user's image when prompted.
3. The image is processed and analyzed by the backend model.
4. The application displays the detected emotion on the webpage.

## Technologies Used
- **Frontend:** HTML5, CSS3, JavaScript
- **Backend:** Django
- **Model:** TensorFlow/Keras
- **Image Processing:** OpenCV

## Future Enhancements
- Add support for additional emotions.
- Integrate with cloud-based APIs for enhanced performance.
- Implement user session tracking and analytics.
