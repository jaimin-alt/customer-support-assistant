# ShopSmart Return and Refund Policy

> **Fictional notice:** ShopSmart is a fictional company. This document is part of a college software demonstration (LLM + RAG + agentic tool calling). It is not a real company policy and is not legal advice.

| Field | Value |
|---|---|
| Company | ShopSmart (fictional online multi-category marketplace, India) |
| Document ID | SS-POL-RET-001 |
| Category | returns_refunds |
| Version | v1.0 |
| Effective date | 1 November 2026 |
| Last updated | 28 October 2026 |
| Currency / time zone | INR (₹) / IST |
| Related documents | SS-POL-CAN-003 (Order Cancellation), SS-POL-DMG-008 (Damaged, Missing or Incorrect Items), SS-POL-WAR-005 (Warranty), SS-POL-SHP-002 (Shipping), SS-FAQ-PAY-004 (Payments), SS-FAQ-ACC-007 (Account and Rewards), SS-CAT-PRD-006 (Product Catalog) |

**Suggested retrieval metadata:** `doc_id=SS-POL-RET-001`, `category=returns_refunds`, `version=1.0`, `effective_date=2026-11-01`, `keywords=return, refund, refund pending, money not received, pickup, inspection, partial refund, return window`

---

## 1. Scope and Purpose

This policy explains how customers can return items delivered by ShopSmart and how refunds are calculated, approved, initiated and completed. It applies to all individual-customer orders in India in the categories Electronics, Home Appliances, Fashion, Footwear, Accessories and Home Essentials.

**This policy does not cover:**
- Cancelling an order before delivery (see SS-POL-CAN-003).
- Items reported damaged, missing or wrong within 48 hours of delivery (see SS-POL-DMG-008, which has its own rules and evidence requirements).
- Repair or replacement of a defective item after the return window has closed (see SS-POL-WAR-005).

**Static vs live information:** This document contains static rules. The status of a specific return or refund, the return-eligibility flag on a specific item, and an item's delivery date are live data held in the ShopSmart database. Support (including the AI assistant) must check live data before confirming anything about a specific order.

---

## 2. Return Eligibility

### 2.1 Return windows

| Product category | Return window |
|---|---|
| Fashion | **10 days** |
| Footwear | **10 days** |
| Electronics | **7 days** |
| Home Appliances | **7 days** |
| Accessories | **7 days** |
| Home Essentials | **7 days** |

### 2.2 How the return window is counted

- The window starts from the date the system marks the item **Delivered**. That date is **Day 0**.
- A return request must be **raised by 23:59 IST on Day 7** (7-day categories) or **Day 10** (10-day categories).
- For orders with multiple items delivered on different dates, the window is counted **separately for each item** from that item's own delivery date.
- The **request** must be raised inside the window. The **pickup** may take place after the window closes.
- Weekends and holidays are counted as calendar days when counting the window (the window is in days, not business days).

**Example (eligible):** A pair of shoes (Footwear, 10-day window) is marked Delivered on 3 December. Day 10 is 13 December. The customer raises a return request on 12 December at 20:00 IST. The request is inside the window and eligible for review, even if the pickup happens on 15 December.

**Example (window expired):** A mixer grinder (Home Appliances, 7-day window) is marked Delivered on 3 December. Day 7 is 10 December at 23:59 IST. A request raised on 11 December is outside the return window. It cannot be processed as a return. If the issue is a defect, the customer may use the warranty process (SS-POL-WAR-005).

### 2.3 Product-condition requirements

