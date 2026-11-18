# ShopSmart Payment and Billing FAQ

> **Fictional notice:** ShopSmart is a fictional company and these policies are fictional. This document was created for a software demonstration (a college RAG and AI-agent project). It is not real company policy, not financial advice and not legal advice.

| Field | Value |
|---|---|
| Company | ShopSmart (fictional online multi-category marketplace, India) |
| Document ID | SS-FAQ-PAY-004 |
| Version | 1.0 |
| Effective date | 1 Nov 2026 |
| Last updated | 28 Oct 2026 |
| Category tag | payments_billing |
| Currency and time zone | INR (₹); IST |
| Related documents | SS-POL-RET-001 (Return and Refund), SS-POL-SHP-002 (Shipping and Delivery), SS-POL-CAN-003 (Order Cancellation), SS-POL-DMG-008 (Damaged, Missing and Incorrect Items), SS-FAQ-ACC-007 (Account and Customer Support), SS-POL-WAR-005 (Warranty), SS-CAT-PRD-006 (Product Catalog) |

**Suggested RAG metadata:** doc_id: SS-FAQ-PAY-004 | category: payments_billing | version: 1.0 | effective_date: 2026-11-01 | doc_type: faq | region: IN | live_data_needed: true (for payment, transaction, refund and invoice status)

## 1. Scope and Purpose

This document answers common questions about paying for ShopSmart orders and about billing. It covers the accepted payment methods (UPI, debit card, credit card, net banking and Cash on Delivery), failed payments, money debited without an order, duplicate charges, payment reconciliation, refund methods and timelines, invoices, billing-address corrections and payment security.

It does not decide whether an order or item qualifies for a refund. Eligibility is set by SS-POL-RET-001 (returns), SS-POL-CAN-003 (cancellations) and SS-POL-DMG-008 (damaged, missing or incorrect items). This document explains how and when money moves once a refund is approved.

Everything here describes fictional ShopSmart rules. The AI assistant must use only these rules and the live database. It must never invent a rule that is not written here.

## 2. Static vs Live Information

| Type | What belongs here | Source |
|---|---|---|
| Static (this document) | Accepted payment methods, COD rules and fee, fee schedule, refund method timelines, reconciliation timelines, invoice rules, billing-address rules, security rules, FAQs | Retrieved documents |
| Live (database or tools) | Whether a payment succeeded, failed or is pending; whether an order was created; transaction status; refund status and stage; whether a refund has been initiated or completed; invoice availability; COD eligibility for an order or pincode; Rewards balance; live prices and discounts | MongoDB tools |

**Rule for the AI assistant:** Do not tell a customer that a specific payment was received, reversed or refunded, or that a specific refund will arrive on a specific date, without checking the live database. Quote the general timeline from this document and then check the live status.

## 3. Accepted Payment Methods

| Method | Notes |
|---|---|
| UPI | Paid online at checkout. Also accepted in cash-equivalent form at the door for COD orders (see Section 5). |
| Debit card | Paid online at checkout. |
| Credit card | Paid online at checkout. |
| Net banking | Paid online at checkout. |
| Cash on Delivery (COD) | Pay cash or UPI at the door. Order value ₹199 to ₹10,000, ₹30 COD fee. Subject to eligibility (Section 5). |

ShopSmart does not offer any other payment method in this fictional framework. EMI, no-cost EMI, gift cards, international payments and international cards are **requires clarification** (see Section 14). The assistant must not say they are supported or unsupported.

**Paying with Rewards points:** Rewards points can be redeemed at 1 point = ₹1, with a minimum of 100 points, up to 20% of the order value. The remaining amount is paid by one of the methods above. Example: on a ₹2,000 order, the most that can be redeemed is ₹400 (400 points), and the remaining ₹1,600 is paid by UPI, card, net banking or COD (subject to COD rules).

## 4. Paying Online: UPI, Cards and Net Banking

**Payment is confirmed when the order is confirmed.** An online payment is only complete when the customer sees an order confirmation. The live database shows the true payment and order status.

**Failed payment.** If a payment fails, any amount debited is automatically reversed. The customer can retry with the same method or with another method. If money was debited and no order was created, follow Section 7.

**Checking an online payment.** The assistant should look up the customer's payment and order status first. It should not ask the customer for card details to do this.

**Pending payment.** If the database shows a payment as pending, the assistant explains that the amount is under reconciliation. Debited-but-no-order cases are reconciled within 24 hours (Section 7). The assistant must not predict the final result.

**Choosing a method.** Refund timelines differ by method (Section 8). UPI refunds usually complete faster than card refunds. This is general information only; the assistant must not recommend a method on the basis of a promised refund date.

