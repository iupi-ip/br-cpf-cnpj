# Changelog

All notable changes to this project will be documented in this file.

The format is based on **Keep a Changelog**  
and this project follows **Semantic Versioning (SemVer)**.

---

## [0.1.0] - 2026-02-05

### Added
- CPF validation using the modulo 11 algorithm
- CNPJ validation with support for:
  - Numeric CNPJ
  - Alphanumeric CNPJ (new official standard)
- Random CPF generator
- Random CNPJ generator (numeric or alphanumeric)
- Input normalization for CPF and CNPJ
- Fully tested codebase with pytest

---

## [0.1.1] - 2026-02-05
### Fixed
- Unique project name


## [0.1.2] - 2026-02-05
### Fixed
- Example code snippets in README.md

## [0.2.0] - 2026-02-20
### Changed
- UV to Pyproject.toml for better dependency management and packaging
- Add coverage reporting with pytest-cov