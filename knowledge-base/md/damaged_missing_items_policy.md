# ShopSmart Damaged, Missing or Incorrect Item Policy

> **FICTIONAL NOTICE:** ShopSmart is a fictional company created for a college software demonstration (LLM + RAG + agentic tool calling). Every policy, deadline and example in this document is invented. This is not a real company policy and is not legal advice.

## Document Information

| Field | Value |
|---|---|
| Document title | Damaged, Missing or Incorrect Item Policy |
| Company | ShopSmart (fictional online multi-category marketplace, India) |
| Document ID | SS-POL-DMG-008 |
| Version | v1.0 |
| Effective date | 1 November 2026 |
| Last updated | 28 October 2026 |
| Category tag | damaged_missing |
| Currency / time zone | INR (₹) / IST |
| Related documents | SS-POL-RET-001, SS-POL-SHP-002, SS-POL-WAR-005, SS-POL-CAN-003, SS-FAQ-ACC-007 |

**Suggested RAG metadata:** doc_id=SS-POL-DMG-008; category=damaged_missing; version=1.0; effective_date=2026-11-01; doc_type=policy; region=India; live_data_needed=order status, Delivered timestamp, parcel count, claim status, stock for replacement.

## 1. Scope and Purpose

This policy covers what a customer should do, and what ShopSmart's support system may and may not promise, when an order arrives damaged, with an item missing, with the wrong item, incomplete, with tampered packaging, or is marked Delivered but was not received.

**Keywords customers use:** broken product, cracked screen, item damaged in transit, parcel empty, item missing from box, wrong product received, wrong size, wrong colour, only one item came, package opened, seal broken, marked delivered but not received, parcel not received, refund for damaged item.

## 2. Static Policy vs Live Information

| Static (this document) | Live (database or tools) |
|---|---|
| Reporting deadline, evidence rules, decision timelines, outcomes | Order status and exact Delivered timestamp |
| Rules for conflicts and escalation | Number of parcels in the order and each parcel's status |
| Refund timelines | Whether a replacement is in stock |
| | Claim and ticket status, refund status |

The AI assistant must look up the order before applying any rule here. If this document and the database disagree, the database is trusted and the difference is flagged.

## 3. Definitions

- **Damaged item:** the item arrived broken, cracked, dented, torn, leaking or otherwise physically damaged.
- **Missing item:** an item listed on the order or invoice is not in the parcel, or part of the item (for example an essential accessory) is absent.
- **Incorrect (wrong) item:** the product, model, colour, size or quantity received differs from what was ordered. Ordering the wrong size yourself is not a wrong-item case; it is a change-of-mind return under SS-POL-RET-001.
- **Incomplete shipment:** some, but not all, items of the order have arrived. This is only a claim once every parcel is shown as Delivered.
- **Tampered packaging:** signs the parcel was opened or altered, such as broken seals, resealed tape or a mismatched label.
- **Marked delivered but not received:** the system shows Delivered but the customer has not received the parcel.
- **Dead on arrival (DOA) / defective:** the item arrives or fails to work properly without visible physical damage. See Section 10.

## 4. The 48-Hour Reporting Deadline

**Rule:** report within **48 hours of the Delivered timestamp**. This applies to damaged, missing, wrong, incomplete and "marked delivered but not received" claims.

- 48 hours means 48 clock hours, counted from the date and time the system marks the item Delivered. Weekends and Sundays are included in the count.
- The time that counts is when you submit your report through in-app chat, the Help Centre or email, not when a human replies. The AI assistant is available 24x7 for this reason.
- For orders with several parcels or items, each item's own Delivered timestamp is used.

**Example:** Order delivered Monday 2 November 2026 at 11:00 IST. The 48-hour deadline is Wednesday 4 November 2026 at 11:00 IST.

This deadline is shorter than the return window (10 days for Fashion and Footwear; 7 days for Electronics, Home Appliances, Accessories and Home Essentials). Do not wait for the return window to report a delivery problem.

## 5. Evidence Required

| Claim type | Clear photos (item, outer packaging, shipping label) | Unboxing video |
|---|---|---|
| Damaged | Required | Recommended |
| Missing or incomplete (Electronics, Home Appliances) | Required | **Required** |
| Missing or incomplete (other categories) | Required | Recommended |
| Wrong item (Electronics, Home Appliances) | Required | **Required** |
| Wrong item (other categories) | Required | Recommended |
| Marked delivered but not received | Not possible (no parcel) | Not applicable |

**Tips for acceptable evidence:**

- Photograph the item, all sides of the outer box, and the shipping label with the order details visible.
- Record the unboxing without cuts if possible, showing the sealed parcel being opened.
- Keep all packaging, tags and contents until the claim is decided.
- Do not share card numbers, CVV, passwords or OTPs in photos, chat or email.
- Accepted file formats and size limits are not defined in v1.0 (requires clarification). If an upload fails, ask the customer to try the Help Centre or email support@shopsmart.example.

