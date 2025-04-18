# Password Generator with QR Code

This is a simple Python script that generates random passwords and provides the option to create a QR code for easy sharing and storing. With increasing concerns about online security, having a reliable password generator can help you create complex passwords that enhance your accounts' safety.

## Features

- Generate secure random passwords with lengths between 8-50 characters
- Includes a diverse character set:
  - Numbers (1-9)
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Special characters (!@#$%^&*)
- Input validation to ensure password length requirements
- QR code generation for easy password sharing
- Error handling for QR code generation
- User-friendly command-line interface

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Password_Generator_with_QRcode.git
cd Password_Generator_with_QRcode
```

2. Install the required dependencies:
```bash
pip install qrcode[pil]
```

## Dependencies

This script requires the following Python libraries:
- `qrcode`: For generating QR codes
- `Pillow (PIL)`: For image processing (required by qrcode)

## Usage

1. Run the script:
``'bash
python password_generator.py
```

2. Follow the interactive prompts:
   - Enter desired password length (8-50 characters)
   - Choose whether to generate a QR code (y/n)

3. The script will:
   - Display your generated password
   - If requested, create a QR code image named `qrcode.png` in the current directory

## Output

- Generated password will be displayed in the console
- QR code image (if selected) will be saved as `qrcode.png`

## Error Handling

- Validates password length input (must be between 8-50 characters)
- Handles invalid numeric inputs
- Manages QR code generation errors gracefully

## Contributing

Feel free to fork this repository and submit pull requests to contribute to this project.

## License

This project is open source and available under the MIT License.

## Author

**Arib Khan**

---

**Note:** Always store your passwords securely and never share them through unsecured channels.