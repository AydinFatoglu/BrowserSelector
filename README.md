# Browser Selector

**Browser Selector** is a simple GUI application for Windows that allows users to choose between two predefined browsers to open a specified URL or application. Built with `wxPython`, this lightweight tool provides an intuitive interface with two buttons, each representing a browser, so users can easily select their preferred option.

## Features

- **Customizable Commands**: Lets you specify commands for each button, supporting any browser or application that can be launched from the command line.
- **Minimal Interface**: A clean and user-friendly design without distractions, focusing solely on launching your specified applications or URLs.
- **Error Handling**: Shows a message box with usage instructions if commands are missing, providing clear guidance for users.

## Usage

Run the application from the command line, specifying the commands for each button:

## Arguments

    --c1: Command for the first button (e.g., launching Chrome).
    --c2: Command for the second button (e.g., launching Edge).

    ```shell
    browserselector.exe --c1="start chrome https://yoursite.com" --c2="start msedge https://yoursite.com"

Replace start chrome or start msedge with any other compatible browser or application command.

This project is suitable for quick-access applications, kiosk setups, or environments where users need to select between two predefined browsing or application options.

