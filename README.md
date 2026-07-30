![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Build Status](https://img.shields.io/badge/tests-passing-brightgreen.svg)

# 🐍 Python Foundations & OOP Portfolio


Welcome to my Python learning repository! This project serves as a step-by-step record of my journey mastering Python fundamentals—from basic CLI tools to data structures and modular programming.

## 📌 Objectives
* Build solid foundational skills in Python logic, syntax, and standard libraries.
* Practice clean coding standards (PEP 8) and clear documentation.
* Maintain a transparent, version-controlled history of progress using Git & GitHub.

---

## 📂 Repository Structure

```text
python-foundations/
├── 01_basics/            # Variables, arithmetic, user input/output
├── 02_control_flow/      # Conditional logic, loops, error handling
├── 03_data_structures/   # Lists, dictionaries, tuples, sets
├── 04_functions_modules/ # Reusable code, standard library modules
└── README.md


A curated collection of 6 hands-on Python projects demonstrating core data structures, object-oriented programming (OOP) principles, algorithmic thinking, and clean code practices.

---

## 🛠️ Tech Stack & Concepts Covered

* **Language:** Python 3.10+
* **Testing:** `pytest`
* **Version Control:** Git & GitHub
* **Core Concepts:**
  * **Data Structures:** Lists, Dictionaries, Sets, Tuples, Stacks (LIFO), Queues (FIFO)
  * **OOP Principles:** Classes, Objects, Methods, Instance Attributes, Inheritance, `super()`, Polymorphism
  * **Python Features:** Magic/Dunder Methods (`__str__`, `__repr__`, `__add__`, `__eq__`, `__len__`, `__getitem__`), Type Annotations, Mutability

---

## 🚀 Projects Overview

| # | Project Name | Directory | Key Concepts Practiced |
| :--- | :--- | :--- | :--- |
| **01** | **Contact Book & Directory** | `02_structures/` | Dictionaries, List Slicing, Case-Insensitive Search, In-Place Mutability |
| **02** | **Skill Matrix & Team Matcher** | `02_structures/` | Sets, Set Operations (`&`, `-`, `\|`, `^`), Roster Deduplication |
| **03** | **Text Editor Action Tracker** | `02_structures/` | Stacks (Undo/Redo via LIFO), Queues (`collections.deque` FIFO), Tuples |
| **04** | **Library Inventory Manager** | `03_oop/` | Classes & Objects, Instance State, Methods, `self` |
| **05** | **E-Commerce Catalog Engine** | `03_oop/` | OOP Inheritance, Method Overriding, `super()`, Polymorphism |
| **06** | **Custom Wallet & Money Object** | `03_oop/` | Magic/Dunder Methods (`__add__`, `__eq__`, `__len__`, `__getitem__`) |

---

## 📦 Project Summaries

### 1. Contact Book & Directory
A CLI contact management tool. Demonstrates nested dictionary storage, list slicing for partial search result pagination, and in-place dictionary updates.

### 2. Skill Matrix & Team Matcher
A technical skill alignment tool using Python sets to analyze team capabilities using set intersection (shared skills), difference (skill gaps), and union (master roster).

### 3. Text Editor Action Tracker
Simulates text editor state management using an **Undo/Redo** stack mechanism (LIFO) alongside an asynchronous **Print Queue** (FIFO using `collections.deque`).

### 4. Library Inventory Manager
An entry-level object-oriented application modeling books and library collections, managing availability states using class methods and instance variables.

### 5. E-Commerce Catalog Engine
An engine handling physical and digital goods using OOP inheritance. Demonstrates `super()` calls and polymorphic fee calculation logic (weight-based shipping vs. digital processing fees).

### 6. Custom Wallet & Money Object
Implements financial value objects with operator overloading using Python magic methods (`Money + Money`, equality checks, and direct sequence indexing on `Wallet`).

---

## ⚡ Quick Start

### 1. Clone the Repository
```bash
git clone [https://github.com/smartexploit/python-foundations.git](https://github.com/smartexploit/python-foundations.git)
cd python-foundations
