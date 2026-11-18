# ShopSmart Order Cancellation Policy

> **Fictional notice:** ShopSmart is a fictional company. This document is part of a college software demonstration (LLM + RAG + agentic tool calling). It is not a real company policy and is not legal advice.

| Field | Value |
|---|---|
| Company | ShopSmart (fictional online multi-category marketplace, India) |
| Document ID | SS-POL-CAN-003 |
| Category | cancellation |
| Version | v1.0 |
| Effective date | 1 November 2026 |
| Last updated | 28 October 2026 |
| Currency / time zone | INR (₹) / IST |
| Related documents | SS-POL-RET-001 (Return and Refund), SS-POL-SHP-002 (Shipping and Delivery), SS-FAQ-PAY-004 (Payments and Billing), SS-POL-DMG-008 (Damaged, Missing or Incorrect Items), SS-FAQ-ACC-007 (Account and Rewards) |

**Suggested retrieval metadata:** `doc_id=SS-POL-CAN-003`, `category=cancellation`, `version=1.0`, `effective_date=2026-11-01`, `keywords=cancel order, cancellation option missing, cancel after shipping, refuse delivery, RTO, COD refusal, order cancelled refund`

---

## 1. Scope and Purpose

This policy explains when and how a customer can cancel a ShopSmart order **before delivery**, what happens to payments, and what to do when the cancel option is not available.

**Where this policy stops:** Once an order is marked **Delivered**, it can no longer be cancelled. The customer should use the Return and Refund Policy (SS-POL-RET-001). Items that arrive damaged, missing or wrong are covered by SS-POL-DMG-008.

**Static vs live information:** This document holds static rules. The current status of an order (Processing, Packed, Shipped, Out for Delivery, Delivered, Cancelled) is **live data** from the ShopSmart database. Support, including the AI assistant, must check the live status before telling a customer whether cancellation is possible.

---

## 2. Order Statuses

Orders move through: **Processing → Packed → Shipped → Out for Delivery → Delivered**, or **Cancelled** at an eligible stage.

---

## 3. Cancellation Rules by Order Status

| Order status | Can the customer cancel? | Cancellation charge | Refund |
|---|---|---|---|
| **Processing** | **Yes.** Self-service in the app or website | None | Full |
| **Packed** | **Request allowed.** Approved only if the parcel has not been handed to the courier | None | Full, if approved |
| **Shipped** | **No cancellation.** Customer may refuse delivery or return after delivery | None, but see refusal rules in Section 5 | See Section 5 |
| **Out for Delivery** | **No cancellation.** Customer may refuse at the door | None, but see Section 5 | See Section 5 |
| **Delivered** | **Not a cancellation.** Use the return process | Per return rules | Per SS-POL-RET-001 |

### 3.1 Processing
The order has been confirmed but not yet packed. The customer can cancel from **Orders → Cancel**. The cancellation is instant and no fee applies. Orders usually remain in Processing for up to 1 business day (up to 2 business days for large appliances), so the self-service window can be short.

### 3.2 Packed
The item has been packed but may not have left the warehouse. The customer can submit a cancellation request. The request is **approved if the parcel has not yet been handed to the courier**. If the courier has already collected it, the status changes to Shipped and the request cannot be approved. Support should not promise approval; the outcome depends on the live status at the time of the request.

### 3.3 Shipped
The parcel is with the courier. The order **cannot be cancelled**. The customer has two options:
1. **Refuse the delivery** when it arrives (the parcel returns to ShopSmart as RTO, see Section 5).
2. **Accept delivery and raise a return** if the item is returnable and still within its return window (SS-POL-RET-001).

Address changes are also not allowed after Shipped. Corrections are handled by the courier on a best-effort basis only and are not guaranteed.

### 3.4 Out for Delivery
The same rules as Shipped apply. The customer can refuse at the door. There is no cancellation button.

### 3.5 Delivered
A delivered order is not cancelled; it is returned. See SS-POL-RET-001 for windows (7 days for Electronics, Home Appliances, Accessories and Home Essentials; 10 days for Fashion and Footwear).

---

