# ShopSmart Shipping and Delivery Policy

> **FICTIONAL NOTICE:** ShopSmart is a fictional company created for a college software demonstration (LLM + RAG + agentic tool calling). Every policy, fee, timeline and example in this document is invented. This is not a real company policy and is not legal advice.

## Document Information

| Field | Value |
|---|---|
| Document title | Shipping and Delivery Policy |
| Company | ShopSmart (fictional online multi-category marketplace, India) |
| Document ID | SS-POL-SHP-002 |
| Version | v1.0 |
| Effective date | 1 November 2026 |
| Last updated | 28 October 2026 |
| Category tag | shipping_delivery |
| Currency / time zone | INR (₹) / IST |
| Related documents | SS-POL-CAN-003, SS-POL-RET-001, SS-POL-DMG-008, SS-FAQ-PAY-004, SS-FAQ-ACC-007 |

**Suggested RAG metadata:** doc_id=SS-POL-SHP-002; category=shipping_delivery; version=1.0; effective_date=2026-11-01; doc_type=policy; region=India; live_data_needed=order status, tracking, delivery ETA, pincode serviceability.

## 1. Scope and Purpose

This policy explains how ShopSmart delivers orders within India: delivery options, estimated timelines, shipping charges, tracking, delays, address problems, failed deliveries and delivery exceptions. It applies to all six product categories: Electronics, Home Appliances, Fashion, Footwear, Accessories and Home Essentials.

It does not decide cancellations (see SS-POL-CAN-003), returns (SS-POL-RET-001), or damaged, missing and wrong items (SS-POL-DMG-008). Where a delivery problem becomes one of those cases, this document points to the right policy.

## 2. Static Policy vs Live Order Information

This document contains **static policy**: rules, fees, timelines. It cannot tell anyone where a specific parcel is.

| Defined in this document (static) | Must come from the live database or tools |
|---|---|
| Delivery timelines by region, fees, thresholds, attempt limits, delay rules | Order status, tracking events, courier details |
| Definition of estimate vs Express Promise | The estimated or promised date for a specific order |
| Rules for COD and remote locations | Whether a pincode is metro, non-metro, remote, COD-eligible or has Express |
| Delay and lost-parcel ladder | How many delivery attempts have already been made |

If a retrieved policy and the live order record disagree, the live record is trusted and the difference is flagged for support.

## 3. Key Terms

- **Business day:** Monday to Saturday, excluding national public holidays. Sundays are not business days.
- **Order confirmation:** the point at which the order is confirmed in the system. Delivery estimates are counted in business days from this point.
- **Delivered timestamp:** the date and time the system marks the order or item Delivered. This starts the return window, the 48-hour reporting period for damaged, missing or wrong items, and the warranty period.
- **RTO (Return to Origin):** a parcel returned to the ShopSmart warehouse because it was refused or could not be delivered.
- **Remote location:** a pincode classified as remote by ShopSmart. Classification is checked at checkout.

## 4. Delivery Options and Estimated Timelines

Order processing for in-stock items takes up to 1 business day (up to 2 business days for large appliances). Processing happens within the delivery estimate below, which is counted from order confirmation.

| Location type | Standard delivery | Express delivery |
|---|---|---|
| Metro | 2–4 business days | 1–2 business days |
| Non-metro | 4–7 business days | 2–4 business days |
| Remote location | 7–10 business days | Not available |

The date range shown at checkout and on the order page is the authoritative estimate for that order. Standard and Express are selected at checkout. Express is never available for remote locations.

**Example:** A Standard order to a metro pincode confirmed on Monday 2 November 2026 has an estimate of 2–4 business days, so the latest estimated date is Friday 6 November 2026 (assuming no public holiday).

## 5. Estimated Delivery Date vs Guaranteed Delivery Date

**Estimated delivery date.** Every delivery date ShopSmart shows is an estimate. It is a good-faith forecast, not a promise. Courier delays, weather, local restrictions and address problems can move it. Support must not describe any Standard delivery date as guaranteed.

**Guaranteed element: the Express Promise.** ShopSmart's only delivery guarantee: if an Express order arrives after its promised date for a reason within ShopSmart's or the courier's control, the ₹99 Express fee is refunded.

- The item price and other fees are not affected. Only the ₹99 Express fee is refunded.
- Delays caused by the customer (for example, an incorrect address, or the customer being unavailable for delivery) are not within ShopSmart's or the courier's control and do not trigger the promise.
- Whether an unusual cause (such as severe weather or a local strike) counts as within control is a judgement for human support. The AI assistant must not decide it.
- The AI assistant must not confirm an Express Promise refund until the live order record and support review confirm it.
- Refund completion timelines are in Section 15. A separate initiation deadline for Express Promise refunds is **not defined in v1.0 (requires clarification)**.