For "marked delivered but not received", no item photos exist. Specific supporting information beyond the report itself is not defined in v1.0 (requires clarification). The AI assistant collects the order ID and when the customer found the parcel missing, files the report and escalates.

## 6. How a Claim Is Handled

1. **Look up the order.** Confirm the order, items, Delivered timestamp and parcel status.
2. **Check the deadline.** Compare the report time with the Delivered timestamp plus 48 hours.
3. **Collect evidence.** Ask for exactly what is needed for the claim type (Section 5).
4. **Register the claim and ticket** (format SS-T- followed by 6 digits).
5. **Decision** within **3 business days of complete evidence**. The clock starts only when the evidence is complete.
6. **Outcome:** replacement (if in stock) or refund. Both need human or authorized-system approval.

The AI assistant must not say "your refund is approved" or "a replacement will be sent" before the system shows approval.

## 7. Damaged Items

Report within 48 hours with photos of the item, outer packaging and shipping label. A video is recommended but not required.

- **If approved:** ShopSmart offers a replacement if the item is in stock, or a refund.
- **Fees on damaged-item refunds:** the shipping fee and any COD fee are refunded as well, because the problem is a ShopSmart-side error.
- **Return shipping:** free for damaged items. Pickup arrangements follow SS-POL-RET-001.
- **Inspection:** if the item is returned, the warehouse inspects it within 2 business days of receipt. If the damage found is inconsistent with the report (for example, signs of use or damage after delivery), the case is handled under the inspection rules of SS-POL-RET-001, where the outcome can be a partial refund (10% or 25% deduction) or rejection. A human reviews this.
- Whether a refund can be issued before the item is physically collected is not defined in v1.0 (requires clarification). The AI assistant states only what the live claim shows.

## 8. Missing Items and Incomplete Shipments

**Item missing inside a delivered parcel.** Report within 48 hours. Provide photos of the item or box contents, the outer packaging and the shipping label. For Electronics and Home Appliances, an unboxing video is required.

**Fewer items than ordered (incomplete shipment).** First check the live record: ShopSmart may have split the order into several parcels. Items in a parcel that is still Shipped or Out for Delivery are not missing. Their lateness falls under SS-POL-SHP-002. Only treat an item as missing when its parcel shows Delivered or the system shows a conflict.

**Outcome if approved:** replacement (if in stock) or refund of the missing item's price, plus fee refunds per Section 7. The decision is made within 3 business days of complete evidence.

## 9. Wrong or Incorrect Items

Report within 48 hours. Provide photos of the item, packaging and shipping label. For Electronics and Home Appliances an unboxing video is required.

- Do not use or wash the item before reporting.
- Compare with the order record: item name, size, colour and quantity. A different size or colour than ordered is a wrong item; a different size than the customer needs is a change-of-mind return.
- **Fees:** shipping and COD fees are refunded. Return shipping is free.
- **Outcome:** replacement with the correct item (if in stock) or refund, after approval.
- Where the item returned is not the item sent (for example a swapped or counterfeit item), the return can be rejected under SS-POL-RET-001. A human decides.

## 10. Items Not Working vs Physically Damaged

An item that arrives not working but looks undamaged is **dead on arrival (DOA)**. Within the return window it is handled as a return or replacement under SS-POL-RET-001, not as a warranty repair. After the return window, defects go to SS-POL-WAR-005. The 48-hour deadline does not apply to DOA claims reported within the return window, but reporting early speeds up resolution.

## 11. Tampered Packaging

- If the parcel looks opened or resealed at delivery, photograph the outside before opening and record the unboxing.
- A customer may refuse a visibly tampered parcel at the door. The refusal rules of SS-POL-CAN-003 then apply, under which the shipping fee and COD fee are non-refundable. How these fees are treated in a tampered-parcel refusal is not separately defined in v1.0 (requires clarification).
- If the customer accepts the parcel, report within 48 hours with evidence. Tampered packaging alone is not proof of loss or fault. The AI assistant must not conclude who is responsible.
- If the item is missing or wrong, the matching evidence rules in Section 5 apply.

## 12. Marked Delivered but Not Received

1. **Report within 48 hours** of the Delivered timestamp.
2. The AI assistant checks the order and tracking, collects details and files the report.
3. ShopSmart investigates for **up to 5 business days**.
4. If the investigation supports the claim, the outcome is replacement (if in stock) or refund, after approval.

**Before reporting, customers are encouraged** to check with household members, neighbours and the building security desk.