**Not defined (requires clarification):** per-transaction payment limits, supported UPI apps, supported banks for net banking, supported card types and networks, saved cards, and the length of the payment page timeout.

## 5. Cash on Delivery (COD)

**Rules (each one stands alone):**

- **Order value:** COD is available for order values from ₹199 to ₹10,000.
- **COD fee:** ₹30 per order.
- **How to pay at the door:** Cash or UPI.
- **When COD is unavailable:** For certain pincodes, for restricted categories (flagged in the database), and for accounts with 3 or more COD refusals in the last 12 months.
- **Checking eligibility:** COD eligibility for a specific pincode, product or account must be checked in the live database. The assistant must not guess.

**COD and refunds.**

- COD orders: nothing is paid online, so if a COD order is cancelled before delivery or refused at the door, no refund applies because nothing was paid.
- If a COD order is delivered and the item is then returned and approved for a refund, the refund goes to a verified UPI ID or bank account. Completion: COD orders (to a verified UPI ID or bank account): 3–5 business days after valid payout details are verified.
- The assistant must never ask the customer to type a full bank account number, card number, CVV, PIN, password or OTP into chat. How payout details are collected is **requires clarification**; the assistant should say the details are collected through the secure refund flow and offer escalation if the customer cannot find it.

**COD refusals.** Refusing a COD parcel at the door counts toward the limit: 3 COD refusals in 12 months disables COD for the account. Whether a failed-COD RTO (caused by failed delivery attempts) counts as a refusal is **requires clarification**.

**COD fee.** The ₹30 COD fee is non-refundable on change-of-mind returns. It is refunded on ShopSmart-error returns (defective, damaged or wrong item) that are approved. If a COD order is cancelled before it ships, nothing was paid, so no fee is collected.

**COD combined with Express delivery** is **requires clarification**.

## 6. What the Customer Pays: Fees and Price Rules

| Charge | Rule |
|---|---|
| Standard delivery | ₹49, free on orders of ₹799 or more after discounts and excluding fees |
| Express delivery | ₹99 flat, never waived. It is the whole shipping charge on an Express order (the ₹49 is not added) |
| Remote surcharge | ₹40, added to Standard delivery and not waived by the ₹799 threshold |
| COD fee | ₹30 |

**Worked example 1 (free Standard shipping, COD):** Item price after discounts ₹1,000, Standard delivery to a non-remote pincode, paying by COD. Shipping is free (₹1,000 is at least ₹799). Total payable at the door = ₹1,000 + ₹30 COD fee = ₹1,030.

**Worked example 2 (remote surcharge):** Item price after discounts ₹900, Standard delivery to a remote pincode, prepaid. Shipping is free but the ₹40 remote surcharge still applies. Total = ₹940.

**Worked example 3 (below threshold):** Item price after discounts ₹500, Standard delivery, non-remote, prepaid. Shipping ₹49. Total = ₹549.

**Which price is charged.** The live database price always overrides the catalogue price. The price charged at checkout and shown on the invoice is binding for that order. If the product page price later changes, the paid order is not affected.

**Whether redeemed Rewards points or ShopSmart Credit count toward the ₹799 free-shipping threshold** is **requires clarification**. Fees on split parcels are also **requires clarification**.

## 7. Payment Problems: Debited Without Order, Duplicate Charge, Failed Payment

| Situation | Rule |
|---|---|
| Debited but no order confirmation | Reconciled within 24 hours. If no order is created, auto-reversal within 5–7 business days. If not reversed after 7 business days, contact support with the transaction reference. |
| Duplicate charge | Reconciled within 3 business days. The extra amount is refunded within 5–7 business days. |
| Failed payment | Any amount debited is auto-reversed. Retry with the same or another method. |

**Debited but no order (exception in the same section).** If the order appears within 24 hours, the payment is treated as successful and nothing is reversed. If the customer places a new order meanwhile, that is a separate order. Do not tell the customer the original payment will be refunded until the database shows no order was created.

**Duplicate charge (exception).** A duplicate charge means the same order was charged more than once. If two separate orders were placed, there is no duplicate charge. The assistant checks the live database for the number of orders and payments before answering.

**Failed payment (exception).** The framework gives no separate reversal timeline for a failed payment. If money was debited and no order exists, the debited-without-order timeline above applies. A different timeline specifically for failed payments is **requires clarification**.

**What support needs.** The order ID (if any), the date and time of the payment, the payment method, the amount, and the transaction reference (UPI transaction reference, card authorisation reference or net-banking reference). The customer should never share a full card number, CVV, PIN, password or OTP.

