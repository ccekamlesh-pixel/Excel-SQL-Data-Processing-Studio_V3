# Excel SQL Data Processing Studio

A professional Windows desktop application for importing, processing, and exporting large datasets using SQL.

## Features

- **Import**: Excel, CSV, TSV, TXT, JSON, XML + SQL Server, MySQL, PostgreSQL, SQLite (Copy Data Mode)
- **Tools**: VLOOKUP, XLOOKUP, Multi-XLOOKUP, Merge VLOOKUP, Table Compare, Duplicate Finder, Fuzzy Matching
- **Query Builder**: Visual drag-and-drop SQL builder + raw SQL editor
- **Export**: Excel, CSV, JSON, XML, Parquet
- **Performance**: DuckDB engine handles 100M+ rows; background workers via QThread
- **UI**: Light/Dark mode, paginated data grid, table explorer, status bar

## Setup

```bash
# 1. Create virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/Mac

# 2. Install dependencies
pip install -r requirements.txt

# For SQL Server support:
pip install pyodbc

# For MySQL:
pip install pymysql

# For PostgreSQL:
pip install psycopg2-binary

# 3. Run
python main.py
```

## Project Structure

```
excel_sql_studio/
├── main.py                    # Entry point
├── requirements.txt
├── core/
│   ├── database.py            # DuckDB engine wrapper
│   ├── importer.py            # File + SQL importers
│   └── exporter.py            # Export to all formats
├── tools/
│   └── processors.py          # VLOOKUP, XLOOKUP, Compare, Fuzzy, etc.
├── workers/
│   └── workers.py             # QThread background workers
├── ui/
│   ├── main_window.py         # Main application window
│   ├── table_explorer.py      # Left panel tree view
│   ├── data_grid.py           # Paginated data table
│   ├── import_dialog.py       # File + SQL import dialogs
│   ├── export_dialog.py       # Export dialog
│   ├── tool_dialogs.py        # Tool dialogs (VLOOKUP etc.)
│   ├── multi_xlookup_dialog.py# Multi-XLOOKUP dialog
│   └── query_builder.py       # Visual + SQL query builder
└── utils/
    ├── logger.py              # Rotating file logger
    └── theme.py               # Light/Dark stylesheet manager
```

## Usage

1. **File → New Project** — creates a `.duckdb` file to store your session
2. **Import → Import File** — load Excel/CSV/JSON/XML data
3. **Import → Import from SQL Database** — connect and copy tables from SQL Server/MySQL/PostgreSQL/SQLite
4. Click any table in the **Table Explorer** to view its data
5. Use **Tools** menu to run VLOOKUP, comparisons, fuzzy match, etc.
6. Use the **Query Builder** tab to write or visually build SQL queries
7. **Export → Export Table** to save results to Excel/CSV/Parquet/etc.

## Logs

Logs are stored at: `~/.excel_sql_studio/logs/app.log`
