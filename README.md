# JadwalSarmag

JadwalSarmag is a Python module to parse _specific_ pdf to gives out some data (_i.e. Jadwal Harian, Jadwal Libur, etc._).

## Installation

Install `virtualenv`:

```bash
pip install virtualenv
```

Create new `virtualenv` and install depedencies:

```bash
virtualenv venv &&
. venv/bin/activate && 
pip install -r requirements.txt
```

## Usage

Always use `virtualenv` when interacting with these modules

```bash
. venv/bin/activate
```

### Basic usage

```bash
python parser.py
```