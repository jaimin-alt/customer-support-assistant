# ShopSmart Warranty and Product Support Policy

> **Fictional notice:** ShopSmart is a fictional company and these policies are fictional. This document was created for a software demonstration (a college RAG and AI-agent project). It is not real company policy, not financial advice and not legal advice.

| Field | Value |
|---|---|
| Company | ShopSmart (fictional online multi-category marketplace, India) |
| Document ID | SS-POL-WAR-005 |
| Version | 1.0 |
| Effective date | 1 Nov 2026 |
| Last updated | 28 Oct 2026 |
| Category tag | warranty_support |
| Currency and time zone | INR (₹); IST |
| Related documents | SS-POL-RET-001 (Return and Refund), SS-POL-DMG-008 (Damaged, Missing or Incorrect Items), SS-CAT-PRD-006 (Product Catalog), SS-FAQ-ACC-007 (Account and Rewards) |

**Suggested RAG metadata:** doc_id: SS-POL-WAR-005 | category: warranty_support | version: 1.0 | effective_date: 2026-11-01 | doc_type: policy | region: IN | live_data_needed: true (for order delivery date, ticket status, repair status, replacement stock authorization)

## 1. Scope and Purpose

This policy outlines the fictional ShopSmart seller warranty for products purchased on the platform. It covers warranty durations by category, what is covered and excluded, how to claim warranty service, the repair and replacement process, and how warranty differs from the standard return window and DOA (Dead on Arrival) claims. 

It does not cover returns for change of mind (see SS-POL-RET-001) or items damaged in transit (see SS-POL-DMG-008). 

## 2. Static Policy vs Live Information

| Type | What belongs here | Source |
|---|---|---|
| Static (this document) | Warranty durations, coverage terms, exclusions, required proof, standard repair timelines, troubleshooting steps | Retrieved documents |
| Live (database or tools) | Item Delivered timestamp (starts the warranty), open warranty ticket status, live stock for replacements, authorized repair center updates | MongoDB tools |

The AI assistant must look up the order’s Delivered timestamp to verify if the warranty is active before promising any service. If the database and this document conflict, trust the database and flag the discrepancy.

## 3. Warranty Durations and Coverage by Category

The ShopSmart seller warranty provides coverage against specific defects arising under normal use during the warranty period. 

| Category | Duration | Covers |
|---|---|---|
| Electronics | 12 months | Manufacturing and functional defects |
| Home Appliances | 24 months | Manufacturing and functional defects |
| Accessories | 6 months | Manufacturing defects |
| Footwear | 90 days | Sole separation, stitching defects |
| Fashion | 30 days | Stitching and fabric defects |
| Home Essentials | 3 months | Manufacturing defects |

**Start date:** The warranty period begins exactly on the **Delivered timestamp** of the item.
**Proof of purchase:** The order ID and the official ShopSmart invoice (downloadable as a PDF from the Orders section once the order is Shipped) are required to initiate a claim.

## 4. Manufacturer Warranties vs ShopSmart Seller Warranty

The warranty provided in this document is the **ShopSmart seller warranty**. 
- Manufacturer warranties are strictly separate, may have different durations or terms, and are not extended, managed, or guaranteed by ShopSmart.
- ShopSmart support and the AI assistant must **make no claims about real manufacturers** or their specific policies. 
- Customers seeking to use a manufacturer's warranty must contact the manufacturer directly using the documentation provided inside the product packaging.

## 5. Dead on Arrival (DOA) vs Warranty Claim

**Rule:** A defective Electronic or Home Appliance reported within its 7-day return window is classified as Dead on Arrival (DOA). 
- DOA items are handled as a **return or replacement** under SS-POL-RET-001. 
- They are **not** subjected to a warranty repair process. 
- Once the 7-day return window closes, any subsequent defect is treated as a warranty claim under this policy. 

## 6. Warranty Exclusions

The ShopSmart seller warranty **does not cover**:
1. Accidental, physical, or liquid damage (e.g., cracked screens, water spills, dropped appliances).
2. Misuse, neglect, or operation outside the intended guidelines.
3. Unauthorized repairs, modifications, or opening of the product chassis by a non-ShopSmart technician.
4. Normal wear and tear, cosmetic damage, dents, or scratches occurring after delivery.
5. Consumables (e.g., water filters, vacuum bags, printer ink, ear tips) and natural battery degradation over time.
6. Damage from power surges or improper electrical supply.
7. Products used for commercial or industrial purposes (unless explicitly marked as commercial grade in the catalogue).
8. Items where the serial number or warranty seal has been tampered with, altered, or removed.

**Edge Case: Accidental Damage.** If a customer drops their phone and shatters the screen, this is accidental physical damage and is explicitly excluded. The AI assistant must inform the customer that accidental damage voids the seller warranty.

## 7. Warranty Claim Process

When a customer reports a defect outside the return window but inside the warranty period, the following process applies:

1. **Troubleshooting:** The AI assistant or human support will attempt basic troubleshooting (e.g., reset instructions, checking power sources).
2. **Ticket Creation:** If unresolved, a warranty ticket is raised (format: SS-T- followed by 6 digits). The customer must provide the order ID, invoice, a description of the defect, and photos/videos of the issue.
3. **Decision:** ShopSmart reviews the evidence and approves or rejects the warranty evaluation within **3 business days** of receiving complete evidence.
4. **Free Pickup:** If approved for evaluation, ShopSmart schedules a free reverse pickup. 
5. **Repair:** The item is sent to the repair facility. Repair takes up to **15 business days** from the time the item reaches the facility.
6. **Replacement:** A replacement is offered only if a repair is not possible, or if the identical defect recurs after 2 previous repairs.
7. **Refund:** A refund is processed **only** if a replacement is unavailable (requires human or authorized-system approval). 