## 6. Shipping Charges and Free-Shipping Eligibility

| Charge | Amount | Rule |
|---|---|---|
| Standard shipping fee | ₹49 | Free on orders of ₹799 or more |
| Express shipping fee | ₹99 flat | Never waived, including on orders above ₹799 |
| Remote-location surcharge | ₹40 | Added to Standard shipping. Not waived by the free-shipping threshold |
| COD handling fee | ₹30 | Only on Cash on Delivery orders |

**How the ₹799 threshold works:** the order value counted is the amount after discounts and excluding fees (shipping, surcharge, COD fee). Whether redeemed Rewards points or ShopSmart Credit reduce the counted value is **not defined in v1.0 (requires clarification)**; the total shown at checkout is binding.

**Express fee:** ₹99 is the flat shipping charge for an Express order. The ₹49 Standard fee is not added on top. How fees apply when one order is split into several parcels is not defined in v1.0 (requires clarification); the checkout and invoice amounts are binding.

**Worked examples**

1. Cart of ₹650 after discounts, Standard, metro, prepaid: shipping ₹49. Total shipping charge: ₹49.
2. Cart of ₹850 after discounts, Standard, metro, prepaid: shipping free. Total shipping charge: ₹0.
3. Cart of ₹1,000 after discounts, Standard, remote location, prepaid: Standard fee waived, surcharge stays. Total shipping charge: ₹40.
4. Cart of ₹500 after discounts, Standard, remote location, COD: ₹49 + ₹40 + ₹30 COD fee = ₹119 in fees.
5. Cart of ₹2,000 after discounts, Express, metro, prepaid: ₹99.

The price and fees charged at checkout and shown on the invoice are binding for that order.

## 7. Cash on Delivery (COD) Deliveries

- COD order value must be between ₹199 and ₹10,000.
- A ₹30 COD handling fee applies.
- The customer can pay at the door in cash or by UPI.
- COD is unavailable for certain pincodes, restricted categories (flagged in the database), and accounts with 3 or more COD refusals in the last 12 months.
- If COD is not offered at checkout, the live system has determined the order does not qualify. Support can confirm the reason from the database but cannot override it.
- Whether COD can be combined with Express delivery is not defined in v1.0 (requires clarification); checkout shows the available options.

## 8. Order Tracking

- Tracking becomes available once the order status is **Shipped**. Before that, only the status (Processing or Packed) is shown.
- The status sequence is: Processing, Packed, Shipped, Out for Delivery, Delivered. An order can also be Cancelled.
- Tracking details are in the Orders section of the website and app. They are live data, so the AI assistant must look them up through the order tool and never guess a location or date.
- **Customers who say "tracking not updating" or "order stuck":** this triggers the delay ladder in Section 9, not an immediate guarantee of loss.

## 9. Delayed Shipments

Counts below are business days relative to the **estimated delivery date** of the order.

| Stage | Trigger | What happens |
|---|---|---|
| 1. Contact allowed | 3 business days past the estimated date | Customer may contact support about the delay |
| 2. Investigation | Tracking shows no movement for 5 business days | An investigation with the courier is opened |
| 3. Declared lost | 10 business days past the estimated date | Customer may choose a refund or a reshipment (reshipment is subject to stock and authorization) |

**Example:** Standard metro order, estimated date Friday 6 November 2026. Stage 1 begins Tuesday 10 November. Stage 3 is reached on Wednesday 18 November (assuming no public holidays).

Rules for the AI assistant:

- Check the live order and tracking before answering.
- Do not promise a new delivery date, a refund or a reshipment before the stage is reached and authorization is confirmed.
- If the order is not yet 3 business days late, explain that the date is an estimate and offer to check tracking again later.
- If tracking says Delivered but the customer did not receive it, see Section 14 and SS-POL-DMG-008.
- Compensation or goodwill credits for delays are **not defined in v1.0 (requires clarification)** and must not be offered. The only delay-related money-back rule is the Express Promise.

## 10. Incorrect or Incomplete Addresses and Address Changes

**Changing the delivery address on an existing order:** allowed before the order is Shipped only. This means during Processing or Packed. The customer should do it from the Orders page if the option is shown, or contact support with the order ID. Support checks the live status first.

**After the order is Shipped:** correction is not guaranteed. It is handled by the courier on a best-effort basis. ShopSmart cannot promise it will succeed.

**Customer responsibility:** provide a complete address with the correct pincode and a reachable mobile number. Delivery to an incorrect address can lead to failed attempts and eventual RTO (Section 11).

**Profile addresses** can be edited at any time, but this does not change an order already placed. Billing-address rules are in SS-FAQ-PAY-004.

