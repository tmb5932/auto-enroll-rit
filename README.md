# Semi-Automated Class Enrollment Script #
This Python script uses Selenium to almost entirely automatically enroll in classes at a specified time. It is designed for automating the enrollment process in RIT's online academic portal (SIS). The script logs into the user’s account, navigates to the enrollment page, and enrolls in the desired classes as soon as the specified enrollment time is reached.

## Features ##
- Automated login using stored credentials
- Automatic selection of classes and completion of the enrollment process
- Configurable to support various numbers of classes and enrollment times

## Requirements ##
- **Python 3.x**
- **Selenium**: Install using `pip install selenium`
- **dotenv**: Used for loading environment variables securely. Install via `pip install python-dotenv`
- **Chrome WebDriver**: Download and ensure it's compatible with your installed Chrome browser version.
- **.env File**: To securely store your login credentials and portal URL.

## Setup ##

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/automatic-class-enrollment.git
   cd automatic-class-enrollment
    ```
2. **Create a .env File**  
Add your SIS credentials and portal URL in a `.env` file:  
    ```plaintext
    WEB_ADDRESS="Web_address_for_SIS_enroll_and_search_page"  
    USERNAME="your_rit_username"  
    PASSWORD="your_rit_password"  
    ```

3. **Set Variables**  
In `enroll.py`, set `enroll_time` to your specified enrollment time, and `num_classes` to the number of classes in your shopping cart.  


4. **Run the Program**  
    ```bash
    python enroll.py

## Authors Note / Disclaimer ##
This script was developed for fun and as a way to learn more about Selenium and automated web testing. It was created, in theory, to optimize the frenzy of class enrollment day at RIT by automating some of the repetitive actions needed.

It’s designed solely for educational purposes and may require adjustments to work in other environments or if the SIS system changes.

**I am not implying through the development of this script that others should use it for class enrollment, nor am I suggesting that using automation tools like this is permitted by RIT or any other institution.** 

Please consult your institution’s policies before considering any form of automated access to their systems. 

Use this script responsibly and in accordance with your institution’s policies. This tool is shared strictly for educational and personal use, and I am not responsible for any misuse or potential policy violations.

