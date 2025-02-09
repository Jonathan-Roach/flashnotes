# FlashNotes: A Simple Flashcard App

FlashNotes is a Python-based flashcard application that allows you to learn interactively by flipping and cycling through flashcards. It's designed to be lightweight, customizable, and easy to use.

## Features

- **Customizable Data**: Use your own CSV file to create personalized flashcards.
- **Interactive Flashcards**: Flip cards to see both sides of the content.
- **Random Card Selection**: Cards are displayed in a random order to keep learning engaging.
- **Clean Interface**: Simple and intuitive design using Tkinter.

## Getting Started

### Prerequisites

Make sure you have Python 3.x installed on your system along with the following library:
- [Pandas](https://pandas.pydata.org/)  
  Install it via pip:
  ```bash
  pip install pandas
  ```

### Installation

1. Clone this repository or download the code files.
2. Ensure the following folder structure is present:
   ```
   /data
      example.csv
   /images
      card_front.png
      card_back.png
      arrow.png
      flip.png
   flash_notes.py
   ```
3. Replace the `example.csv` file in the `/data` folder with your own CSV file, if desired.

### CSV File Format

The CSV file should have at least two columns, where each row represents a flashcard. For example:

| Front       | Back      |
|-------------|-----------|
| Hello       | Hola      |
| Thank You   | Gracias   |

Update the `fileName` variable in the code to match your CSV file name.

### Running the App

Run the Python script to launch the app:
```bash
python flash_notes.py
```

## Usage

1. Launch the app, and the first flashcard will appear.
2. Use the **flip button** to see the other side of the card.
3. Use the **next button** to display a new random card.

## Customization

- **Data**: Replace the default CSV file with your own to create personalized flashcards.
- **Design**: Customize the card's appearance by modifying the images in the `/images` folder.

## File Details

- **`main.py`**: The main Python script to run the app.
- **`/data/example.csv`**: Example dataset for flashcards.
- **`/images/`**: Contains images for card backgrounds and button icons.

## Example

Given the following CSV:
| Front       | Back      |
|-------------|-----------|
| Bonjour     | Hello     |
| Merci       | Thank You |

FlashNotes will display "Bonjour" on one side of the card and "Hello" on the flip side, ideal for language learning.

---
