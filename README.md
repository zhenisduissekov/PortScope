# PortScope - Port Logistics Dashboard

PortScope is a Streamlit-based dashboard for monitoring port logistics operations, specifically designed for the Houston port. The application simulates vessel tracking, shipment status, and delay predictions with an intuitive interface and AI-powered insights.

## 🚀 Features

- **Real-time Shipment Tracking**: Monitor vessel locations and statuses in real-time
- **KPI Dashboard**: View key metrics including average delay, success rate, and active shipments
- **Interactive Map**: Visualize vessel positions on an interactive map
- **Delay Trends**: Analyze delay patterns with a time-series chart
- **Shipment Lookup**: Search for specific shipments by ID
- **AI-Powered Predictions**: Get delay predictions with risk factors and confidence scores
- **Responsive Design**: Works on desktop and tablet devices

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Instructions

#### Using pip (Recommended)

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/portscope.git
   cd portscope
   ```

2. Create and activate a virtual environment:
   ```bash
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   
   # On Windows
   # python -m venv venv
   # venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

#### Using pipenv

```bash
# Install pipenv if you don't have it
pip install --user pipenv

# Clone and navigate to project
pipenv install
pipenv shell
```

## 🚦 Running the Application

1. Activate your virtual environment (if not already activated):
   ```bash
   # macOS/Linux
   source venv/bin/activate
   
   # Windows
   # venv\Scripts\activate
   ```

2. Start the Streamlit app:
   ```bash
   streamlit run streamlit_app.py
   ```

3. Open your web browser and navigate to:
   ```
   http://localhost:8501
   ```

## ☁️ Deployment

### Streamlit Cloud (Recommended)

1. Push your code to a GitHub repository
2. Sign up/Log in to [Streamlit Cloud](https://share.streamlit.io/)
3. Click "New app" and select your repository
4. Configure the app:
   - Branch: `main` (or your preferred branch)
   - Main file path: `streamlit_app.py`
5. Click "Deploy!"

### Other Cloud Providers

#### Heroku

1. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
2. Create a `Procfile` in your project root:
   ```
   web: sh setup.sh && streamlit run streamlit_app.py
   ```
3. Create `setup.sh`:
   ```bash
   mkdir -p ~/.streamlit/
   echo "\
   [server]\n\
   headless = true\n\
   port = $PORT\n\
   enableCORS = false\n\
   \n   " > ~/.streamlit/config.toml
   ```
4. Deploy to Heroku:
   ```bash
   heroku create
   git push heroku main
   heroku open
   ```

## 📂 Project Structure

```
portscope/
├── streamlit_app.py       # Main Streamlit application
├── shipment_generator.py   # Random data generation and AI prediction logic
├── utils.py               # Helper functions and utilities
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🤖 Data Generation

The application generates realistic but simulated data including:
- Vessel information (name, status, location)
- Route details and ETAs
- Delay information with various reasons
- Geographic coordinates near Houston port

## 🛠️ Development

### Running Tests
```bash
# Install test dependencies
pip install pytest

# Run tests
pytest
```

### Code Style
This project follows PEP 8 style guidelines. To check your code:

```bash
pip install flake8 black
flake8 .
black .
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Icons by [EmojiOne](https://www.joypixels.com/)
- Inspired by real-world port logistics challenges