## 4. Cancellation Confirmation and Charges

- **Confirmation:** an email and an in-app notice are sent within **15 minutes** of a successful cancellation. If neither arrives after 15 minutes, check the live order status. The order status in the account is the source of truth, not the email.
- **Cancellation charges:** ShopSmart charges **no cancellation fee** at any eligible stage.
- **Multi-item orders:** Cancelling only some items of a multi-item order is **not defined in v1.0 and requires clarification**. Support must check the live order screen and must not assume item-level cancellation is available.

---

## 5. Refund Handling After Cancellation or Refusal

### 5.1 Prepaid orders (UPI, debit card, credit card, net banking)

| Event | Refund initiation | Refund amount |
|---|---|---|
| Customer cancels at Processing or an approved Packed request | Within **1 business day** | Full order amount, including shipping fee |
| ShopSmart cancels (stock-out, payment verification failure) | Within **1 business day** | Full amount |
| Customer refuses delivery (RTO) | Within **2 business days** of the item being received and verified at the warehouse | **Item price only.** Shipping fee and COD fee are not refunded |

**Refund completion after initiation:**

| Refund destination | Completion time |
|---|---|
| UPI | **1–3 business days** |
| Net banking | **3–5 business days** |
| Debit or credit card | **5–7 business days** |
| ShopSmart Credit (customer option) | **Instant** on initiation |

Refunds go to the original payment method by default, or to ShopSmart Credit if the customer chooses it.

**Refund not received:** If the money has not arrived after the maximum timeline for the method **plus 2 business days**, raise a ticket with the order ID and the UTR or ARN if available. Never share a full card number, CVV, PIN or OTP.

### 5.2 Cash on Delivery orders
No money is collected before delivery, so **no refund applies** when a COD order is cancelled or refused.

**COD refusal rule:** After **3 COD refusals within 12 months**, COD is disabled for the account. The customer can still order using UPI, cards or net banking.

### 5.3 Loyalty points
Points redeemed on a cancelled order are returned as points, or as ShopSmart Credit if the points have expired. Points that would have been earned on the cancelled order are not credited (see SS-FAQ-ACC-007).

### 5.4 ShopSmart-initiated cancellations
ShopSmart may cancel an order for stock-out or failed payment verification. The customer receives a notification, and the full amount is refunded, initiated within 1 business day, with completion times as in Section 5.1.

---

## 6. When the Cancel Option Is Not Available

The Cancel button may be missing because:
- The order has moved to Shipped or Out for Delivery.
- The order is already Delivered or Cancelled.
- The order is still being confirmed after payment.
- The item type has restricted cancellation (live database flag).

**What to do:**
1. Check the order status under Orders.
2. If it still shows Processing or Packed, contact support in the in-app chat with the **order ID**.
3. Support checks the live order status. If the parcel is already shipped, cancellation is not possible; use the refusal or return options above.
4. If the customer believes the status is wrong, escalate through a ticket.

The AI assistant must **not** promise that an order will be cancelled. It can explain the rules and submit or suggest the request.

---

## 7. Edge Cases

| Situation | Expected response |
|---|---|
| Customer asks to cancel an order that shows **Shipped** | Explain that cancellation is not available. Offer refusal at delivery or a return after delivery, after checking the live status and returnability. |
| Customer cancels at Processing but the amount was debited | Refund is initiated within 1 business day. Share the completion time for the payment method. |
| Customer cancels a prepaid order, but no refund after the maximum time plus 2 business days | Check the live refund status. Raise a ticket with the UTR or ARN. |
| Order is Packed and the customer asks to cancel | Submit the request, but say approval depends on whether the courier has collected the parcel. Do not promise success. |
| Customer has refused 3 COD orders in 12 months and now wants COD | Explain COD is disabled for the account. Offer prepaid options. |
| The order was cancelled by ShopSmart for stock-out | Confirm the full refund is initiated within 1 business day. Check the live status. |
| Customer wants to cancel only one item from a multi-item order | Not defined in v1.0. Check the live order screen and escalate if the option is not shown. |
| Delivered order, customer says "cancel" | Not a cancellation. Redirect to SS-POL-RET-001 and check the return window. |

