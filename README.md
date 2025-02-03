# Personal Finance Manager

A web application to manage personal finances, track expenses, and visualize spending patterns using Streamlit.

## Features

- Set and update monthly budget
- Add, update, and delete expenses
- View expenses in a tabular format
- Delete multiple expenses at once
- Visualize expenses by category and name using pie charts
- Track remaining budget

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/employement-portal.git
    cd employement-portal
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501` to access the application.

## Project Structure

- `app.py`: Main application file containing the Streamlit UI and logic.
- `controllers/budget_controller.py`: Controller for managing budget and expenses.
- `models/`: Directory containing data models.
- `requirements.txt`: List of Python dependencies.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)

