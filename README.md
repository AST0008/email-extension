# Email Boilerplate Generator Extension

This browser extension helps users generate professional email templates based on the email subject using AI. The extension integrates with a backend powered by the Hugging Face API to create concise, formal boilerplate emails.

---

## Features
- Automatically generates a boilerplate email based on the subject line.
- Adds a "Generate Boilerplate" button in the email composer.
- Supports Gmail and Outlook web interfaces.

---

## Installation

### Prerequisites
- Google Chrome or any Chromium-based browser (e.g., Edge).

### Steps
1. Clone this repository:
    ```bash
    git clone https://github.com/AST0008/email-extension
    cd email-extension/frontend
    ```

2. Open the browser and navigate to `chrome://extensions/`.
3. Enable **Developer Mode** (toggle in the top-right corner).
4. Click **Load unpacked** and select the folder containing the extension files.
5. The extension will now appear in your browser's toolbar.

---

## Usage

1. Open your Gmail or Outlook web client.
2. Compose a new email.
3. Type the subject of your email in the subject field.
4. Click the "Generate Boilerplate" button added to the email composer toolbar.
5. The AI-generated boilerplate email will appear in the body of your email.

---

## Backend API

This extension communicates with a backend hosted on [Railway](https://railway.app/). The backend uses the Hugging Face `flan-t5-large` model to generate email content.

### Backend Repository
If you want to set up the backend yourself, check out the backend code here: [Backend Repository Link](https://github.com/your-username/email-boilerplate-backend).

---

## Configuration

The extension is preconfigured to work with the hosted backend. No additional configuration is needed.

---

## Contributing

Contributions are welcome! If you find bugs or want to add features:
1. Fork this repository.
2. Create a feature branch:
    ```bash
    git checkout -b feature-name
    ```
3. Commit your changes:
    ```bash
    git commit -m "Add a new feature"
    ```
4. Push the branch:
    ```bash
    git push origin feature-name
    ```
5. Open a Pull Request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments
- [Hugging Face](https://huggingface.co/) for providing pre-trained models.
- [Railway](https://railway.app/) for hosting the backend.

---

## Issues

If you encounter any issues, feel free to open an issue in the [GitHub Issues](https://github.com/AST0008/email-extension/issues) section.
