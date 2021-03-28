# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- `data.py` to acquire data through API
- `feature.py` to perform feature engineering and include desired datasets
- `portfolio.py`:
    - Trade: Buy
    - Trade: Sell
    - Trade: Fee
    - Import: Portfolio: Takes in a specific format of CSV
    - Update: Portfolio: Update Portfolio
    - Export: Portfolio: Export in CSV

## [0.1.0] - 2021-03-27
### Added
- `Portfolio.search()` that queries keywords on Yahoo! Finance autocomplete API
- Added Docstrings to `portfolio.py`

### Changed
- In `Portfolio()` class, `self.balance` changed to `self.cash` to allow trade features

## [0.0.1] - 2021-03-26
### Added
- This CHANGELOG file to keep track of changes happening around this long-term project
- README to indicate that this project is based on a previous project
