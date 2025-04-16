# 🧪 ATG.Party Profile Automation using Python & Selenium

This project automates the process of logging into [ATG.Party](https://atg.party), updating the user’s profile with a new cover photo, a randomized username, and a new bio using Python and Selenium WebDriver.

---

## 📌 Features

- ✅ Website availability check using `requests`
- ⏱️ Measures page load time
- 🔐 Automates login with credentials
- 🖼️ Uploads a new cover photo
- 👤 Updates username with a random suffix
- 📝 Edits and saves bio information
- 📄 Logs key events to console and file (`selenium_log.txt`)

---

## 🚀 Technologies Used

- Python 3
- Selenium WebDriver
- Requests
- Logging module
- WebDriverWait for element handling

---

## 🔧 Setup Instructions

### 1. Install Dependencies

```bash
pip install selenium requests
```
Log:
2025-04-14 11:35:00 - INFO - HTTP Status Code: 200
2025-04-14 11:35:03 - INFO - Page Load Time: 2.45 seconds
2025-04-14 11:35:07 - INFO - Clicked the Login button.
2025-04-14 11:35:10 - INFO - Logged in successfully.
2025-04-14 11:35:15 - INFO - Cover photo selected.
2025-04-14 11:35:20 - INFO - Cover photo saved successfully.
2025-04-14 11:35:23 - INFO - Cover photo popup closed successfully.
2025-04-14 11:35:30 - INFO - Successfully clicked the Save button.
2025-04-14 11:35:31 - INFO - Bio information updated successfully.


