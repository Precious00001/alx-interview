# Star Wars Character Fetcher

## Overview

This Node.js script retrieves information about characters from a specific Star Wars film using the Star Wars API (SWAPI). It takes a film number as a command line argument, fetches details about the film, and then prints the names of the characters associated with that film.

## Prerequisites

- Node.js installed on your machine. You can download it [here](https://nodejs.org/).

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd star-wars-character-fetcher
   ```

3. Install the required Node.js modules:

   ```bash
   npm install
   ```

## Usage

Run the script from the command line, providing the film number as an argument:

```bash
./script.js <film-number>
```

Example:

```bash
./script.js 1
```

## Features

- Retrieves film information from SWAPI based on the provided film number.
- Fetches and prints the names of characters associated with the film.
- Utilizes the 'request' module for making HTTP requests.

## Contributing

If you'd like to contribute to this project, feel free to open an issue or submit a pull request.


---

Feel free to customize the README based on the specific details of your project. Add any additional information, usage examples, or contribution guidelines as needed.
