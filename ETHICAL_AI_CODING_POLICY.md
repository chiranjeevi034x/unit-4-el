# Ethical AI Coding Policy
 
**Owner:** D S CHIRANJEEVI RAO (PES1UG25CA034)   **Version:** 1.0   **Date:** 20 November 2026
 
## 1. Purpose
To make sure AI coding assistants such as GitHub Copilot are used safely, legally and transparently.
 
## 2. Data-handling protocols
- Never paste secrets, credentials, personal data or confidential client code into AI prompts.
- Store secrets only in environment variables or a secrets manager; keep .env in .gitignore.
- Use only approved AI tools with organisation-level privacy settings; disable prompt retention where possible.
- Use synthetic or anonymised data for examples and tests.
 
## 3. Review checkpoints before deployment
1. Author review: the developer reads and understands every AI-generated line.
2. Automated checks: unit tests, linting, secret scanning and dependency/licence scan must pass.
3. Peer review: a second developer approves the pull request.
4. Security and fairness check for code that handles personal data or decisions about people.
5. Licence check when a suggestion matches known public code.
 
## 4. Accountability structure
- Developer: fully responsible for any AI-assisted code they commit.
- Reviewer: responsible for verifying review checkpoints were followed.
- Team lead: owns this policy, approves tools and handles incidents.
- Incident process: report, revert, rotate any exposed credentials, and record lessons learned.
 
## 5. Transparency
AI-assisted changes are marked in commit messages or PR descriptions. Third-party code and its licence
are recorded in THIRD_PARTY.md.
 
## 6. Review of this policy
Reviewed every six months or after any AI-related incident.