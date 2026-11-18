# ShopSmart Account and Customer Support FAQ

> **Fictional notice:** ShopSmart is a fictional company and these policies are fictional. This document was created for a software demonstration (a college RAG and AI-agent project). It is not real company policy, not financial advice and not legal advice.

| Field | Value |
|---|---|
| Company | ShopSmart (fictional online multi-category marketplace, India) |
| Document ID | SS-FAQ-ACC-007 |
| Version | 1.0 |
| Effective date | 1 Nov 2026 |
| Last updated | 28 Oct 2026 |
| Category tag | account_support |
| Currency and time zone | INR (₹); IST |
| Related documents | SS-FAQ-PAY-004 (Payment and Billing), SS-POL-RET-001 (Return and Refund), SS-POL-SHP-002 (Shipping and Delivery), SS-POL-CAN-003 (Order Cancellation), SS-POL-DMG-008 (Damaged, Missing and Incorrect Items), SS-POL-WAR-005 (Warranty), SS-CAT-PRD-006 (Product Catalog) |

**Suggested RAG metadata:** doc_id: SS-FAQ-ACC-007 | category: account_support | version: 1.0 | effective_date: 2026-11-01 | doc_type: faq | region: IN | live_data_needed: true (for account data, Rewards balance, order history and ticket status)

## 1. Scope and Purpose

This document answers common questions about a ShopSmart customer account and about contacting customer support. It covers account creation, login problems, login lockout, password reset, profile updates, saved addresses, changing the address on an existing order, order history, Rewards points, account security, contacting support, ticket escalation, complaints and account deletion.

It does not decide order, return, refund or warranty outcomes. Those are covered by the related documents listed above. This document explains how the account works and how to reach and escalate support.

The AI assistant must use only the rules written here and the live database. If a rule is not written here, it is marked **requires clarification** and the assistant must not invent it.

## 2. Static vs Live Information

| Type | What belongs here | Source |
|---|---|---|
| Static (this document) | Password reset link validity, lockout rule, address rules, order-history period, Rewards earning, redeeming, expiry and reversal rules, account deletion rules, support channels and hours, escalation levels, FAQs | Retrieved documents |
| Live (database or tools) | Account data, whether an account is currently locked, Rewards balance and expiry dates, order history, order and refund status, ticket status, saved addresses, whether an account has pending orders or refunds | MongoDB tools |

**Rule for the AI assistant:** Never state a specific customer's Rewards balance, lock status, ticket status or deletion eligibility without checking the live database. Quote the general rule from this document and then check the live data.

## 3. Creating and Using an Account

A ShopSmart account lets a customer place orders, track them, download invoices, manage addresses, view order history, earn and redeem Rewards points and contact support.

**What is defined:** order history is kept for the last 24 months; profile addresses are editable at any time; Rewards points are earned and redeemed as described in Section 7.

**Not defined (requires clarification):** the exact fields needed to create an account, minimum age, how the account is verified (for example by email or mobile), whether guest checkout exists, how to change the registered email or mobile number, whether two-factor login exists, and whether more than one account per person is allowed. The assistant must say these are not defined and offer escalation.

**Identity.** The assistant works with the account that is signed in to the in-app chat. How identity is verified for email or other channels is **requires clarification**. The assistant never asks the customer for a password or OTP to verify identity.

## 4. Login Problems, Lockout and Password Reset

**Password reset link.** The reset link is valid for 15 minutes. After 15 minutes it expires and the customer must request a new link.

**Login lockout.** After 5 failed login attempts, the account is locked for 30 minutes. After 30 minutes the customer can try again.

**Exception (same section).** Requesting a password reset does not unlock the account earlier than 30 minutes unless the live system shows otherwise. Whether an early unlock by support is possible is **requires clarification**. The assistant must not promise it.

**Worked example 1 (lockout).** A customer fails to log in 5 times at 10:00 IST. The account is locked until 10:30 IST. If they try again at 10:20 IST, the account is still locked.

**Worked example 2 (expired reset link).** A reset link is requested at 14:00 IST and opened at 14:20 IST. The link expired at 14:15 IST (15 minutes). The customer requests a new link and opens it within 15 minutes.

**Troubleshooting steps the assistant may suggest:**

1. Check that the email or mobile number is the one used at sign-up.
2. Use "Forgot password" and open the reset link within 15 minutes.
3. If locked, wait 30 minutes before trying again.
4. If the reset link or message does not arrive, check spam or junk folders, then contact support.

**Never share secrets.** The assistant and ShopSmart staff will never ask for a password or OTP. If a customer pastes a password or OTP into chat, the assistant must not repeat it and should tell the customer not to share it and to change the password if it was exposed.

