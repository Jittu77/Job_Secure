# Job Insights and Freshers Classification Web App

This Flask-based web application provides insights into job postings, such as summarizing job descriptions, extracting key features, and determining whether a job is suitable for freshers. It also supports scraping job details and links from external websites.

## Features

- **Job Scraping**: Fetches job links and descriptions from external websites using BeautifulSoup.
- **Job Classification**: Predicts whether a job is suitable for freshers using pre-trained models (`model1.pkl`, `model2.pkl`, and `model3.h5`).
- **Text Summarization**: Uses EDEN AI API to summarize job descriptions.
- **Feature Extraction**: Extracts features like experience level, skills, and qualifications from job descriptions.
- **User Inputs**: Allows users to input job URLs for analysis or choose job categories to scrape predefined links.
- **Dynamic Information**: Displays job location, salary, and pay period alongside classification results.

## Technologies Used

- **Backend**: Python, Flask
- **Machine Learning**: Pre-trained models (`pickle` and TensorFlow `.h5` format)
- **Scraping**: BeautifulSoup
- **Text Summarization**: EDEN AI API
- **HTML Templates**: Flask `render_template`
- **External APIs**: ScrapingDog API for scraping job links and descriptions.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.7+
- Required Python packages (listed in `requirements.txt`)

### Models

Ensure you have the following model files in the root directory:

- `model1.pkl`
- `model2.pkl`
- `model3.h5`

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-repo/job-insights-app.git
   cd job-insights-app
   ```

2. **Set up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Place Model Files**
   Place `model1.pkl`, `model2.pkl`, and `model3.h5` in the root directory.

5. **Set up API Keys**
   Replace placeholders in the code for the EDEN AI API and ScrapingDog API with your API keys.

6. **Run the Application**
   ```bash
   python app.py
   ```

7. **Access the Application**
   Open your browser and navigate to `http://127.0.0.1:5000/`.

## Usage

1. Navigate to the homepage.
2. **Submit Job URL**: Input a job posting URL to analyze job details.
3. **Select Job Category**: Choose from predefined categories (e.g., QA, ML, Web) to fetch job links.
4. View the results, including job summaries, salary, location, and classification.

## Project Structure

```
.
├── app.py               # Main Flask application
├── model1.pkl           # First ML model
├── model2.pkl           # Second ML model
├── model3.h5            # Third ML model (TensorFlow)
├── requirements.txt     # Python dependencies
├── templates/
│   └── home.html        # HTML template for the app
└── README.md            # Project documentation
```

## API Keys

- **EDEN AI API**: Replace `Authorization` header with your API key in the `summary` function.
- **ScrapingDog API**: Replace the `api_key` parameter in relevant URLs.

## Troubleshooting

- **Model Not Found**: Ensure all model files (`model1.pkl`, `model2.pkl`, and `model3.h5`) are in the root directory.
- **API Errors**: Verify API keys for EDEN AI and ScrapingDog.
- **Package Errors**: Ensure all dependencies are installed via `pip install -r requirements.txt`.

## License

This project is open-source and available under the [MIT License](LICENSE).

---

This README should provide users with the necessary information to set up and use your application. Be sure to modify placeholders like `your-repo` with actual repository details if hosting the project on a platform like GitHub.
