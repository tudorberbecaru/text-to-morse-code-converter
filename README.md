# Morse Code Encoder/Decoder

This Python script provides a simple text-based interface for encoding and decoding Morse code. It allows users to convert regular text to Morse code and vice versa.

## Usage

1. Run the script:

    ```bash
    python main.py
    ```

2. Follow the on-screen prompts to choose between encoding and decoding. Input the required text or Morse code as prompted.

3. View the result and choose whether to perform another action.

## Requirements

- Python 3.x
- Bidict 0.22.1

Install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

## How it Works

The Morse code dictionary includes mappings for uppercase letters, numbers (0-9), and some common punctuation marks. I used a bidirectional dictionary (from the bidict module) for efficient mapping between Morse code and characters. The bidirectional dictionary allows seamless conversion in both directions, making it an ideal choice for encoding and decoding operations.


- **Encoding:** Converts regular text to Morse code using the provided dictionary.
- **Decoding:** Converts Morse code back to regular text.

```plaintext
Use '.' and '-' for Morse code
Use ' ' to separate letters
Use '/' to separate words
'#' denotes an untranslatable character
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Contributions are welcome! Feel free to open issues or submit pull requests.
