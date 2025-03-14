# JyotishyaMitra Streamlit App

This Streamlit application uses the `jyotishyamitra` library to generate and display Vedic astrology charts (Lagna and Navamsa).

## Features

*   Input birth data (name, gender, date, time, place).
*   Validate birth data using `jyotishyamitra`.
*   Generate Lagna (D1) and Navamsa (D9) charts.
*   Display chart data in a user-friendly text format.
*   Display raw chart data in JSON format.

## Requirements

*   Python 3.6+
*   `streamlit`
*   `pyswisseph==2.8.0.post1`
*    `jyotishyamitra` (Install using pip from the provided GitHub URL)

## Installation

1.  **Clone the repository:**

    ```bash
    git clone <your_repository_url>
    cd <your_repository_directory>
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the app:**

    ```bash
    streamlit run app.py
    ```

2.  **Enter birth data:** Fill in the required fields in the Streamlit web interface.

3.  **Generate Chart:** Click the "Generate Chart" button.

4.  **View Results:** The app will display the selected chart (Lagna or Navamsa) in both text and JSON formats.

## Project Structure

*   `app.py`: The main Streamlit application code.
*   `requirements.txt`:  Lists the required Python packages.
*   `.gitignore`: Specifies files and folders to be ignored by Git.
*   `README.md`: This file, providing project documentation.
*    `jyotishyamitra`: Put the jyotishyamitra package here.

## Troubleshooting

*   **Validation Errors:**  If you see a validation error, double-check the format of your input data.  Ensure all required fields are filled in correctly.
*   **Chart Generation Errors:**  If the chart generation fails, check the error messages in the Streamlit app and your terminal.  It may indicate problems with the input data or the `jyotishyamitra` library itself.

## License

[Specify your project's license here, e.g., MIT, Apache 2.0, etc.]

## Contributing

[If you're open to contributions, describe how others can contribute to your project.]