## 11. Failed Delivery Attempts and Return to Origin (RTO)

- The courier makes **3 delivery attempts**. Each attempt is recorded in tracking.
- After the third failed attempt, the parcel goes back to the warehouse (RTO).
- **Customer refuses delivery at the door:** also handled as RTO. For prepaid orders the item price is refunded after the parcel is received back at the warehouse. The shipping fee and COD fee are non-refundable. See SS-POL-CAN-003.
- **Prepaid RTO refund timing:** a refund is initiated within 2 business days of the item being received back and verified. Completion follows the timelines in Section 15.
- **COD RTO:** nothing was paid, so no refund applies.
- **Repeated refusals:** after 3 COD refusals in 12 months, COD is disabled for the account.
- The refund amount for an RTO caused by failed attempts (not by a refusal), including whether the shipping fee is returned, is not defined in v1.0 (requires clarification). Support must not promise a fee refund in that case.
- Whether an RTO from failed COD attempts counts toward the 3-refusal rule is not defined in v1.0 (requires clarification).
- A customer cannot cancel an order that is Shipped or Out for Delivery. See SS-POL-CAN-003.

## 12. Remote Locations

- Standard delivery takes 7–10 business days.
- Express is not available.
- A ₹40 remote-location surcharge is added to Standard shipping and is not waived by the ₹799 free-shipping threshold.
- Whether a pincode is remote is determined at checkout from the live pincode list. The static list is not published in this document.
- If no reverse-pickup service exists for a pincode, returns follow the courier-shipping rule in SS-POL-RET-001 (reimbursement up to ₹100 with a receipt).

## 13. Delivery Exceptions and Services Not Defined

ShopSmart has **not defined** the following in v1.0. Support must say it cannot confirm them and offer escalation if the customer insists:

- International shipping
- Sunday delivery (Sundays are not business days)
- Installation services for large appliances
- Pickup or return service for oversized items
- Price-match or compensation for delays
- Delivery to a different address after Shipped (best-effort only, see Section 10)

Other exceptions: delivery estimates can change because of public holidays, courier disruption and local restrictions. The order page is updated when the estimate changes.

## 14. Marked Delivered, Not Received, or Damaged on Arrival

When the order status is **Delivered**, three clocks start from the Delivered timestamp:

1. **48 hours** to report a damaged, missing, wrong or incomplete item, or an order marked delivered but not received.
2. The **return window** (10 days for Fashion and Footwear; 7 days for Electronics, Home Appliances, Accessories and Home Essentials).
3. The **seller warranty** period.

If a customer says they did not receive an order marked Delivered, they should report it within 48 hours. The investigation takes up to 5 business days. Details, evidence rules and outcomes are in SS-POL-DMG-008. The AI assistant must not promise a refund or reshipment while that investigation is open.

## 15. Refund Timelines for Shipping-Related Refunds

These timelines apply to refunds such as the Express Promise fee, RTO refunds and lost-parcel refunds, once a refund has been initiated.

| Refund destination | Completion time after initiation |
|---|---|
| UPI | 1–3 business days |
| Net banking | 3–5 business days |
| Debit or credit card | 5–7 business days |
| COD orders (to verified UPI ID or bank account) | 3–5 business days after valid payout details are verified |
| ShopSmart Credit (if the customer chooses it) | Instant on initiation |

If the refund has not arrived by the maximum timeline plus 2 business days, the customer should raise a ticket and include the UTR or ARN if available.

## 16. Worked Scenarios

**Scenario A: Delay within the estimate.** Order estimated for Friday 6 November; customer asks on Thursday 5 November why it has not arrived. Response: the date is an estimate and the order is still within it. Check tracking live. Offer to check again.

**Scenario B: Express order late.** An Express order promised for Wednesday arrives Friday because of courier hub congestion. Support verifies the live record. If confirmed as within the courier's control, the ₹99 Express fee is refunded and the item price is unaffected.

**Scenario C: Express order late due to the customer.** The courier attempted on the promised date but the customer was unreachable. This is not within ShopSmart's or the courier's control, so the Express Promise does not apply.

**Scenario D: Three failed attempts.** A prepaid parcel fails 3 attempts and returns to the warehouse. The refund is initiated within 2 business days of receipt and verification. The fee treatment is not defined (see Section 11), so the agent escalates fee questions.

**Scenario E: Remote location order.** A customer in a remote pincode asks for Express. Not available. Standard takes 7–10 business days with a ₹40 surcharge.

## 17. Frequently Asked Questions

**1. How long does Standard delivery take?**
Metro: 2–4 business days. Non-metro: 4–7 business days. Remote locations: 7–10 business days. These are estimates counted from order confirmation.