**Account takeover or suspicious logins** (for example orders the customer did not place) need human support. See Section 9.

## 5. Profile and Addresses

**Profile addresses** can be edited at any time. A change to a saved address does not change an order that has already been placed.

**Address on an existing order** can be changed only before Shipped. After the order is Shipped, an address change is best-effort by the courier and is not guaranteed. Order statuses are: Processing, Packed, Shipped, Out for Delivery, Delivered (or Cancelled).

**Worked example 3.** A customer places an order and notices a wrong flat number while the order is Packed. The address can still be changed because the order is not yet Shipped (the assistant checks the live status). If the status is Shipped, the assistant explains that the change is best-effort by the courier and cannot be guaranteed.

**Billing address.** Corrections are before Shipped only. After the invoice is generated, only minor spelling corrections are possible via support (see SS-FAQ-PAY-004).

**Not defined (requires clarification):** the maximum number of saved addresses, editing the name or phone number on a profile, adding a new mobile number, and communication preferences.

## 6. Order History

Order history shows the last 24 months. The customer can view the order, its status and its invoice (once the order is Shipped and the invoice is generated within 24 hours).

**Older orders.** Orders older than 24 months are not shown. How a customer can get information on them is **requires clarification**. The assistant must not promise it.

**Live status.** For the current status, tracking or refund status of an order, the assistant looks up the live database first. This document does not contain order data.

## 7. Rewards Points

| Topic | Rule |
|---|---|
| Earning | 1 point per ₹100 paid, excluding shipping and COD fees |
| When credited | On the 11th day after delivery |
| Redeeming | 1 point = ₹1, minimum 100 points, up to 20% of the order value |
| Expiry | 12 months after crediting |
| Reversal | Points are reversed on returned or cancelled items |

**Worked example 4 (earning).** An order is delivered on 1 Dec 2026 and ₹1,200 was paid for the item (excluding shipping and COD fees). Points earned = 1200 / 100 = 12 points, credited on the 11th day after delivery, which is 12 Dec 2026. The assistant checks the live balance to confirm.

**Worked example 5 (redeeming).** An order's value is ₹2,000. Maximum redemption = 20% of ₹2,000 = ₹400 = 400 points. A customer with 350 points can redeem up to 350 points (₹350). A customer with 80 points cannot redeem, because the minimum is 100 points.

**Worked example 6 (expiry).** Points credited on 12 Dec 2026 expire 12 months after crediting, that is, on 12 Dec 2027.

**Exceptions (same section).**

- Points are not earned on shipping fees or COD fees.
- Points earned on an item that is returned or cancelled are reversed.
- Redeemed points on a returned or cancelled item are returned as points, or as ShopSmart Credit if the points expired.
- Points are credited on the 11th day after delivery, after the longest return window (10 days) has passed.

**Not defined (requires clarification):** rounding of points when the amount paid is not a multiple of ₹100; whether redeemed points or ShopSmart Credit reduce the amount "paid" for earning; whether redeemed points count toward the ₹799 free-shipping threshold; points transfer between accounts; and what happens to points on account deletion.

The assistant never states a customer's balance, credit date or expiry date without checking the live database.

## 8. Account Security

- Never share your password, OTP, CVV, PIN or full card number with anyone, including anyone claiming to be from ShopSmart.
- ShopSmart staff and the AI assistant never ask for full card numbers, CVV, PINs, passwords or OTPs.
- Use a password that is not used on other sites, and log out on shared devices.
- Report any order, login or message you do not recognise to support@shopsmart.example or through in-app chat.
- If a customer says their account was accessed by someone else, the assistant does not make changes on its own and escalates to human support.

**Not defined (requires clarification):** how quickly a compromised account is secured, two-factor login, login alerts, and device or session management.

## 9. Contacting Support and Escalating

| Level | Contact | First response | Target resolution |
|---|---|---|---|
| AI assistant (in-app chat) | 24x7 | Instant | n/a |
| Human chat (9:00–21:00 IST, all days) | In-app | 30 minutes in support hours | n/a |
| Email | support@shopsmart.example | 24 hours | 3 business days (complex: 7) |
| Level 2 Senior Support | Escalation from a ticket | 24 hours | 5 business days |
| Level 3 Grievance Officer (fictional role) | Written complaint | Acknowledge in 48 hours | 15 calendar days |

There is no phone support. The website Help Centre is also available. Ticket ID format: SS-T- plus 6 digits (for example, SS-T-000000 is the format only, not a real ticket).

**Escalation triggers:** SLA breach, customer request, disputed evidence, or a conflict between documents and the database.

**How escalation works.**

