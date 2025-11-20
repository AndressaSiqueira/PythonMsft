# Azure Functions OCR Service

An Azure Functions-based OCR (Optical Character Recognition) service that processes PDF documents using Azure Form Recognizer (Cognitive Services) with integrated performance monitoring via Application Insights.

## Features

- **PDF Document Processing**: Extract text and data from PDF documents using Azure Form Recognizer
- **HTTP Trigger**: Simple REST API endpoint for document submission
- **Performance Monitoring**: Real-time latency tracking with Azure Application Insights
- **Containerized Deployment**: Docker support for easy deployment
- **Scalable Architecture**: Built on Azure Functions for automatic scaling

## Prerequisites

Before you begin, ensure you have the following:

- **Python 3.9** or higher
- **Azure Account** with active subscription
- **Azure Cognitive Services** - Form Recognizer resource
- **Azure Application Insights** resource (for metrics)
- **Docker** (optional, for containerized deployment)

## Installation

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/AndressaSiqueira/PythonMsft.git
   cd PythonMsft
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

### Environment Variables

You need to configure the following Azure resources in your project:

1. **Azure Form Recognizer**
   - Update `ENDPOINT` in `ocr.py` with your Form Recognizer endpoint
   - Update `API_KEY` in `ocr.py` with your subscription key

2. **Application Insights**
   - Update the `connection_string` in `metrics.py` with your Application Insights connection string

> **⚠️ Security Note**: For production deployments, store sensitive credentials in Azure Key Vault or use environment variables instead of hardcoding them in source files.

### Configuration Files

- `host.json` - Azure Functions host configuration
- `MyFunction/function.json` - HTTP trigger binding configuration
- `requirements.txt` - Python package dependencies

## Usage

### Running Locally

1. **Start the Azure Functions runtime**
   ```bash
   func start
   ```

2. **Send a POST request with a PDF file**
   ```bash
   curl -X POST http://localhost:7071/api/MyFunction \
     -F "file=@document.pdf" \
     -F "documentId=doc123"
   ```

### Request Parameters

- **file** (required): PDF file to process
- **documentId** (optional): Identifier for tracking purposes (default: "desconhecido")

### Response

- **200 OK**: OCR processing completed successfully
- **400 Bad Request**: No file provided
- **500 Internal Server Error**: Processing error

## Project Structure

```
.
├── MyFunction/              # Azure Function definition
│   ├── __init__.py         # Main function handler
│   └── function.json       # Function bindings configuration
├── ocr.py                  # OCR processing logic
├── metrics.py              # Application Insights metrics tracking
├── requirements.txt        # Python dependencies
├── host.json              # Functions host configuration
├── Dockerfile             # Container image definition
└── README.md              # This file
```

## Docker Deployment

### Build the Docker Image

```bash
docker build -t azure-functions-ocr .
```

### Run the Container

```bash
docker run -p 8080:80 azure-functions-ocr
```

The function will be available at `http://localhost:8080/api/MyFunction`

## Monitoring

The service automatically tracks OCR processing latency metrics:

- **Metric Name**: `ocr_latency`
- **Type**: Distribution
- **Unit**: Milliseconds
- **Buckets**: 100ms, 500ms, 1000ms, 2000ms, 5000ms

View metrics in your Azure Application Insights resource dashboard.

## Dependencies

- **azure-functions**: Azure Functions Python runtime
- **opencensus-ext-azure**: Azure Monitor integration for OpenCensus
- **requests**: HTTP library for API calls

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is available for educational and development purposes.

## Support

For issues or questions, please open an issue in the GitHub repository.

---

**Note**: Remember to secure your API keys and connection strings before deploying to production. Use Azure Key Vault or Azure Functions Application Settings for sensitive configuration.
