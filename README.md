# WORDY Dictionary

WORDY Dictionary is a simple desktop application built using Python and the Tkinter library. It allows users to search for the definitions of English words.

## Features

- **Search:** Users can enter a word and click on the search button to find its definition.
- **Threading:** The application uses threading to prevent the GUI from freezing while fetching the definition.
- **Dark Theme:** Implemented with the 'darkly' theme for a modern and visually appealing interface.

## Requirements

- Python 3.x
- Tkinter library
- ttkbootstrap library
- requests library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/wordy-dictionary.git
    ```

2. Install the required dependencies:

    ```bash
    pip install ttkbootstrap requests
    ```

3. Run the application:

    ```bash
    python wordy_dictionary.py
    ```

## Usage

1. Enter a word in the text field provided.
2. Click on the "Search" button.
3. The definition of the word will be displayed in the text area below.
4. A loading message will be shown while the definition is being fetched.

## Credits

This application was designed and developed by [Anusigan Sivananthan](https://github.com/your_username).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