**Worked example 4 (debited, no order).** A customer pays ₹1,299 by UPI on Monday and sees no order confirmation. The assistant checks the database. If the order is not found, it explains the 24-hour reconciliation. If no order is created, the amount is auto-reversed within 5–7 business days. If the amount has not come back after 7 business days, the customer contacts support with the transaction reference.

## 8. Refund Methods and Timelines

**Default method:** the original payment method, or ShopSmart Credit if the customer chooses it.

**Refund initiation:** within 2 business days after inspection passes for returns. Within 1 business day after a pre-shipment cancellation or a ShopSmart-initiated cancellation. RTO refund (prepaid): initiated within 2 business days of the item being received back and verified.

**Completion after the refund is initiated:**

| Method | Completion timeline |
|---|---|
| UPI | 1–3 business days after the refund is initiated |
| Net banking | 3–5 business days after the refund is initiated |
| Debit or credit card | 5–7 business days after the refund is initiated |
| COD orders (to a verified UPI ID or bank account) | 3–5 business days after valid payout details are verified |
| ShopSmart Credit | Instant |

Business days are Monday to Saturday, excluding national public holidays. Sundays are not business days.

**Refund not received.** If the refund is not credited by the maximum timeline for the method plus 2 business days, raise a ticket with the UTR or ARN if available. Example: for a card refund, the maximum is 7 business days after initiation, so the customer raises a ticket after 9 business days.

**Redeemed Rewards points.** Redeemed points are returned as points, or as ShopSmart Credit if the points expired.

**The assistant's duty.** Always check the live refund status (stage and initiated date) before quoting dates. Never promise that a refund has been or will be approved.

## 9. Refund Amount and Non-Refundable Fees

**Refund amount:** the item price paid, adjusted by any partial deduction (10% minor, 25% moderate; severe issue means return rejected).

| Return type | Shipping fee | COD fee | ₹60 reverse-pickup fee |
|---|---|---|---|
| Change of mind | Not refunded | Not refunded | Deducted from the refund |
| ShopSmart error (defective, damaged, wrong) | Refunded | Refunded | Not charged |

**Worked example 5 (change of mind, prepaid by UPI).** Item ₹1,299, free Standard shipping. Return approved after inspection. Refund = ₹1,299 − ₹60 = ₹1,239 to the original UPI account. Initiated within 2 business days after inspection passes. UPI: 1–3 business days after the refund is initiated.

**Worked example 6 (defective item, COD).** Item ₹499, Standard shipping ₹49, COD fee ₹30. Total paid at the door ₹578. Return approved as defective. Refund = ₹499 + ₹49 + ₹30 = ₹578 to the verified UPI ID or bank account. COD orders (to a verified UPI ID or bank account): 3–5 business days after valid payout details are verified.

**Worked example 7 (pre-shipment cancellation, card).** An order of ₹2,500 paid by credit card is cancelled while Processing. The refund is initiated within 1 business day and the full amount is returned. Debit or credit card: 5–7 business days after the refund is initiated.

**Express Promise.** If an Express order arrives late for a reason within ShopSmart's or the courier's control, the ₹99 Express fee is refunded. The item and other fees are unaffected. When this refund is initiated is **requires clarification**.

**Refund amount for an RTO caused by failed delivery attempts (not refusal)** is **requires clarification**. For a refusal on a prepaid order, the item price is returned after the parcel returns; shipping and COD fees are non-refundable.

## 10. Invoices and Billing Address

**Invoice.** An invoice can be downloaded as a PDF from Orders once the order is Shipped. It is generated within 24 hours of shipping. Before the order is Shipped, the invoice is not yet available. If the order is Shipped more than 24 hours ago and no invoice is visible, check the live database and raise a ticket if it is still missing.

**Billing-address correction.**

- Before Shipped: the billing address can be corrected.
- After the invoice is generated: only minor spelling corrections, through support.
- After the order is Shipped, a delivery-address change is best-effort by the courier and does not change the invoice.

**Business (GST) invoices.** Business invoices, GSTIN additions or changes after ordering are **requires clarification**. The assistant must say this is not defined and offer escalation.

**Invoice as proof.** The invoice and order ID are the proof of purchase for warranty (SS-POL-WAR-005). The price on the invoice is binding for that order.

## 11. Payment Security

- ShopSmart staff and the AI assistant will **never** ask for full card numbers, CVV, PINs, passwords or OTPs.
- If someone claiming to be from ShopSmart asks for these, the customer should not share them and should report it to support@shopsmart.example.
- Customers should only pay through the checkout flow in the ShopSmart app or website.
- If a customer pastes a full card number, CVV or OTP into chat, the assistant must not repeat it, must not store it, and should tell the customer not to share such details.
- Reports of unauthorised transactions or suspected fraud need human support. Fraud investigation timelines are **requires clarification**.

