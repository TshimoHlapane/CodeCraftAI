## 150-Word Summary: How AI Improves Test Coverage

AI-powered testing tools like Testim.io and Selenium with AI plugins can automatically generate, execute, and adapt test cases based on application changes and user behavior. This increases test coverage by identifying edge cases and regression issues that manual testers might overlook. AI can prioritize tests, detect flaky tests, and suggest new scenarios by analyzing historical data and code changes. Compared to manual testing, AI-driven automation is faster, more consistent, and scalable for large applications. In this assignment, the automated script tested both valid and invalid login scenarios, ensuring that authentication logic works as expected. The results showed that automation can quickly validate core functionality and catch errors, freeing up human testers for exploratory or usability testing. Overall, AI enhances reliability and efficiency in software quality assurance.

---

## Screenshots

- [Valid Login Test Result](screenshots\Valid.png)
- [Invalid Login Test Result](screenshots\Invalid.png)

---

### Q2: Compare supervised and unsupervised learning in the context of automated bug detection

**Supervised Learning:**  
Supervised learning uses labeled data (e.g., code labeled as "buggy" or "clean") to train models to detect bugs. Example: Training a classifier to flag code snippets as buggy based on historical bug reports.

**Unsupervised Learning:**  
Unsupervised learning finds patterns or anomalies in unlabeled code. Example: Using clustering or anomaly detection to identify unusual code changes that might indicate bugs.

**Comparison:**  
- Supervised learning is more accurate when labeled data is available but requires manual labeling.
- Unsupervised learning can discover new bug patterns but may produce more false positives.

---

# Automated Login Testing with Selenium

## Task Overview

This task demonstrates how AI-powered tools like Selenium can automate the testing of a login page. Two scenarios were tested:  
- **Valid credentials:** The script attempted to log in using correct username and password.  
- **Invalid credentials:** The script attempted to log in using incorrect username and password.

## Results

- **Valid login:** The script successfully logged in and printed a success message.
- **Invalid login:** The script detected the error message and printed a failure message.
- Screenshots of both test results are included in the submission.

## Summary

Automating login tests with Selenium demonstrates the effectiveness of AI in software testing. The process is efficient, repeatable, and helps ensure that critical authentication features work as intended. AI-driven tools improve coverage, reduce manual effort, and increase confidence in software quality.