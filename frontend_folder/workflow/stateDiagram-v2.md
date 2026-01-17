```mermaid
stateDiagram-v2
    [*] --> authpageWidget 
    authpageWidget --> inst_dept_year_semesterWidget: Log In
    authpageWidget --> create_account: Create Account
    inst_dept_year_semesterWidget --> syllabus_previewWidget
    syllabus_previewWidget --> inst_dept_year_semesterWidget
    syllabus_previewWidget --> landing_page
```