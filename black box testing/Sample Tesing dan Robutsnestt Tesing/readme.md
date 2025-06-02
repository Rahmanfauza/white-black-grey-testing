# Pengujian Comparison Testing dan Decision Table Testing
## 1. Sample Testing
Sample Testing adalah pendekatan pengujian di mana hanya sebagian (sampel) dari fungsionalitas, data, atau skenario yang mungkin dari suatu aplikasi yang diuji, bukan keseluruhan. Tujuannya adalah untuk mendapatkan indikasi kualitas atau kinerja sistem secara keseluruhan dengan usaha pengujian yang terbatas.

## Sample Testing
| No. | Feature            | Input Data                                                         | Expected Output                                      | Status (✔️/❌) | Screenshot                           |
| --- | ------------------ | ------------------------------------------------------------------ | ---------------------------------------------------- | ------------- | -------------------------------------- |
| 1   | User Registration  | username: `testuser`, email: `test@mail.com`, password: `Test123!` | User is registered successfully, redirected to login |               | (screenshot/registration\_success.png) |
| 2   | User Login         | username: `testuser`, password: `Test123!`                         | User is logged in, redirected to dashboard           |               | (screenshot/login\_success.png)        |
| 3   | Add Task           | title: `Buy Groceries`, description: `Eggs, milk`                  | Task appears in dashboard with correct data          |               | (screenshot/add\_task.png)             |
| 4   | View Task Details  | Click task `Buy Groceries`                                         | Task details page displays correct information       |               | (screenshot/task\_detail.png)          |
| 5   | Update Task Status | Change status to `completed`                                       | Status is updated, success message shown             |               | (screenshot/update\_status.png)        |
| 6   | Delete Task        | Click delete on `Buy Groceries`                                    | Task is removed, success message shown               |               | (screenshot/delete\_task.png)          |
| 7   | Logout             | -                                                                  | User is logged out, redirected to login              |               | (screenshot/logout.png)                |


## 2. Robustness Testing
Robustness Testing adalah jenis pengujian fungsional yang bertujuan untuk memverifikasi seberapa baik sistem perangkat lunak dapat menangani kondisi input yang tidak valid, kondisi lingkungan yang tidak terduga, atau situasi stres lainnya tanpa mengalami kegagalan (crash) atau perilaku yang tidak benar.

| No. | Feature            | Input Data                                                         | Expected Output                                         | Status (✔️/❌) | Screenshot (Optional)                          |
| --- | ------------------ | ------------------------------------------------------------------ | ------------------------------------------------------- | ------------- | ---------------------------------------------- |
| 1   | User Registration  | username: \`\`, email: `test@mail.com`, password: `Test123!`       | Registration fails with error message                   |               | (screenshot/registration\_empty\_username.png) |
| 2   | User Registration  | username: `longusername...` (1000 chars)                           | Application handles gracefully, limit enforced          |               | (screenshot/registration\_long\_username.png)  |
| 3   | User Registration  | username: `testuser`, email: `invalid-email`, password: `Test123!` | Registration fails, error message shown                 |               | (screenshot/registration\_invalid\_email.png)  |
| 4   | Add Task           | title: `@#$%^&*()_+`, description: `123`                           | Task is added, special characters accepted or sanitized |               | (screenshot/add\_task\_special\_chars.png)     |
| 5   | Add Task           | title: (empty), description: `123`                                 | Task creation fails, error message shown                |               | (screenshot/add\_task\_empty\_title.png)       |
| 6   | Update Task Status | status: `completed<script>alert(1)</script>`                       | Input sanitized, XSS not executed                       |               | (screenshot/xss\_attempt.png)                  |
| 7   | SQL Injection Test | username: `' OR '1'='1`, password: `abc`                           | Login fails, SQL injection prevented                    |               | (screenshot/sql\_injection\_attempt.png)       |
| 8   | Large Input Test   | description: 10,000 characters                                     | Application remains stable, data stored or truncated    |               | (screenshot/large\_input\_test.png)            |
