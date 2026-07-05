# Student Management System

A modular, file-based Student Management System built in Python that supports full CRUD operations, bulk data import, sorting/filtering, and report generation for managing student records.

## Features

- **Admissions:** Add new student records to the system
- **Lookup:** Search and retrieve student records by identifier or attribute
- **Updates:** Modify existing student records
- **Deletions:** Remove student records
- **Sorting & Filtering:** Query and organize records by various criteria (e.g., grade, name, ID)
- **Bulk Import:** Import multiple student records at once from CSV, with error logging for malformed entries
- **Reports:** Generate summary reports from student data
- **File Handling:** Reads/writes structured data to CSV for persistence

## Tech Stack

- **Language:** Python
- **Storage:** CSV-based data persistence
- **Architecture:** Modular design — each core operation (admissions, updates, deletions, lookup, sorting/filtering, bulk import) is implemented as a separate module

## Project Structure

```
student-management-system/
├── main.py                  # Entry point — routes user commands to the appropriate module
├── models.py                 # Data model(s) representing a student record
├── admissions.py              # Add new student records
├── lookup.py                  # Search/retrieve records
├── updates.py                  # Modify existing records
├── deletions.py                 # Remove records
├── sorting_filtering.py          # Sort and filter records by criteria
├── bulk_import.py                 # Bulk import from CSV with validation
├── file_handler.py                 # Read/write operations for CSV persistence
├── reports.py                       # Generate summary reports
├── students.csv                      # Student data store
└── import_errors.csv                  # Logs invalid rows encountered during bulk import
```

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Renuka-Kamani/student-management-system.git
   cd student-management-system
   ```

2. No external dependencies beyond the Python standard library (update this if you're using pandas or another library — check your `bulk_import.py`/`file_handler.py` imports).

## Usage

```bash
python main.py
```

Follow the on-screen prompts to add, look up, update, delete, or bulk-import student records. Reports can be generated via the reports module once records exist in `students.csv`.

### Bulk Import Example

```bash
python bulk_import.py --file new_students.csv
```

Any rows that fail validation (missing fields, malformed data) are logged to `import_errors.csv` rather than silently dropped or crashing the import.

## Design Notes

- Each operation (admissions, updates, deletions, etc.) is isolated into its own module, making the codebase easier to extend — new features can be added without touching unrelated logic.
- Bulk import includes basic validation and error logging rather than failing on the first bad row, which reflects a more production-realistic approach to handling messy input data.

## Future Improvements

- Migrate from CSV storage to a proper relational database (e.g., SQLite or MySQL) for better data integrity and query performance
- Add unit tests for each module (admissions, updates, deletions, lookup)
- Add a simple CLI menu or basic web interface (Flask/Streamlit) instead of script-based invocation

## License

This project is open source and available for personal/educational use.
