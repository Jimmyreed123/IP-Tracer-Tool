# IP Tracer Tool

## Overview

The **IP Tracer Tool** is a simple Python application that traces the geographical information of a given IP address. It provides details such as the country, city, region, timezone, and internet service provider (ISP) for any valid IP. The tool includes a welcome screen, handles common errors (such as invalid IP input or connection issues), and presents output in color-coded text: green for successful traces and red for errors.

## Features

- **IP Geolocation Lookup**: Get detailed information about an IP address.
- **Color-coded Output**:
  - **Green**: Successful IP trace details.
  - **Red**: Error messages (invalid IP, network issues, etc.).
- **Error Handling**: Handles connection issues, timeouts, and invalid IP addresses.
- **Interactive Interface**: Prompts users for input and allows them to trace multiple IP addresses.
  
## Requirements

- Python 3.x
- `requests` library
- `colorama` library (for colored terminal output)

## Installation

1. **Clone the repository**:

   git clone 

3. **Install dependencies**:
   You can install the required libraries using `pip`:
   
   pip install requests colorama
   

4. **Run the tool**:
   After installing the dependencies, you can run the script using:
   
   python iptracer.py
   

## Usage

1. After running the tool, you'll be greeted with a welcome screen.
2. The tool will prompt you to enter an IP address.
   - Example input: `8.8.8.8`
3. The tool will display detailed information about the IP address, such as:
   - Country
   - Region
   - City
   - Latitude/Longitude
   - ISP and Organization
   - Timezone
4. You can trace multiple IP addresses by entering them one after the other.
5. To exit the tool, type `quit`.

### Example Output

```bash
==================================================
 Welcome to IP Tracer Tool 
==================================================
This tool will provide geographical information about an IP address.
==================================================

Please enter an IP address to trace (or type 'quit' to exit): 8.8.8.8

IP Information:
IP: 8.8.8.8
Country: United States
Region: California
City: Mountain View
ZIP: 94035
Lat/Lon: 37.386, -122.0838
ISP: Google LLC
Org: Google Public DNS
Timezone: America/Los_Angeles
```

### Error Handling

- If the user enters an invalid IP address, the tool will show a red error message.
- If there's no internet connection or the IP lookup service is down, it will inform the user accordingly.

### Example Error Output


Error: invalid query


## Contributing

Feel free to contribute to the project by submitting issues or pull requests on the GitHub repository.

## License

This project is open source and available under the [MIT License](LICENSE).

---

**Created by Isaac**
