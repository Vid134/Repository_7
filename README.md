# Repository_7
Selenium automation

Sauce-demo Automation Project:
This repository contains an automation testing project for the Sauce-demo e-commerce demo website. The project is implemented using Python, Selenium WebDriver, and PyTest.

Objective:
To perform automated testing on key user functionalities of the Sauce-demo web application, such as login, cart operations, and logout, ensuring they work as expected.

Technologies Used:
1.Python 3.11
2.Selenium WebDriver
3.PyTest
4.ChromeDriver


✅ Features Covered:

✔ Extracting Webpage Title  
✔ Extracting Current URL  
✔ Extracting Entire HTML Page Content  
✔ Positive Test Cases using PyTest  
✔ Negative Test Cases using PyTest  
✔ HTML Test Report Generation  

Extracted page content saved as:
Webpage_task_11.txt


 🧪 Test Scenarios Implemented:

 ✅ Positive Tests
1️⃣ Verify Title of the Web Application  
2️⃣ Verify Homepage URL  
3️⃣ Verify Dashboard URL after Successful Login  

 ❌ Negative Tests
4️⃣ Wrong Password Login  
5️⃣ Wrong Username Login  
6️⃣ Locked-out User Login  

---

---

🌐 Website Under Test
https://www.saucedemo.com/



Credentials Used: 
Username: standard_user
Password: secret_sauce

---

 📁 Project Structure
Repository_7/

├── sauce-demo.py

├── Webpage_task_11.txt

├── tests/

│   ├── test_saucedemo.py

│   ├── test_saucedemo_negative.py

├── reports/

│   └── report.html

├── pytest.ini

└── README.md

---

 ▶️ How to Run the Tests

1️. Install dependencies:
```bash
pip install selenium pytest pytest-html
2️.Activate Virtual Environment (Windows

venv\Scripts\Activate.ps1

3️.Run Tests with HTML report:

python -m pytest --html=reports/report.html --self-contained-html

 4.HTML Report will be generated in:

reports/report.html



Conclusion:
    All required test cases were automated successfully

Both functional validity and negative behavior were verified

Automation outputs are documented and validated ✅

Screenshots are provided in a folder named screenshots.saucedemo