An item must be returned:
- **Unused and unwashed.**
- With **original tags, seals and packaging** intact.
- With **all accessories, manuals and free gifts** that came with it.
- With the **invoice** (available in the customer's account).

### 2.4 Electronics and Home Appliances: change of mind vs defect

| Situation | Returnable? |
|---|---|
| Change of mind, item **sealed or unopened and unused** | Yes, within 7 days |
| Change of mind, item **opened or used** | **No** |
| Opened item that is **defective, dead on arrival (DOA), damaged or wrong** | Yes, within 7 days, free return shipping |

A defective electronic or appliance reported inside its 7-day window is handled as a **return or replacement**, not as a warranty repair.

### 2.5 Non-returnable items

The following cannot be returned for change of mind:
- Innerwear and socks.
- Personal care and hygiene items.
- In-ear earphones and earbuds **once opened** (unless defective or wrong).
- Opened consumables and home essentials marked hygiene-sensitive.
- Items marked **Final Sale** or **Non-returnable** on the product page.
- Items without a required seal or tag.

**Important:** The product page and the database flag override category defaults. If an item is flagged non-returnable in the database, it is non-returnable even if its category is normally returnable. If an item is flagged returnable but the customer believes it should not be, the database flag is used and the discrepancy is noted for review.

**Exception:** A non-returnable item that arrives damaged, defective, incomplete or incorrect is covered by SS-POL-DMG-008 (report within 48 hours of delivery) or the warranty policy, not rejected on the basis of this list.

---

## 3. How to Request a Return

1. Open **Orders**, select the item, and choose **Return**. (Items not eligible do not show the option.)
2. Select a reason: change of mind, defective, damaged, wrong item, missing accessory, or other.
3. Upload photos where requested. Photos are required for defective, damaged and wrong-item reasons.
4. Choose a refund method (original payment method or ShopSmart Credit).
5. Confirm. A return request ID is shown.

If the Return option is not visible, the item may be non-returnable, the window may have closed, or the item may not yet be marked Delivered. Contact support with the order ID and the item name; support must check the live record.

---

## 4. Return Review, Pickup and Inspection

| Stage | Timeline |
|---|---|
| Review of the request | Within **24 hours**. Items flagged eligible in the database may be **auto-approved**. |
| Pickup scheduling | Within **2 business days** of approval |
| Pickup attempts | Up to **2 attempts** |
| Inspection at the warehouse | Within **2 business days** of the item reaching the warehouse |
| Refund initiation after a passed inspection | Within **2 business days** |

**Return stages shown in the account:** Return Requested → Return Approved → Pickup Scheduled → Picked Up → Received at Warehouse → Under Inspection → Refund Approved (or Return Rejected / Partial Refund Offered) → Refund Initiated → Refund Completed.

**If both pickup attempts fail:** The return request is closed. The customer may raise it again **only if the return window is still open**. Customers should make sure someone is available at the address and the phone number on the order is reachable.

**Pincodes without pickup service:** The customer ships the item by courier. ShopSmart reimburses up to **₹100** on submission of the courier receipt. Whether a pincode is serviceable is live data and must be checked in the database.

---

## 5. Return Shipping Costs

| Return reason | Who pays |
|---|---|
| Defective, damaged, wrong or missing item | **ShopSmart.** Pickup is free. Shipping fee and COD fee are refunded. |
| Change of mind | **Customer.** A flat **₹60 reverse-pickup fee** is deducted from the refund. The original shipping fee and the COD fee are **not refunded**. |

---

## 6. Inspection Outcomes

After the item reaches the warehouse, it is inspected against the condition requirements in Section 2.3.

### 6.1 Full refund
The item passes inspection. The full item price paid is refunded (less the ₹60 pickup fee for change of mind).

### 6.2 Partial refund tiers

| Issue level | Examples | Outcome |
|---|---|---|
| **Minor** | Missing non-essential accessory, damaged outer packaging | **10% deduction** from the item price |
| **Moderate** | Visible use, missing essential accessory | **25% deduction** |
| **Severe** | Heavy use, damage, or a wrong or counterfeit item swapped in | **Return rejected** |

- The customer sees the deduction in a **Partial Refund Offered** status and may **accept or decline** it.
- If the customer declines, the item is sent back **once at no charge**.
- The deduction applies to the item price, not to shipping or fees.

### 6.3 Worked examples

**Example 1: Full refund, ShopSmart error.** A customer returns a kettle priced ₹1,500 as defective, within 7 days. It passes inspection. Refund: ₹1,500 plus the shipping fee paid if any. Pickup is free.

**Example 2: Change of mind with pickup fee.** A customer returns a fashion top priced ₹1,200 (unworn, tags on) for change of mind. Refund: ₹1,200 − ₹60 = **₹1,140**. The standard shipping fee already paid is not refunded.

**Example 3: Minor deduction.** A customer returns a sealed-box Bluetooth speaker priced ₹2,000 for change of mind. The outer box is crushed. Minor issue: 10% = ₹200. Refund: ₹2,000 − ₹200 − ₹60 = **₹1,740**.

**Example 4: Moderate deduction.** A pair of sports shoes priced ₹3,000 comes back visibly worn. Moderate issue: 25% = ₹750. If the reason was change of mind: ₹3,000 − ₹750 − ₹60 = **₹2,190**. The customer may decline and have the shoes sent back once.

**Example 5: Failed inspection.** A customer returns a wireless earbud set claimed to be "wrong item", but the returned unit has a different serial number from the one shipped and shows heavy use. This is Severe. The return is rejected. The customer is told the reason in writing and may raise a ticket to dispute it (see Section 9).

---

## 7. Refunds

### 7.1 Refund methods

- **Original payment method** (default), or
- **ShopSmart Credit** (customer option; instant on initiation), or
- For **COD orders**, to the customer's **verified UPI ID or bank account**.

### 7.2 Refund timelines

Refund initiation: within **2 business days** after inspection passes (within **1 business day** for pre-shipment cancellations, see SS-POL-CAN-003).

| Refund destination | Completion time after initiation |
|---|---|
| UPI | **1–3 business days** |
| Net banking | **3–5 business days** |
| Debit or credit card | **5–7 business days** |
| COD orders (UPI or bank transfer) | **3–5 business days** after valid payout details are verified |
| ShopSmart Credit | **Instant** on initiation |

Business days are Monday to Saturday, excluding national public holidays. Sundays are not business days.

### 7.3 Refund amount

- The item price paid, adjusted by any partial-refund deduction.
- Shipping fee, COD fee and the ₹60 pickup fee are **not refunded** on change-of-mind returns.
- Shipping fee and COD fee **are refunded** for defective, damaged, wrong or missing items.
- **Loyalty points** redeemed on the order are returned as points, or as ShopSmart Credit if the points have expired. Points earned on the returned item are reversed (see SS-FAQ-ACC-007).

### 7.4 Refund pending or money not received

A refund is **not yet late** until the maximum completion time for the method **plus 2 business days** has passed.

| Method | Raise a ticket if not credited after |
|---|---|
| UPI | 3 business days + 2 = **5 business days** from initiation |
| Net banking | 5 + 2 = **7 business days** |
| Debit or credit card | 7 + 2 = **9 business days** |
| COD payout | 5 + 2 = **7 business days** from verification |

When raising a ticket, share the order ID and the **UTR or ARN** if available. Never share a full card number, CVV, PIN or OTP.

If the account shows **Refund Initiated**, the money has left ShopSmart and is with the bank or UPI network. If it shows **Under Inspection** or **Return Approved**, no refund has been initiated yet. Support must check the live status before answering.

---

## 8. Rejected Returns

A return may be rejected when:
- The request was raised after the window closed.
- The item is non-returnable (Section 2.5).
- The item fails inspection at the Severe level.
- The item received is not the item shipped.
- Both pickup attempts failed and the window has since closed.

A rejection includes the reason. The customer can raise a ticket to dispute it. Disputed evidence is escalated to Level 2 (see Section 9). Support must not promise that a rejected return will be reversed.

---

## 9. Support and Escalation

| Level | Contact | First response | Target resolution |
|---|---|---|---|
| AI assistant | In-app chat, 24x7 | Instant | n/a |
| Human agent (chat, 9:00–21:00 IST, all days) | In-app chat | 30 minutes in support hours | n/a |
| Email | support@shopsmart.example | 24 hours | 3 business days (complex: 7) |
| Level 2 (Senior Support) | Escalation from a ticket | 24 hours | 5 business days |
| Level 3 (Grievance Officer, fictional role) | Written complaint | Acknowledged in 48 hours | 15 calendar days |

Escalate when: an SLA is breached, the customer asks, evidence is disputed, or documents and the database conflict. Ticket IDs look like `SS-T-123456` (fictional).

---

## 10. Frequently Asked Questions

**1. How many days do I have to return an item?**
Fashion and Footwear: 10 days. Electronics, Home Appliances, Accessories and Home Essentials: 7 days. Counting starts from the day the item is marked Delivered (Day 0), and you must raise the request by 23:59 IST on the last day.

**2. I ordered two items that arrived on different days. Which date counts?**
Each item has its own window, counted from that item's own delivery date.

**3. Can I return something after the window if I have already booked a pickup?**
The request must be raised inside the window. The pickup itself can happen after the window closes. If you did not raise the request in time, it is not eligible as a return.

**4. My return window has expired. What can I do?**
It cannot be processed as a return. If the item has a defect, check the warranty policy (SS-POL-WAR-005). A damaged, missing or wrong-item claim after 48 hours is handled as a manual-review request only if you are still inside the return window.

**5. Can I return a phone or laptop I have opened because I changed my mind?**
No. Opened Electronics and Home Appliances are returnable only if defective, dead on arrival, damaged or wrong. Sealed and unused ones can be returned for change of mind within 7 days.

**6. Which items can never be returned?**
Innerwear, socks, personal care and hygiene items, opened in-ear earphones (unless defective or wrong), opened hygiene-sensitive consumables, and anything marked Final Sale or Non-returnable. The product page and database flag always take priority.

**7. Do I pay for return shipping?**
Not if the item is defective, damaged, wrong or missing a part. For change of mind, a flat ₹60 pickup fee is deducted from your refund.

**8. How much will I get back?**
The item price paid, minus any partial-refund deduction (10% or 25%) and, for change of mind, the ₹60 pickup fee. Shipping and COD fees are refunded only for ShopSmart-error returns.

**9. When will the money reach me?**
Refund is initiated within 2 business days after the item passes inspection. After that: UPI 1–3 business days, net banking 3–5, debit or credit card 5–7, COD payouts 3–5 after payout details are verified. ShopSmart Credit is instant.

**10. My refund is pending / money not received. What now?**
Check the refund status in your account. If it shows Refund Initiated and the maximum timeline plus 2 business days has passed, raise a ticket with the order ID and the UTR or ARN. Support will check the live status. If it still shows Under Inspection, the refund has not been initiated yet.

**11. Why was I offered a partial refund?**
Inspection found a minor issue (10% deduction) or moderate issue (25% deduction) such as a missing accessory or visible use. You can decline, and the item is returned to you once at no charge.

**12. Why was my return rejected?**
Common reasons are an expired window, a non-returnable item, a severe condition problem, or a returned item that does not match what was shipped. The reason is shown in your return details. You can raise a ticket to dispute it.

**13. The pickup person did not come. What happens?**
There are up to 2 pickup attempts. If both fail, the request is closed and you can raise it again only if your window is still open.

**14. My pincode has no pickup. How do I return?**
Ship the item by courier and upload the receipt. ShopSmart reimburses up to ₹100.

**15. I used reward points on this order. What happens to them?**
Redeemed points are returned as points, or as ShopSmart Credit if they have expired. Points earned on the returned item are reversed.

**16. Can the AI assistant promise my refund will be approved?**
No. Approval depends on inspection and the live database record. The assistant can explain the rules and check the status.

---

## 11. Limitations and Cases Requiring Human Support

- This document does not decide any individual return. Final decisions come from the system and inspection team.
- **Needs live database lookup:** delivery date, return window status, item return flag, return and refund stage, pincode pickup availability, refund UTR.
- **Needs human escalation:** disputed inspection results, rejected returns the customer disputes, refunds beyond the maximum timeline plus 2 business days, conflicting delivery status, suspected swapped or counterfeit items.
- **Requires clarification (not defined in v1.0):** exchanges for a different size or colour, price-match, EMI refunds, gift-card refunds, international returns, goodwill credits, installation-related returns, and returns of oversized items. Do not assume rules for these.
- Never request passwords, OTPs, CVV or full card numbers in any support conversation.