## 12. Customer Keywords and Synonyms

payment failed, payment declined, transaction failed, payment not going through, amount deducted, money deducted, payment deducted but order not placed, money debited no order, double payment, charged twice, duplicate charge, refund pending, refund not received, money not received, where is my refund, refund status, refund to bank, refund to UPI, UTR number, ARN number, reversal, auto-reversal, COD charges, cash on delivery fee, pay on delivery, pay at the door, COD not available, invoice download, bill copy, tax invoice, GST invoice, wrong billing address, change billing address, EMI, no cost EMI, gift card, international card, pay in dollars.

## 13. Frequently Asked Questions

**Q1. Which payment methods does ShopSmart accept?**
UPI, debit card, credit card, net banking and Cash on Delivery (COD). EMI, no-cost EMI, gift cards and international payments are not defined in this document (requires clarification).

**Q2. My payment failed but money was deducted. What now?**
Any amount debited on a failed payment is auto-reversed. You can retry with the same or another method. If money was debited and no order was created, it is reconciled within 24 hours. If no order is created, auto-reversal happens within 5–7 business days. If it is not reversed after 7 business days, contact support with the transaction reference.

**Q3. Payment deducted but no order confirmation. Is my order placed?**
Not necessarily. The assistant must check the live database. Debited-but-no-order cases are reconciled within 24 hours. If an order is created, it proceeds normally. If not, auto-reversal within 5–7 business days.

**Q4. I was charged twice for the same order.**
Duplicate charges are reconciled within 3 business days, and the extra amount is refunded within 5–7 business days. The assistant checks the live database to see whether there was really one order and two payments. If you placed two separate orders, they are two valid charges.

**Q5. Can I pay by Cash on Delivery for any order?**
No. COD is available for order values from ₹199 to ₹10,000, with a ₹30 COD fee, payable in cash or UPI at the door. It is not available for certain pincodes, restricted categories (flagged in the database), or accounts with 3 or more COD refusals in 12 months.

**Q6. Why is COD not showing for my order?**
It may be because the order value is outside ₹199 to ₹10,000, the pincode is not eligible, an item is in a restricted category, or the account has 3 or more COD refusals in 12 months. The assistant checks the live database before explaining which one applies.

**Q7. How long does a refund take?**
First the refund is initiated: within 2 business days after inspection passes for returns, or within 1 business day after a pre-shipment or ShopSmart-initiated cancellation. Then it completes: UPI: 1–3 business days after the refund is initiated. Net banking: 3–5 business days after the refund is initiated. Debit or credit card: 5–7 business days after the refund is initiated. COD orders (to a verified UPI ID or bank account): 3–5 business days after valid payout details are verified. ShopSmart Credit: instant.

**Q8. My refund has not arrived. What should I do?**
Check the refund status in the app first. If the refund is not credited by the maximum timeline for your method plus 2 business days, raise a ticket with the UTR or ARN if available. The assistant checks the live refund stage before answering.

**Q9. Where will my refund go?**
To the original payment method by default, or to ShopSmart Credit if you choose it. For COD orders it goes to a verified UPI ID or bank account.

**Q10. Is the ₹60 pickup fee or the shipping fee refunded?**
For change-of-mind returns, the shipping fee, COD fee and ₹60 reverse-pickup fee are non-refundable (the ₹60 is deducted from the refund). For ShopSmart-error returns (defective, damaged, wrong), the shipping fee and COD fee are refunded.

**Q11. How do I download my invoice?**
Open Orders and download the invoice as a PDF once the order is Shipped. It is generated within 24 hours of shipping.

**Q12. Can I change my billing address after ordering?**
Before the order is Shipped, yes. After the invoice is generated, only minor spelling corrections are possible, through support.

**Q13. Can I get a GST invoice or add a GSTIN?**
Business (GST) invoices and GSTIN changes are not defined in this document (requires clarification). The assistant offers escalation.

**Q14. Do you offer EMI or no-cost EMI?**
EMI and no-cost EMI are not defined in this document (requires clarification). The assistant must not say they are available.

**Q15. Can I pay with a gift card or an international card?**
Gift cards, international payments and international cards are not defined (requires clarification).

**Q16. The price at checkout is different from what I saw in the catalogue. Which one applies?**
The live database price always overrides the catalogue price. The price charged at checkout and shown on the invoice is binding for that order.