1. The assistant tries to answer from the documents and the live database.
2. If it cannot, it offers human chat (9:00–21:00 IST, all days) or a ticket by email.
3. If the ticket's target resolution passes without a resolution, the customer can ask for Level 2 Senior Support.
4. If still unresolved, the customer can send a written complaint to the Level 3 Grievance Officer (a fictional role). Acknowledgement is within 48 hours and the target resolution is 15 calendar days.

**Worked example 7.** A customer emails support on a Monday about a complex issue. First response is due within 24 hours. The target resolution for a complex issue is 7 business days. If it is not resolved in that time, the customer asks for escalation to Level 2 Senior Support, which responds within 24 hours with a target of 5 business days.

**Ticket status.** The assistant checks ticket status in the live database. It must not guess it.

**Complaints.** A complaint is a written statement of dissatisfaction. The assistant should log or direct it as a ticket and offer escalation. The assistant must not promise a particular outcome, compensation or goodwill credit; these are **requires clarification**. The address or form for a Level 3 written complaint is also **requires clarification**; the assistant says the complaint can be raised through a ticket escalation or email to support@shopsmart.example and offers human support.

## 10. Account Deletion

**Rule.** Account deletion is processed within 30 days. It is blocked while orders or refunds are pending.

**Worked example 8.** A customer requests deletion on 1 Dec 2026 with a return refund still pending. Deletion is blocked until the refund is completed. The assistant checks the live database for pending orders or refunds. After the order is Delivered and no refund or return is pending, deletion can be processed within 30 days of the request.

**Exceptions and notes (same section).**

- "Pending orders" means any order not yet Delivered or Cancelled. Whether an open return or warranty ticket also blocks deletion is **requires clarification**.
- The assistant never deletes an account on its own authority. A deletion request is passed to human support or an authorized system.

**Not defined (requires clarification):** what happens to Rewards points and ShopSmart Credit on deletion; whether invoices and order history remain available afterwards; whether deletion can be undone; how long data is kept; and how to request a copy of personal data.

## 11. Customer Keywords and Synonyms

can't log in, login failed, account locked, too many attempts, locked out, forgot password, reset password, password reset link expired, link not working, change password, update profile, change phone number, change email, add address, edit address, wrong address, change delivery address, order history, old orders, past orders, rewards points, reward balance, points not credited, points expired, redeem points, delete my account, close my account, remove my account, contact support, talk to human, customer care number, phone support, support email, ticket status, escalate, complaint, grievance, senior support, manager, nobody replied, no response.

## 12. Frequently Asked Questions

**Q1. How do I create a ShopSmart account?**
The exact sign-up steps, required fields and verification method are not defined in this document (requires clarification). The assistant offers escalation or points to the website Help Centre.

**Q2. I cannot log in. What should I do?**
Check that you are using the email or mobile number you registered with. After 5 failed attempts the account is locked for 30 minutes, so wait 30 minutes and try again. You can also use "Forgot password". Never share your password or OTP with anyone.

**Q3. Why is my account locked?**
After 5 failed login attempts the account is locked for 30 minutes. The assistant checks the live database for lock status. After 30 minutes you can try again.

**Q4. My password reset link is not working.**
The link is valid for 15 minutes. If it expired, request a new link and open it within 15 minutes. If the link does not arrive, check spam or junk folders and contact support.

**Q5. Can support unlock my account before 30 minutes?**
An early unlock is not defined (requires clarification). The assistant must not promise it and offers escalation.

**Q6. Can the AI assistant ask me for my password or OTP to help?**
No. ShopSmart staff and the AI assistant never ask for passwords, OTPs, CVV, PINs or full card numbers.

**Q7. How do I change my saved address?**
Profile addresses can be edited at any time in your account.

**Q8. Can I change the address on an order I already placed?**
Only before the order is Shipped. After Shipped, an address change is best-effort by the courier and is not guaranteed. The assistant checks the live order status first.

**Q9. How far back can I see my orders?**
Order history shows the last 24 months.

**Q10. How do I earn Rewards points?**
You earn 1 point per ₹100 paid, excluding shipping and COD fees. Points are credited on the 11th day after delivery.

**Q11. How do I use Rewards points?**
1 point = ₹1. The minimum is 100 points, and you can redeem up to 20% of the order value.

**Q12. When do my Rewards points expire?**
12 months after crediting. The assistant checks the live database for the exact date.

**Q13. My Rewards points were not credited.**
Points are credited on the 11th day after delivery. If it has been less than 11 days, they are not yet due. If it has been longer, the assistant checks the live database and offers a ticket. Points are not earned on shipping or COD fees, and are reversed on returned or cancelled items.

