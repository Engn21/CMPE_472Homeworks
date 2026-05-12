# Homework 1 — Weather Temperature Guessing Game (TCP Socket)

A TCP client–server application developed for CMPE 472 Homework 1.

## Goal

The server picks a **random city** from `weathers.xlsx` and asks the client to guess that city's temperature within **3 attempts**. After each guess, the client receives a `Higher` / `Lower` hint. A guess is accepted as correct when it falls within a **±10% tolerance** of the actual value.

## Files

| File | Description |
| --- | --- |
| `server.py` | Listens on `localhost:8888`, picks a city from the Excel file, and manages the game. |
| `client.py` | Connects to the server and takes guesses from the user. |
| `weathers.xlsx` | Data source with `City` and `Temp` columns. |
| `CMPE472_HW1EnginSametDedeSection1.pdf` | Homework report. |

## How to Run

```bash
# 1) Start the server
python server.py

# 2) In a new terminal, run the client
python client.py
```

When prompted, enter your temperature guess. Type `END` to terminate the session.

## Requirements

```bash
pip install pandas openpyxl
```