**What the AI assistant must not do:** promise a refund during the investigation, or say the parcel was definitely delivered or definitely lost.

## 13. Reports After 48 Hours

A report after 48 hours is **not automatic** and is not automatically rejected either.

- **Still inside the return window** (10 days for Fashion and Footwear; 7 days for other categories): handled as a **manual-review request**, and as a normal return if the item is eligible under SS-POL-RET-001. Opened Electronics and Home Appliances are returnable only if defective, DOA, damaged or wrong.
- **After the return window:** defects go to warranty under SS-POL-WAR-005. Missing or wrong items outside the window require a human reviewer.

The AI assistant must not promise an outcome. It states the process and creates the ticket.

## 14. Insufficient Evidence

1. Tell the customer precisely what is missing (for example "a clear photo of the shipping label" or "an unboxing video").
2. Ask **once**.
3. If the evidence is still insufficient, **escalate to a human**.

The AI assistant must not reject the claim, and must not approve it, on its own authority.

## 15. Conflicts Between the Customer's Claim and the Order Record

Check the live database first. If a conflict remains, escalate.

| Conflict | Action |
|---|---|
| Status is Shipped or Out for Delivery, customer says it was delivered | Re-check live status. If it remains, escalate. The 48-hour clock has not started because no Delivered timestamp exists |
| Status is Delivered, customer says the parcel is still with the courier | Treat as "marked delivered but not received" and file a report |
| Status is Cancelled, customer says an item arrived | Escalate. Do not decide |
| Customer's order details differ from the record (item, size, colour) | Quote the live record and escalate if still disputed |

## 16. Outcomes, Refund Methods and Timelines

**Outcomes:** replacement (if in stock) or refund. A replacement's delivery date is an estimate under SS-POL-SHP-002 and is not guaranteed. How the warranty and return clocks work on a replacement item is not defined in v1.0 (requires clarification).

**Refund amount:** item price paid, plus shipping fee and COD fee refunded for these ShopSmart-error claims. Rewards points redeemed on the order are returned as points, or as ShopSmart Credit if the points have expired.

**Refund method:** original payment method, or ShopSmart Credit if the customer chooses it. COD refunds go to the customer's verified UPI ID or bank account.

| Refund destination | Completion time after initiation |
|---|---|
| UPI | 1–3 business days |
| Net banking | 3–5 business days |
| Debit or credit card | 5–7 business days |
| COD orders (to verified UPI ID or bank account) | 3–5 business days after valid payout details are verified |
| ShopSmart Credit (customer option) | Instant on initiation |

Refund initiation after inspection passes: within 2 business days. If the refund has not arrived by the maximum timeline plus 2 business days, raise a ticket with the UTR or ARN if available. Rewards points on returned items are reversed.

## 17. When the AI Assistant Must Escalate Instead of Promising

Escalate when any of the following is true:

- Evidence is still insufficient after one request.
- The customer disputes the evidence decision.
- The order status conflicts with the claim.
- The report is after 48 hours.
- The claim is "delivered but not received".
- Tampered packaging, suspected swapped or counterfeit item, or repeated claims on the account.
- A support SLA has been breached.
- The customer asks for a human.
- The retrieved documents do not contain the answer.

Suggested wording: "I have registered your report under ticket SS-T-xxxxxx. A human reviewer will decide this. I can't confirm a refund or replacement yet."

## 18. Worked Scenarios

**Scenario A: Damaged within the window.** A mixer grinder (Home Appliance) is delivered Monday 2 November 2026 at 11:00 with a cracked jar. The customer reports on Tuesday 3 November at 09:30 with photos. A video is only recommended for damage. Once evidence is complete, a decision is due within 3 business days (by Friday 6 November, assuming no public holiday). Replacement if in stock, or refund, after approval. Shipping and COD fees would be refunded.

**Scenario B: Wrong electronics item, no video.** A customer receives a different earphone model and has photos but no video. The assistant asks once for the video. The customer says they did not record one. The assistant escalates; it neither refuses nor approves.

**Scenario C: Reported after 48 hours, window open.** A fashion order was delivered Monday 2 November 10:00. The customer reports a torn sleeve on Thursday 5 November 10:00 (72 hours). Not automatic. The 10-day window is open, so it is a manual-review request and a normal return if eligible.

**Scenario D: Window expired.** Footwear delivered 2 November; sole separation reported 20 November (day 18). The 48-hour deadline and the 10-day window have passed. The case goes to SS-POL-WAR-005 (90-day footwear warranty for sole separation and stitching defects), subject to warranty exclusions.

**Scenario E: Status conflict.** The order shows Out for Delivery but the customer says it arrived. The assistant re-checks. If it still shows Out for Delivery, it escalates. No refund is promised.