**How warranty and return clocks work on a replacement item** is **requires clarification**. The AI assistant must not guess when a replacement's warranty expires.

## 8. Customer Keywords and Synonyms

item stopped working, product broken after a month, claim warranty, repair my phone, sole came off, stitching tore, machine making noise, battery draining fast, dead on arrival, DOA, manufacturer warranty, guarantee, out of warranty, repair center, replacement for defective item, fix my order, physical damage, accidental drop, cracked screen, liquid damage.

## 9. Frequently Asked Questions

**Q1. How long is the warranty on electronics?**
Electronics are covered for 12 months from the Delivered date for manufacturing and functional defects.

**Q2. My appliance stopped working on day 5. Is this a warranty repair?**
No. Defective electronics and appliances reported within the 7-day return window are handled as Dead on Arrival (DOA). You are eligible for a return or replacement under the standard return policy, not a repair.

**Q3. Does the warranty cover accidental damage like a cracked screen?**
No. Accidental, physical, and liquid damage are excluded from the ShopSmart seller warranty.

**Q4. What proof do I need for a warranty claim?**
You need your order ID and the ShopSmart invoice, which you can download from your Orders page.

**Q5. How long will the repair take?**
Repairs take up to 15 business days from the time the item reaches our repair facility.

**Q6. Do I have to pay to ship the item for repair?**
No. If your warranty evaluation is approved, ShopSmart schedules a free reverse pickup.

**Q7. Will I get a replacement instead of a repair?**
A replacement is provided if the item cannot be repaired, or if the exact same defect happens again after 2 previous repairs. 

**Q8. Can I just get a refund instead of waiting for a repair?**
Refunds for warranty claims are only issued if a repair is not possible and a replacement is completely out of stock. This requires specific system authorization.

**Q9. Is the manufacturer's warranty the same as the ShopSmart warranty?**
No. Manufacturer warranties are separate and may have different terms. ShopSmart does not manage or extend manufacturer warranties. 

**Q10. The sole of my shoe separated after 2 months. Is this covered?**
Yes. Footwear has a 90-day warranty that specifically covers sole separation and stitching defects, provided there are no signs of abnormal misuse.

**Q11. The battery on my 10-month-old phone doesn't last as long as it used to. Is this covered?**
Natural battery degradation over time is considered a consumable exclusion and is not covered by the warranty. 

**Q12. How quickly will you decide on my warranty claim?**
Once we have your complete evidence (photos/videos and description), a decision to approve or reject the evaluation is made within 3 business days.

**Q13. I lost my invoice. Can I still claim warranty?**
Your invoice is permanently available to download as a PDF in the Orders section of your ShopSmart account. 

**Q14. What happens if my warranty claim is rejected at the repair center?**
If the repair center determines the defect was caused by an exclusion (like liquid damage or unauthorized modification), the claim is rejected and the un-repaired item will be shipped back to you.

**Q15. Can the AI chat assistant approve a replacement for me?**
No. The AI assistant can help you troubleshoot and raise a ticket, but approval for repairs, replacements, or refunds comes from the human review team and the repair facility.

## 10. Support and Escalation

| Level | Contact | First response | Target resolution |
|---|---|---|---|
| AI assistant (in-app chat) | 24x7 | Instant | n/a |
| Human chat (9:00–21:00 IST, all days) | In-app | 30 minutes in support hours | n/a |
| Email | support@shopsmart.example | 24 hours | 3 business days (complex: 7) |
| Level 2 Senior Support | Escalation from a ticket | 24 hours | 5 business days |
| Level 3 Grievance Officer (fictional role) | Written complaint | Acknowledge in 48 hours | 15 calendar days |

Escalation triggers: SLA breach, customer request, disputed evidence, or a conflict between documents and the database.

## 11. Cross-References

- SS-POL-RET-001: Return windows (7 days for electronics/appliances), which dictate DOA handling.
- SS-FAQ-PAY-004: Invoice downloading instructions.
- SS-POL-DMG-008: Damaged/missing items (must be reported within 48 hours of delivery, not warranty).
- SS-CAT-PRD-006: Product limitations and category eligibility.

## 12. Limitations and Cases Needing Human Support

The AI assistant cannot approve repairs, replacements, or warranty refunds. It must escalate if the customer disputes an exclusion (e.g., claiming liquid damage was a manufacturing flaw), if the 15-business-day repair timeline is breached, or if the documents and the database conflict. Anything marked **requires clarification** must be escalated.

## 13. Security Note

ShopSmart staff and the AI assistant never ask for full card numbers, CVV, PINs, passwords or OTPs. Do not share them in chat, email or with anyone claiming to be from ShopSmart. 

## 14. Note on Interpretations and Clarifications

**Interpretations made in this document:**
- Warranty duration is calculated directly from the Delivered timestamp on a strict calendar-day basis (e.g., 90 days for footwear). 
- Accidental damage strictly voids the warranty; it does not convert it to a paid repair service in this fictional policy.

**Newly marked requires clarification:** 
- How warranty and return clocks work on a replacement item.
- Whether ShopSmart offers paid out-of-warranty repair services. 
- Logistics for returning rejected out-of-warranty items to the customer.