**2. How long does Express delivery take?**
Metro: 1–2 business days. Non-metro: 2–4 business days. Express is not available for remote locations.

**3. Is my delivery date guaranteed?**
No. All dates are estimates. The only guarantee is the Express Promise: if an Express order is late for a reason within ShopSmart's or the courier's control, the ₹99 Express fee is refunded.

**4. How much is shipping?**
Standard: ₹49, free on orders of ₹799 or more after discounts (fees excluded). Express: ₹99 flat, never waived. Remote locations: add ₹40. COD: add ₹30.

**5. Why was I charged shipping on an order above ₹799?**
Possible reasons: you chose Express (never waived), the ₹40 remote surcharge applies, the ₹30 COD fee applies, or the value after discounts fell below ₹799. Check the checkout summary and invoice.

**6. My order is late. What should I do?**
Check tracking in the Orders section. You can contact support once the order is 3 business days past its estimated date. If tracking shows no movement for 5 business days, an investigation opens.

**7. When is my order considered lost?**
10 business days after the estimated delivery date. You can then choose a refund or a reshipment, subject to stock and authorization.

**8. Can I change my delivery address?**
Yes, before the order is Shipped. After shipping, correction is not guaranteed and is handled by the courier on a best-effort basis.

**9. I missed the delivery. What happens now?**
The courier makes 3 attempts in total. After the third failure the parcel returns to the warehouse (RTO).

**10. Can I refuse a parcel at the door?**
Yes. For prepaid orders, the item price is refunded after the parcel is received back; the shipping and COD fees are not refunded. Three COD refusals in 12 months disable COD on your account.

**11. Tracking shows Delivered but I have not received my order.**
Report it within 48 hours of the Delivered timestamp. An investigation takes up to 5 business days. See SS-POL-DMG-008.

**12. Do you deliver on Sundays or outside India?**
Sunday delivery and international shipping are not defined in the current policy, so support cannot confirm either.

**13. Is Cash on Delivery available for every order?**
No. COD works for orders of ₹199 to ₹10,000, with a ₹30 fee, and is unavailable for some pincodes, restricted categories and accounts with 3 or more COD refusals in 12 months.

**14. Why did my items arrive in different parcels?**
An order can be split into more than one parcel. Check each parcel's tracking. Do not report an item missing until the status shows Delivered for it; the live order record shows which parcels exist.

**15. My Express order arrived late. Do I get a refund?**
If the delay was within ShopSmart's or the courier's control and support confirms it, the ₹99 Express fee is refunded. The item price is not refunded.

**16. My refund for a shipping fee has not arrived. Where is it?**
Refunds complete in 1–3 business days (UPI), 3–5 (net banking), 5–7 (card). If it is not credited within the maximum plus 2 business days, raise a ticket with the UTR or ARN.

## 18. Support and Escalation

| Level | Contact | First response | Target resolution |
|---|---|---|---|
| AI assistant (in-app chat) | 24x7 | Instant | n/a |
| Human agent chat (9:00–21:00 IST, all days) | In-app chat | 30 minutes in support hours | n/a |
| Email | support@shopsmart.example | 24 hours | 3 business days (complex: 7) |
| Level 2 Senior Support | Escalation from a ticket | 24 hours | 5 business days |
| Level 3 Grievance Officer (fictional role) | Written complaint | Acknowledge in 48 hours | 15 calendar days |

Escalation triggers: SLA breach, customer request, disputed evidence, or a conflict between documents and the database. Ticket IDs look like SS-T-123456. No phone support is offered.

## 19. Cross-References

- SS-POL-CAN-003: cancellation by order status, refusing delivery.
- SS-POL-RET-001: returns, return windows, courier-shipping reimbursement.
- SS-POL-DMG-008: damaged, missing, wrong items and "delivered but not received".
- SS-FAQ-PAY-004: payment failures, COD payment, invoices.
- SS-FAQ-ACC-007: addresses in the profile, contacting support.

## 20. Limitations and Cases Requiring Human Support

The AI assistant cannot decide the following and must escalate:

- Any request to confirm a delivery date as guaranteed.
- Express Promise refund approval, and whether an unusual cause was within control.
- Reshipment or refund for a lost parcel.
- Investigations for "Delivered but not received".
- Disputes about the number of delivery attempts or courier behaviour.
- Courier address correction after Shipped.
- Compensation, goodwill credits, Sunday delivery, international shipping, installation, oversized pickup and COD refusal edge cases.
- Any conflict between this document and the live order record.

**Security:** ShopSmart staff and the AI assistant never ask for full card numbers, CVV, PINs, passwords or OTPs. Customers should not share any such details with anyone claiming to be from ShopSmart.
