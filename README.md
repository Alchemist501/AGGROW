# Aggrow - AI-Powered Agricultural Assistant

Aggrow is an innovative agricultural assistant powered by artificial intelligence, designed to help farmers and agricultural professionals optimize their practices and improve crop yields.

## Features

- **Disease Detection:** Instantly identify plant health issues through image analysis.
- **Optimal Crop Selection:** Find the best crops to grow on your land based on soil analysis and environmental factors.
- **Personalized Recommendations:** Receive customized advice on fertilization, soil management, and pest control.
- **Location Services:** Uses geolocation to provide location-specific recommendations.
- **Multilingual Support:** Offers support in multiple languages, including Hindi and Malayalam.
- **User-Friendly Interface:** Easy-to-use platform for efficient agricultural management.

## Demo

#### 1. Home

![home](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZXJnemNpYjc0ZmM0dmk5NTJxMGlqYnZ6azdkNGg1ajhzcmc2cWoyZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/kDMUEiovRiZb1E4wku/giphy.gif)

#### 2. Crop Recommendation

![cropRecommendation](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGN5cHp2OXV0OXl1N284cm0xamRodndnajhxdzd1czJucGFpdWxubCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/pW4yg0fmQTMMHoMt2p/giphy.gif)

#### 3. Fertilizer Recommendation

![fertRecommendation](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZzY4bDBmNDhwMWhkNDVwamZtcnVrb3Z6amZ4OTVwaDY4eXZkZmh6NyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/bKzXhPQnDTbhWPHPgQ/giphy.gif)

#### 4. Disease Detection

![diseaseDetection](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExeWlibTZpM2w1dzJ2czFhazlneXdjcW0yZ3c3aHNuNHpncTQ4eG9scCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/diBZKNE1az2RJhyCeZ/giphy.gif)

## Getting Started

### Prerequisites

- Node.js (>= 14.0.0)
- npm or yarn
- Python 3.x
- Virtualenv (or venv)

### Installation

1.  Clone the repository:

    ```bash
        git clone https://github.com/Alchemist501/AGGROW.git
        cd frontend
    ```

### To run the website :

1.  Navigate to the backend directory:

    ```bash
    cd ../backend
    ```

2.  Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate      # On Windows
    ```

3.  Install backend dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4.  Run the Flask application:

    ```bash
    python app.py
    ```

    The backend API will be available at `http://localhost:5000` (or the port specified in your Flask app).

##

### Development Phase

**Frontend (React):**

1. Change directory to frontend

   ```bash
   cd frontend
   ```

2. Install dependencies:

   ```bash
   npm install
   # or
   yarn install
   ```

3. Run the development server:

   ```bash
   npm start
   # or
   yarn start
   ```

   The application will be available at `http://localhost:5173`.

**Backend (Flask):**

1.  Navigate to the backend directory:

    ```bash
    cd ../backend
    ```

2.  Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate      # On Windows
    ```

3.  Install backend dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4.  Run the Flask application:

    ```bash
    python3 app.py
    ```

    The backend API will be available at `http://localhost:5000` (or the port specified in your Flask app).

### Building for Production

**Frontend:**

1.  Change directory to frontend

    ```bash
    cd frontend
    ```

2.  Build the application:

    ```bash
    npm run build
    # or
    yarn build
    ```

3.  The production build will be located in the `build` directory.

**Backend:**

- For production deployment, consider using a WSGI server like Gunicorn or uWSGI.
- Refer to Flask deployment documentation for specific production setup instructions.

## Configuration

- **Localization:** Language files are located in the `frontend/assets/locales` directory (frontend). Modify or add JSON files for new languages.
- **API Integration:** Configure your API endpoints and keys in the frontend configuration files. Ensure the frontend is configured to communicate with the Flask backend.
- **Database (Backend):** Configure your database settings in the Flask application.

## Technology Stack

- **Frontend:**
  - React.js
  - Node.js
- **Backend:**
  - Python Flask
  - scikit-learn
  - pytorch

## Contributing

We welcome contributions! Please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them.
4.  Submit a pull request.

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE.

## Contact

For questions or support, please contact me.

## Future Improvements

- Implement a robust soil analysis tool.
- Integrate weather forecasting for better crop planning.
- Add more language options.
- Improve image recognition accuracy for disease detection.
- Add a community forum for farmers to share knowledge.