**Scenario F: Delivered but not received.** Marked Delivered Tuesday 3 November 16:20; customer reports Wednesday 4 November 10:00. Within 48 hours. Investigation up to 5 business days; no promise.

**Scenario G: Split parcels.** The order has two parcels; one is delivered, the other still Shipped. The customer reports a "missing" item 30 hours after the first delivery. It is not missing; it is in transit. Explain, show tracking, and apply SS-POL-SHP-002.

## 19. Frequently Asked Questions

**1. How long do I have to report a damaged item?**
48 hours from the Delivered timestamp.

**2. What evidence do I need?**
Clear photos of the item, outer packaging and shipping label. For missing or wrong items in Electronics and Home Appliances, an unboxing video is also required.

**3. I received the wrong product. What do I do?**
Report within 48 hours with photos (and a video for Electronics or Home Appliances). If approved, you get a replacement if in stock, or a refund. Shipping and COD fees are refunded.

**4. Part of my order is missing. Is it lost?**
Check tracking first. Your order may be split into several parcels. If every parcel is Delivered and an item is still missing, report within 48 hours.

**5. The status says Delivered but I did not get my order.**
Report within 48 hours. The investigation takes up to 5 business days.

**6. Will I automatically get a refund if I report?**
No. Replacements and refunds need human or authorized-system approval after the evidence is reviewed.

**7. How long until I get a decision?**
Within 3 business days of complete evidence. "Delivered but not received" investigations take up to 5 business days.

**8. I reported after 48 hours. Is my claim rejected?**
Not automatically. If you are still within the return window, it is handled as a manual-review request and a normal return if eligible. After the return window, defects go to warranty.

**9. Do I pay return shipping for a damaged or wrong item?**
No, it is free. For change-of-mind returns a ₹60 pickup fee applies, but not here.

**10. Will my shipping and COD fees be refunded?**
Yes, if the claim is approved because of a damaged, missing or wrong item.

**11. My photos were rejected. What now?**
The assistant tells you what is missing and asks once. If it is still insufficient, the case goes to a human.

**12. The packaging looked opened. Should I accept the parcel?**
You may refuse at the door, in which case the refusal rules in SS-POL-CAN-003 apply (shipping and COD fees not refunded). If you accept, photograph and film the unboxing and report within 48 hours.

**13. My phone arrived but does not switch on.**
Report promptly. Within the return window it is handled as DOA, a return or replacement under SS-POL-RET-001, not a warranty repair.

**14. How long does the refund take to arrive?**
UPI 1–3 business days, net banking 3–5, debit or credit card 5–7, COD orders 3–5 after payout details are verified, ShopSmart Credit instantly. If not received after the maximum plus 2 business days, raise a ticket.

**15. Can the chat assistant approve my replacement?**
No. It can register your report and show status, but approval comes from a human or authorized system.

**16. I ordered a size M but need L. Is this a wrong item?**
No. That is a change-of-mind return under SS-POL-RET-001, not a damaged or wrong-item claim.

## 20. Support and Escalation

| Level | Contact | First response | Target resolution |
|---|---|---|---|
| AI assistant (in-app chat) | 24x7 | Instant | n/a |
| Human agent chat (9:00–21:00 IST, all days) | In-app chat | 30 minutes in support hours | n/a |
| Email | support@shopsmart.example | 24 hours | 3 business days (complex: 7) |
| Level 2 Senior Support | Escalation from a ticket | 24 hours | 5 business days |
| Level 3 Grievance Officer (fictional role) | Written complaint | Acknowledge in 48 hours | 15 calendar days |

Escalation triggers: SLA breach, customer request, disputed evidence, or conflict between documents and the database. No phone support is offered.

## 21. Cross-References

- SS-POL-RET-001: return windows, inspection, partial refunds, refund timelines.
- SS-POL-SHP-002: delivery estimates, delays, split parcels, RTO.
- SS-POL-WAR-005: defects after the return window, DOA and warranty exclusions.
- SS-POL-CAN-003: refusing delivery.
- SS-FAQ-ACC-007: contacting support and complaints.

## 22. Limitations and Cases Requiring Human Support

The AI assistant cannot decide, and must escalate:

- Approval or rejection of any replacement or refund.
- Disputed or insufficient evidence after one request.
- Reports after 48 hours.
- Delivered-but-not-received investigations.
- Conflicts between the order record and the customer's claim.
- Suspected swapped, counterfeit or fraudulent claims.
- Cases listed as "requires clarification": file formats and size limits, refund before pickup, replacement warranty clocks, fee treatment in tampered-parcel refusals.
- Replacement stock and delivery date for the replacement.

**Security:** ShopSmart staff and the AI assistant never ask for full card numbers, CVV, PINs, passwords or OTPs. Customers should not post evidence that shows such details.
