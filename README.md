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
- Python 3.10 (recommended)
- pip (Python package manager)

### Project Configuration

#### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/portscope.git
cd portscope
```

#### 2. Create and Configure .streamlit Directory
Create a `.streamlit` directory and `config.toml` file to manage Streamlit configuration:

```bash
# Create .streamlit directory
mkdir -p .streamlit

# Create config.toml with recommended settings
echo '[scheduler]
pythonVersion = "3.10"' > .streamlit/config.toml
```

**Why this is important:**
- The `.streamlit/config.toml` file ensures consistent Python version usage across different environments.
- It helps prevent compatibility issues between local development and deployment.
- The Python version specified here should match your `runtime.txt` for deployment.

### Setup Virtual Environment

#### Option 1: Using venv (Recommended)

1. **Create a new virtual environment**:
   ```bash
   # For Python 3.10
   python3.10 -m venv venv
   
   # For default Python version
   # python -m venv venv
   ```

2. **Activate the virtual environment**:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```cmd
     .\venv\Scripts\activate
     ```

3. **Upgrade pip**:
   ```bash
   pip install --upgrade pip
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

#### Option 2: Using pipenv

```bash
# Install pipenv if you don't have it
pip install --user pipenv

# Install dependencies
pipenv install -r requirements.txt

# Activate the virtual environment
pipenv shell
```

### 🚀 Running the Application

1. **Ensure virtual environment is activated** (you should see `(venv)` at the start of your terminal prompt)

2. **Start the Streamlit app**:
   ```bash
   streamlit run streamlit_app.py
   ```

3. **Access the application**:
   Open your web browser and navigate to:
   ```
   http://localhost:8501
   ```

## 🔄 Environment Management

### Resetting the Environment

If you encounter issues, you can reset your environment:

```bash
# Deactivate the current virtual environment (if active)
deactivate

# Remove the existing virtual environment
rm -rf venv

# Then follow the setup instructions above to create a fresh environment
```

### Updating Dependencies

1. Activate your virtual environment
2. Update packages:
   ```bash
   pip install --upgrade -r requirements.txt
   ```
3. To update a specific package:
   ```bash
   pip install --upgrade package_name
   ```

## ☁️ Deployment

### Streamlit Cloud (Recommended)

1. Push your code to a GitHub repository
2. Sign up/Log in to [Streamlit Cloud](https://share.streamlit.io/)
3. Click "New app" and select your repository
4. Configure the app:
   - Branch: `main` (or your preferred branch)
   - Main file path: `streamlit_app.py`
   - Advanced settings:
     - Python version: 3.10
     - Command: `sh setup.sh && streamlit run streamlit_app.py`
5. Click "Deploy!"

### Configuration for Deployment

- The `setup.sh` script will:
  - Create necessary directories and config files
  - Install dependencies with `--prefer-binary` flag
  - Set up proper Python version and server configuration
- The `runtime.txt` specifies Python 3.10.13
- All dependencies are specified in `requirements.txt`

## 🛠️ Troubleshooting

### Common Issues

1. **Python Version Mismatch**:
   - Ensure Python 3.10 is installed
   - Verify `runtime.txt` and `.streamlit/config.toml` specify the same Python version

2. **Dependency Conflicts**:
   - Delete the virtual environment and create a fresh one
   - Make sure to use `--prefer-binary` in `requirements.txt`

3. **Port Already in Use**:
   - Change the port: `streamlit run streamlit_app.py --server.port=8502`
   - Or kill existing processes: `pkill -f "streamlit run"`

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
