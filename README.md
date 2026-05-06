# UX Project - Test Automation Framework

This project is a Python-based automation framework designed for web application testing. It utilizes a modular approach with reusable functions and script-based execution.

## 📂 Project Structure

*   **Functions/**: Contains reusable utility scripts for common web actions.
    *   `Check_URL.py`: Validates page URLs.
    *   `login.py` & `login1.py`: Scripts handling authentication flows.
    *   `XLUtils.py`: Utility for reading and writing data to Excel files.
    *   `dropdown.py`: Handles interaction with dropdown elements.
*   **Scripts/**: Execution scripts for specific test cases and environment activation.
*   **Gateway-gulf/** & **MAC-DATA_SOL/**: Module-specific test scripts (e.g., `login-page.py`, `TC_005.py`).
*   **Include/**: Supplementary files or dependencies.
*   **.idea/**: Configuration files for the PyCharm IDE.

## 🚀 Getting Started

### Prerequisites
*   Python 3.8+
*   Virtual Environment (recommended)

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
