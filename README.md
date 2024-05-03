# Wildfire Prevention Backend

## Overview

This repository contains the backend code for wildfire prevention system. The system collects data from sensors (heat, humidity, wind speed) connected to a Raspberry Pi. This data is then sent to a Django backend for processing.

## Features

- Collects data from heat, humidity, and wind speed sensors via Raspberry Pi.
- Django REST API to retrieve sensor data through POST requests.
- Utilizes a set of parameters based on observatory data for wildfire prediction.
- Provides API endpoints for notification functionality when conditions are met.
- Includes a result display URL for observing wildfire conditions.
- Offers a test API for manual control of input data to simulate different wildfire conditions.

## Usage

1. Install required dependencies.
2. Connect sensors to Raspberry Pi and ensure it is active.
3. Start the Django backend.
4. Access the API endpoints for retrieving sensor data and controlling test conditions.

## Repository Data

For analysis and testing, refer to the following repository data:
- [Demo URL]
- ([link_to_repository_data](https://wildfire-prevention-backend.vercel.app/api/sensor_data/))

## Frontend
<img width="223" alt="f1" src="https://github.com/jay6294100293/wildfire_prevention_backend/assets/142631405/f5886ce9-0d24-4adc-b660-b13e9751d836">

The current status is displayed in a simple frontend. The API can be further integrated with mobile notifications, cellular notifications, and IoT devices for real-time alerts.

## Contributors

- [Mrityunjay Gupta]([link_to_profile](https://github.com/jay6294100293)) - Backend Management and Data Analytics
- [Kush Patel ](link_to_profile) - Power Bi Dashboard and Data Analytics
- [Sidharth Alashi ](link_to_profile) - Historic measurement of wildfire and Data Analytics

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.