**Q17. Can I use Rewards points to pay?**
Yes. 1 point = ₹1, minimum 100 points, up to 20% of the order value. Points redeemed on a returned or cancelled item are returned as points, or as ShopSmart Credit if the points expired.

**Q18. Someone asked for my OTP or card number saying they are from ShopSmart.**
Do not share it. ShopSmart staff and the AI assistant never ask for full card numbers, CVV, PINs, passwords or OTPs. Report it to support@shopsmart.example.

**Q19. Can the AI tell me exactly when my refund will arrive?**
No. It can give the general timeline for your method and check the live status. It cannot promise an exact date or approve a refund.

## 14. Not Defined: Requires Clarification

The assistant must say these are not defined and offer escalation. It must not invent a rule.

EMI and no-cost EMI; gift cards; international shipping and international payments; price-match; business (GST) invoices with GSTIN changes; compensation or goodwill credits; payment limits and supported apps, banks and card networks; saved cards; payment timeout length; a specific reversal timeline for failed payments; how COD payout details are collected; whether redeemed Rewards points or Credit count toward the ₹799 threshold; fees on split parcels; COD combined with Express; when the Express Promise refund is initiated; refund amount for an RTO caused by failed attempts; whether a failed-COD RTO counts as a refusal; fraud investigation timelines.

## 15. Support and Escalation

| Level | Contact | First response | Target resolution |
|---|---|---|---|
| AI assistant (in-app chat) | 24x7 | Instant | n/a |
| Human chat (9:00–21:00 IST, all days) | In-app | 30 minutes in support hours | n/a |
| Email | support@shopsmart.example | 24 hours | 3 business days (complex: 7) |
| Level 2 Senior Support | Escalation from a ticket | 24 hours | 5 business days |
| Level 3 Grievance Officer (fictional role) | Written complaint | Acknowledge in 48 hours | 15 calendar days |

There is no phone support. Ticket ID format: SS-T- plus 6 digits.

**Escalation triggers:** SLA breach, customer request, disputed evidence, or a conflict between documents and the database. Refund not received after the maximum timeline plus 2 business days, and debited money not reversed after 7 business days, should be ticketed.

## 16. Cross-References

- SS-POL-RET-001: return eligibility, return stages, partial refunds, ₹60 pickup fee.
- SS-POL-CAN-003: cancellations, refusal at the door, COD refusals.
- SS-POL-SHP-002: shipping fees, Express Promise, RTO.
- SS-POL-DMG-008: damaged, missing or incorrect items (48 hours).
- SS-FAQ-ACC-007: Rewards points, account and support contact.
- SS-POL-WAR-005: invoice as proof of purchase for warranty.
- SS-CAT-PRD-006: catalogue prices, always overridden by live prices.

**Conflict precedence:** Payment and refund-method timelines are defined once (Section 8) and repeated verbatim wherever used. If this document and the live database conflict, trust the database and flag it.

## 17. Limitations and Cases Needing Human Support

This document cannot tell the assistant whether a specific payment, refund or invoice exists. The assistant must look up live data. The assistant cannot approve refunds, reverse payments or change payment methods. Human support is needed for: unauthorised or suspected fraudulent transactions; a debit not reversed after 7 business days; a refund not credited after the maximum timeline plus 2 business days; a duplicate charge not refunded within 5–7 business days; missing invoices; GST or business invoice requests; and anything marked requires clarification. If the retrieved documents do not contain the answer, the assistant says so and offers escalation.

## 18. Security Note

ShopSmart staff and the AI assistant never ask for full card numbers, CVV, PINs, passwords or OTPs. Do not share them in chat, email or with anyone claiming to be from ShopSmart. This document contains no real personal data, order IDs, addresses or payment details.

## 19. Note on Interpretations and Clarifications

**Interpretations made in this document:**
- The ₹99 Express fee is the whole shipping charge on an Express order.
- ShopSmart-error fee refunds (shipping and COD) apply to approved damaged, missing and wrong-item claims.
- A failed payment with money debited and no order created is handled under the debited-but-no-order timeline, because no separate timeline is defined.
- The assistant does not collect bank account numbers in chat; payout details go through a secure refund flow.
- Refund-not-received example: ticket after maximum timeline plus 2 business days (card: 9 business days).

**Newly marked requires clarification:** payment limits and supported apps, banks and card networks; saved cards; payment timeout; failed-payment reversal timeline; how COD payout details are collected; fraud investigation timelines. Previously flagged items repeated here: EMI, gift cards, international payments, GST invoices, Rewards or Credit and the ₹799 threshold, split-parcel fees, COD with Express, Express Promise refund timing, RTO refund for failed attempts, failed-COD RTO as refusal.
