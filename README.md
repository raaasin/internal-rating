﻿# Rating System with Flask

This Flask-based web application creates a rating system to collect ratings for a list of people. The system allows users to rate individuals and stores this information in a CSV file for further analysis.

## Overview

The application provides a user interface where individuals can rate a predefined list of people. Upon submitting their ratings, the data is stored in a CSV file for future reference or analysis.

## Functionality

- **Rating Interface**: Users can access the web interface to view a list of individuals and rate them.
- **CSV Storage**: Ratings submitted by users are stored in a CSV file (`ml.csv`) for easy retrieval and analysis.

## Usage

### Setup

1. Clone the repository containing this Flask application.
2. Ensure you have Python installed on your system.

### Running the Application

1. Open a terminal and navigate to the directory containing the Flask application.
2. Run the Flask application:

   ```bash
   python app.py
   ```
3. Access the application by opening a web browser and navigating to `http://127.0.0.1:5000/`.

### Rating Individuals

1. The main page displays a list of individuals to be rated.
2. Users can rate each individual by selecting a rating and clicking the "Submit" button.
3. Upon submitting a rating, the system stores the data in the `ml.csv` file.

### Accessing Data

- Collected ratings are stored in the `ml.csv` file, which can be accessed for further analysis or processing.

## File Structure

- **app.py**: Contains the Flask application code.
- **templates/index.html**: HTML template for rendering the rating interface.

## Dependencies

- Flask
- CSV module (Python standard library)

## Customization

- Modify the `people` list in `app.py` to include or remove individuals to be rated.
- Customize the HTML template (`index.html`) to change the appearance or layout of the rating interface.

## Contributing

Contributions, bug reports, or feature requests are welcome! Feel free to submit pull requests or open issues.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
