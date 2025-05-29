# Contract Management System (CMS)

A simple command-line interface for managing contracts using SQLite database.

## Features

- View all contracts in a table format
- View contract summaries and details by ID
- Add new contracts
- Update existing contracts
- Delete contracts

## Setup

1. Ensure you have Python 3 installed
2. Clone or download this project
3. The database (`cms.db`) will be automatically created on first run

## Usage

Run the script with various command-line arguments:

```bash
python3 main.py [options]
```

### Available Commands

#### View Operations
- `--view-table` - Display the entire contracts table
- `--summary [ID]` - Show summary for a specific contract ID
- `--details [ID]` - Show detailed information for a specific contract ID

#### Modification Operations
- `--add` - Add a new contract (interactive prompts)
- `--update [ID]` - Update an existing contract by ID (interactive prompts)
- `--delete [ID]` - Delete a contract by ID

### Examples

```bash
# View all contracts
python3 main.py --view-table

# View summary for contract ID 5
python3 main.py --summary 5

# View details for contract ID 3
python3 main.py --details 3

# Add a new contract (followed by prompts)
python3 main.py --add

# Update contract ID 2 (followed by prompts)
python3 main.py --update 2

# Delete contract ID 7
python3 main.py --delete 7

# Show help
python3 main.py --help
```

## Interactive Input

When using `--add` or `--update`, you'll be prompted to enter:
- **Title**: Contract name/title
- **Vendor**: Company or vendor name
- **Cost**: Contract cost/price
- **Pay Cycle**: Payment frequency [yearly, quarterly, monthly, weekly]
- **Expiration Date**: Contract end date (yyyy-mm-dd)

## Project Structure

```
contract-management-system/
├── main.py          # Main CLI application
├── queries.py       # Database query functions
├── setup.py         # Database setup and initialization
└── cms.db          # SQLite database (auto-created)
```

## Requirements

- Python 3.x
