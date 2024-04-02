# Library Management System

The Library Management System is a Python-based application designed to manage a library's catalog and handle different types of users with varying permissions, such as librarians and patrons. It leverages a role-based access control (RBAC) system for managing user permissions.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have Python 3 installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Setting Up the Project

1. **Clone the Repository**

   First, clone this repository to your local machine using Git.

   ```bash
   git clone https://github.com/bekbull/css217-assignment-2 220107088_assignment_2
   cd 220107088_assignment_2
   ```

2. **Create a Virtual Environment**

   A virtual environment is a self-contained directory that contains a Python installation for a particular version of Python, plus a number of additional packages.

   Create a virtual environment in the project directory by running:

   ```bash
   python3 -m venv venv
   ```

   This command creates a directory called `venv` in your project directory, containing a copy of the Python and pip binaries, among other things.

3. **Activate the Virtual Environment**

   Before you can start installing or using packages in your virtual environment, you need to activate it. The activation command varies depending on your operating system.

   - **On macOS and Linux:**

     ```bash
     source venv/bin/activate
     ```

   - **On Windows:**

     ```cmd
     .\venv\Scripts\activate
     ```

   You'll know the virtual environment is activated because your command prompt will change to show the name of the virtual environment. It will look something like `(venv) user@hostname:~/library-management-system$`.

4. **Install Required Packages**

   With your virtual environment active, install the required packages using `pip`. The required packages should be listed in a `requirements.txt` file. If your project doesn't have many dependencies, you could manually install them as needed.

   ```bash
   pip install -r requirements.txt
   ```

   or if there are no specific dependencies:

   ```bash
   pip install some-package-name
   ```

### Running the Application

With the setup complete, you can now run the application:

```bash
python app.py
```

## Using the Application

- Follow the command-line prompts to interact with the library management system.
- To perform actions such as adding items to the catalog or borrowing items, log in with the appropriate user credentials (librarian or patron).

## Closing the Application

To exit the application, follow the exit instructions provided in the command-line interface. To deactivate the virtual environment, use the command:

```bash
deactivate
```

This will return you to your system's default Python interpreter.

## Contributing

Please read [CONTRIBUTING.md](https://your-repository-url/CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

---

Replace placeholders like `https://your-repository-url.git` with your actual repository URL and adjust the instructions as needed based on your project's requirements and setup.
