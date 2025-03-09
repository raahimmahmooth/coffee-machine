# coffee-machine
# Coffee Machine Project

## Overview

This is a simple Python-based coffee machine program that allows customers to order beverages and maintainers to manage resources. The program supports authentication for maintainers and provides functionalities for ordering, payment processing, and inventory management.

## Features

- Customers can order coffee, make payments, and receive their drinks.
- Maintainers can check inventory levels and replenish resources.
- A password-protected maintainer portal for secure access.
- Handles insufficient resources and incorrect payments.

## Menu

- **Nestea**: 110 Rs
- **Nescafe**: 110 Rs
- **Chai**: 150 Rs

## Setup & Usage

### Running the Program

1. Ensure you have Python installed.
2. Run the script:
   ```sh
   python coffee_machine.py
   ```

### Customer Portal

- Choose from Nestea, Nescafe, or Chai.
- Insert money as prompted.
- If sufficient, coffee is served, and change is returned if needed.
- If insufficient, a retry message appears.

### Maintainer Portal

- Requires password authentication.
- Default password: `123456` (can be changed in the program).
- Options available:
  - `Report`: View current inventory and profit.
  - `Replenish`: Add more ingredients to the inventory.

## Technologies Used

- Python

## Future Improvements

- Add more drink options.
- Implement a graphical user interface (GUI).
- Enhance security with hashed passwords.

## License

This project is open-source and available for modification and distribution.