---

## 8. Support and Escalation

| Level | Contact | First response | Target resolution |
|---|---|---|---|
| AI assistant | In-app chat, 24x7 | Instant | n/a |
| Human agent (chat, 9:00–21:00 IST, all days) | In-app chat | 30 minutes in support hours | n/a |
| Email | support@shopsmart.example | 24 hours | 3 business days (complex: 7) |
| Level 2 (Senior Support) | Escalation from a ticket | 24 hours | 5 business days |
| Level 3 (Grievance Officer, fictional role) | Written complaint | Acknowledged in 48 hours | 15 calendar days |

Escalate when an SLA is breached, the customer asks, evidence is disputed, or the documents and the database conflict.

---

## 9. Frequently Asked Questions

**1. Can I cancel my order?**
It depends on the status. You can cancel yourself at Processing. At Packed you can request it, and it is approved only if the courier has not collected the parcel. At Shipped and Out for Delivery you cannot cancel. After Delivered, use the return process.

**2. How do I cancel an order?**
Go to Orders, select the order and tap Cancel. If the button is missing, check the order status and contact support in chat with your order ID.

**3. Is there a cancellation fee?**
No. ShopSmart does not charge a fee for cancellations at eligible stages.

**4. My order is Shipped. Can I still cancel?**
No. You can refuse the delivery when it arrives, or accept it and request a return if the item is returnable and within its window. For refusals of prepaid orders, the item price is refunded after the parcel is received back; the shipping and COD fees are not refunded.

**5. I cancelled. When will I get my money back?**
Refund is initiated within 1 business day. Then UPI takes 1–3 business days, net banking 3–5, and debit or credit card 5–7. ShopSmart Credit is instant.

**6. I cancelled but did not get a confirmation email.**
Confirmations come within 15 minutes by email and in-app notice. Check the order status in your account. If it shows Cancelled, the cancellation is done. If not, contact support.

**7. Do I get a refund on a cancelled COD order?**
No money was paid, so no refund applies.

**8. What happens if I keep refusing COD orders?**
After 3 COD refusals in 12 months, COD is turned off for your account. You can still pay online.

**9. The Cancel button is greyed out or missing. Why?**
The order is likely Shipped, Out for Delivery, Delivered or already Cancelled. If it still shows Processing or Packed, contact support with the order ID.

**10. ShopSmart cancelled my order. Why, and will I be refunded?**
Orders can be cancelled for stock-out or failed payment verification. You get a full refund, initiated within 1 business day.

**11. What happens to reward points I used on a cancelled order?**
They are returned as points, or as ShopSmart Credit if they have expired. Points you would have earned are not credited.

**12. Can I cancel just one item in my order?**
This is not defined in the current policy. Check the order screen. If the option is not shown, contact support. Do not assume it is possible.

**13. I changed my address after ordering. Can I still do that?**
Only before the order is Shipped. After that, the courier handles corrections on a best-effort basis with no guarantee.

**14. My refund has not arrived. What do I do?**
Wait until the maximum time for your method plus 2 business days. Then raise a ticket with your order ID and the UTR or ARN. See SS-POL-RET-001 Section 7.4 for the table of waiting times.

**15. Can the AI assistant cancel my order for me?**
It can explain the rules and check the status. It must not promise a cancellation or refund without the live status and authorization.

---

## 10. Limitations and Cases Requiring Human Support

- This document does not decide any individual cancellation. The live order status and system authorization decide.
- **Needs live database lookup:** current order status, courier handover for Packed orders, refund stage and UTR, COD refusal count, cancellation-restricted item flags.
- **Needs human escalation:** disputed order status, a Packed cancellation the customer says was wrongly denied, refunds past the maximum timeline plus 2 business days, repeated duplicate debits.
- **Requires clarification (not defined in v1.0):** partial (item-level) cancellation of multi-item orders, EMI cancellation, gift-card payments, international orders, goodwill credits, and cancellation of installation-linked orders. Do not invent rules for these.
- Never request passwords, OTPs, CVV or full card numbers in any support conversation.