**Q14. I returned an item. What happens to the points I earned or redeemed?**
Points earned on a returned or cancelled item are reversed. Redeemed points are returned as points, or as ShopSmart Credit if the points expired.

**Q15. How can I contact ShopSmart support?**
Through the in-app AI assistant (24x7), human chat in the app (9:00–21:00 IST, all days), email at support@shopsmart.example, or the website Help Centre. There is no phone support.

**Q16. How fast will support reply?**
Human chat: first response within 30 minutes during support hours. Email: first response within 24 hours, with target resolution of 3 business days (complex: 7 business days).

**Q17. My issue was not resolved. How do I escalate?**
Ask for Level 2 Senior Support from your ticket (first response in 24 hours, target resolution 5 business days). If it is still unresolved, send a written complaint to the Level 3 Grievance Officer (a fictional role). They acknowledge in 48 hours and aim to resolve in 15 calendar days.

**Q18. What is my ticket ID format and how do I check my ticket?**
Ticket IDs look like SS-T- followed by 6 digits. The assistant checks ticket status in the live database.

**Q19. How do I delete my account?**
Deletion is processed within 30 days of the request. It is blocked while orders or refunds are pending. The assistant passes the request to human support and does not delete the account itself.

**Q20. Will I get compensation for the trouble?**
Compensation and goodwill credits are not defined (requires clarification). The assistant must not promise them and offers escalation.

## 13. Not Defined: Requires Clarification

The assistant must say these are not defined and offer escalation. It must not invent a rule.

Account creation details (fields, minimum age, verification method); guest checkout; multiple accounts; changing the registered email or mobile; two-factor login, login alerts and device management; early lockout release; maximum saved addresses and editing profile name or phone; communication preferences; access to orders older than 24 months; Rewards rounding, Rewards and Credit effect on "amount paid" and on the ₹799 threshold, points transfer, points on deletion; ShopSmart Credit and invoices on deletion, undoing deletion, data retention and data copy requests; whether open returns or warranty tickets block deletion; the Level 3 complaint address or form; identity verification on email; compensation or goodwill credits; and all items listed as not defined in the Master Policy Framework (EMI and no-cost EMI, gift cards, international shipping and payments, price-match, GST invoices with GSTIN changes, installation services for large appliances, pickup for oversized items, Sunday delivery).

## 14. Cross-References

- SS-FAQ-PAY-004: payments, refunds, invoices and billing address.
- SS-POL-RET-001: returns and refund stages (Rewards reversal).
- SS-POL-CAN-003: cancellations and COD refusals (3 COD refusals in 12 months disables COD).
- SS-POL-SHP-002: shipping, address change before Shipped.
- SS-POL-DMG-008: damaged, missing or incorrect items.
- SS-POL-WAR-005: warranty and product support tickets.
- SS-CAT-PRD-006: catalogue (live price overrides catalogue price).

**Conflict precedence:** If this document and the live database conflict, trust the database and flag it.

## 15. Limitations and Cases Needing Human Support

This document cannot say whether a specific account is locked, what a customer's balance is or what a ticket's status is. The assistant looks up live data. The assistant cannot unlock accounts early, delete accounts, grant compensation, change registered contact details or approve refunds. Human support is needed for: suspected account takeover; password reset messages that never arrive; Rewards discrepancies after a live check; account deletion requests; complaints and Level 2 or Level 3 escalations; SLA breaches; and anything marked requires clarification. If the retrieved documents do not contain the answer, the assistant says so and offers escalation.

## 16. Security Note

ShopSmart staff and the AI assistant never ask for full card numbers, CVV, PINs, passwords or OTPs. Do not share them in chat, email or with anyone claiming to be from ShopSmart. This document contains no real personal data, order IDs, addresses or payment details.

## 17. Note on Interpretations and Clarifications

**Interpretations made in this document:**
- "11th day after delivery" is counted from the Delivered date, so an order delivered on 1 Dec is credited on 12 Dec.
- "12 months after crediting" means the same calendar date one year later.
- "Pending orders" for deletion means any order not yet Delivered or Cancelled; a pending refund is one not yet Refund Completed.
- The reset link is sent to the account's registered contact details.
- The assistant never deletes accounts or unlocks them early; it passes such requests to human support.
- A Level 3 written complaint can be started through ticket escalation or email to support@shopsmart.example.

**Newly marked requires clarification:** account creation details; guest checkout; multiple accounts; changing registered email or mobile; two-factor login and device management; early unlock; maximum saved addresses and profile name or phone editing; communication preferences; orders older than 24 months; Rewards rounding and "amount paid" definition; points on deletion; effects of deletion on Credit, invoices and data; whether open returns or warranty tickets block deletion; Level 3 complaint address; identity verification on email.
