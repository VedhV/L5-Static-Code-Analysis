# Lab 5: Static Code Analysis — Issues and Fixes

| Issue | Type | Original Location | Description | Fix Approach |
|---|---|---|---|---|
| XML-RPC security warning (B411) | High security | Import near line 5 | XML-RPC may be vulnerable to XML attacks. | Removed the unused XML-RPC payment gateway integration from the demo. |
| Jinja2 autoescape disabled (B701) | High security | renderListing | Unescaped titles could allow cross-site scripting (XSS). | Used HTML escaping before inserting the title into the listing. |
| Unsafe Markup usage (B704) | Medium security | bidderBadge | Marking untrusted bidder input as safe could allow XSS. | Escaped bidder text before rendering the badge. |
| Broad exception handling | Code quality | bid | Catching all exceptions could hide unexpected errors. | Handled expected invalid date input specifically. |
| Reserve price not enforced | Logic bug | placeBid | Bids below the reserve could be accepted. | Rejected bids below the reserve price. |
| Minimum increment not enforced | Logic bug | placeBid | Bids could increase by less than the required increment. | Enforced MIN_INCREMENT. |
| Seller self-bidding | Logic bug | placeBid | Sellers could bid on their own items. | Rejected bids made by the seller. |
| String-based closing-time comparison | Logic bug | placeBid | Comparing time strings could produce incorrect results. | Parsed dates and compared datetime values. |
| Missing documentation and naming issues | Code quality | Multiple locations | Missing docstrings and non-standard naming reduced maintainability. | Added docstrings and converted names to snake_case. |
| Formatting violations | Style | Multiple locations | Missing blank lines and overly long lines violated Flake8 rules. | Reformatted the code to pass Flake8. |

## Verification

- Original Pylint score: 6.09/10
- Final Pylint score: 10.00/10
- Final Bandit scan: No issues identified
- Final Flake8 scan: No violations reported
