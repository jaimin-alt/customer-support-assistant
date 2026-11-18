# ShopSmart Product Catalog and Buying Guide

> **Fictional notice:** ShopSmart is a fictional company and these policies are fictional. This document was created for a software demonstration (a college RAG and AI-agent project). It is not real company policy, not financial advice and not legal advice.

| Field | Value |
|---|---|
| Company | ShopSmart (fictional online multi-category marketplace, India) |
| Document ID | SS-CAT-PRD-006 |
| Version | 1.0 |
| Effective date | 1 Nov 2026 |
| Last updated | 28 Oct 2026 |
| Category tag | product_catalog |
| Currency and time zone | INR (₹); IST |
| Related documents | SS-POL-RET-001 (Return and Refund), SS-POL-WAR-005 (Warranty), SS-FAQ-PAY-004 (Payment and Billing) |

**Suggested RAG metadata:** doc_id: SS-CAT-PRD-006 | category: product_catalog | version: 1.0 | effective_date: 2026-11-01 | doc_type: catalog | region: IN | live_data_needed: true (for live prices, stock availability, discounts, item-level return flags)

## 1. Scope and Purpose

This document provides a sample fictional product catalog for ShopSmart, including specifications, intended use, compatibility, and standard return/warranty eligibility. It also features a brief buying guide to help compare products.

## 2. Static Policy vs Live Information

| Type | What belongs here | Source |
|---|---|---|
| Static (this document) | Product specifications, baseline category, brand names, standard warranty duration, standard return category window | Retrieved documents |
| Live (database or tools) | **Live price**, stock availability, item-specific non-returnable overrides, active discounts | MongoDB tools |

**Crucial Price Rule:** The **live database price always overrides the catalogue price**. The prices listed in this document are baseline catalog prices. The price charged at checkout and shown on the invoice is binding for that order. The AI assistant must check the live database for current stock and pricing.

## 3. Product Catalog (Fictional Items)

### Electronics
**1. NovaTech Pro Smartphone**
- **Product ID / SKU:** ELEC-NVT-P100
- **Brand:** NovaTech (fictional)
- **Catalog Price:** ₹45,999
- **Key Specs:** 6.7" OLED display, 256GB storage, 12GB RAM, 50MP triple camera, 5000mAh battery.
- **Intended Use:** High-end mobile computing and photography.
- **Warranty:** 12 months (Electronics category).
- **Return Eligibility:** 7 days. Returnable for change of mind *only* if sealed/unopened. If opened, returnable only if defective/DOA.

**2. NovaTech Lite Smartphone**
- **Product ID / SKU:** ELEC-NVT-L050
- **Brand:** NovaTech (fictional)
- **Catalog Price:** ₹15,499
- **Key Specs:** 6.4" LCD display, 128GB storage, 6GB RAM, 13MP dual camera, 4500mAh battery.
- **Intended Use:** Budget-friendly everyday mobile use.
- **Warranty:** 12 months (Electronics category).
- **Return Eligibility:** 7 days. Returnable for change of mind *only* if sealed/unopened.

### Home Appliances
**3. AeroBreeze 1.5 Ton Inverter AC**
- **Product ID / SKU:** HAP-AER-AC15
- **Brand:** AeroBreeze (fictional)
- **Catalog Price:** ₹32,999
- **Key Specs:** 1.5 Ton capacity, 4-star energy rating, copper condenser, smart Wi-Fi enabled.
- **Intended Use:** Cooling medium-sized rooms (110-150 sq ft).
- **Warranty:** 24 months (Home Appliances category).
- **Return Eligibility:** 7 days. Returnable for change of mind *only* if sealed/unopened. **Note:** Installation services for large appliances are **requires clarification**.

**4. ChefMate 750W Mixer Grinder**
- **Product ID / SKU:** HAP-CMT-MG750
- **Brand:** ChefMate (fictional)
- **Catalog Price:** ₹2,499
- **Key Specs:** 750W copper motor, 3 stainless steel jars, overload protection.
- **Intended Use:** Heavy-duty kitchen grinding and blending.
- **Warranty:** 24 months (Home Appliances category).
- **Return Eligibility:** 7 days. Returnable for change of mind *only* if sealed/unopened.

### Fashion
**5. UrbanWeave Men's Cotton Casual Shirt**
- **Product ID / SKU:** FSH-URB-M01
- **Brand:** UrbanWeave (fictional)
- **Catalog Price:** ₹899
- **Key Specs:** 100% breathable cotton, slim fit, full sleeves, button-down collar.
- **Intended Use:** Casual and semi-formal wear.
- **Warranty:** 30 days (Fashion category - covers stitching/fabric defects).
- **Return Eligibility:** 10 days. Must be unused, unwashed, with original tags intact.

**6. UrbanWeave Women's Winter Puffer Jacket**
- **Product ID / SKU:** FSH-URB-W05
- **Brand:** UrbanWeave (fictional)
- **Catalog Price:** ₹2,199
- **Key Specs:** Water-resistant outer, synthetic down insulation, detachable hood.
- **Intended Use:** Cold weather protection.
- **Warranty:** 30 days (Fashion category).
- **Return Eligibility:** 10 days. Must be unused, unwashed, with original tags.

### Footwear
**7. StrideMax Pro Running Shoes**
- **Product ID / SKU:** FTW-STR-R99
- **Brand:** StrideMax (fictional)
- **Catalog Price:** ₹3,499
- **Key Specs:** Lightweight mesh upper, responsive foam midsole, anti-slip rubber outsole.
- **Intended Use:** High-impact running and athletic training.
- **Warranty:** 90 days (Footwear category - covers sole separation/stitching).
- **Return Eligibility:** 10 days. Must be unused with original tags.

**8. StrideMax Casual Canvas Sneakers**
- **Product ID / SKU:** FTW-STR-C20
- **Brand:** StrideMax (fictional)
- **Catalog Price:** ₹1,299
- **Key Specs:** Breathable canvas, flat rubber sole, lace-up design.
- **Intended Use:** Daily casual wear.
- **Warranty:** 90 days (Footwear category).
- **Return Eligibility:** 10 days. Must be unused with original tags.

### Accessories
**9. SoundVibe Wireless Earbuds**
- **Product ID / SKU:** ACC-SND-E10
- **Brand:** SoundVibe (fictional)
- **Catalog Price:** ₹1,799
- **Key Specs:** Bluetooth 5.2, active noise cancellation (ANC), 24-hour battery life with case.
- **Intended Use:** Personal audio listening.
- **Warranty:** 6 months (Accessories category).
- **Return Eligibility:** 7 days. **Limitation:** In-ear earphones are **non-returnable once opened** for hygiene reasons, unless defective/DOA (Section 2.5 of SS-POL-RET-001).

**10. SoundVibe Premium Leather Wallet**
- **Product ID / SKU:** ACC-SND-W44
- **Brand:** SoundVibe (fictional)
- **Catalog Price:** ₹799
- **Key Specs:** Genuine leather, RFID blocking, 6 card slots, coin pocket.
- **Intended Use:** Carrying currency and cards securely.
- **Warranty:** 6 months (Accessories category).
- **Return Eligibility:** 7 days. Unused condition with tags.

### Home Essentials
**11. SleepHaven Memory Foam Pillow**
- **Product ID / SKU:** HME-SLP-P01
- **Brand:** SleepHaven (fictional)
- **Catalog Price:** ₹1,199
- **Key Specs:** Contour design, cooling gel infused, hypoallergenic washable cover.
- **Intended Use:** Neck support and sleep comfort.
- **Warranty:** 3 months (Home Essentials category).
- **Return Eligibility:** 7 days. **Limitation:** Flagged as hygiene-sensitive. Non-returnable for change of mind if the vacuum seal is opened.

**12. AquaPure Water Filter Cartridge (Pack of 2)**
- **Product ID / SKU:** HME-AQA-F02
- **Brand:** AquaPure (fictional)
- **Catalog Price:** ₹599
- **Key Specs:** Multi-stage carbon block filtration. Compatible with AquaPure standard RO systems.
- **Intended Use:** Consumable water filtration.
- **Warranty:** 3 months (Home Essentials). **Limitation:** Consumable item; warranty covers manufacturing defects upon arrival, not usage depletion.
- **Return Eligibility:** 7 days. Non-returnable if opened or installed.

## 4. Buying Guide and Comparisons

### Choosing a Smartphone (NovaTech Pro vs Lite)
- **For Power Users:** The **NovaTech Pro** is ideal for heavy gaming, high-quality photography (50MP), and multitasking (12GB RAM).
- **For Everyday Use:** The **NovaTech Lite** offers excellent value for standard browsing, social media, and communication at a fraction of the cost.

### Choosing Footwear (StrideMax Running vs Casual)
- **For Fitness:** Select the **StrideMax Pro Running Shoes**. The responsive foam and mesh upper are designed for athletic impact.
- **For Lifestyle:** The **StrideMax Casual Canvas Sneakers** provide a flat, aesthetic profile suited for relaxed, everyday wear but lack the support needed for workouts.

## 5. Conflict Precedence

1. A product-page or database **non-returnable flag** overrides standard category return defaults. (e.g., if the live DB marks a specific shirt as Final Sale, it cannot be returned).
2. The **live database price** overrides the catalog prices listed in Section 3.
3. Live inventory overrides this catalog; if the DB says Out of Stock, the item cannot be promised.

## 6. Customer Keywords and Synonyms

compare phones, which AC to buy, specs for mixer grinder, is the pillow returnable, warranty on shoes, earbuds battery life, how much is the smartphone, buy leather wallet, best running shoes, cheap smartphone, product specifications, out of stock, live price, product details, buying guide.

## 7. Frequently Asked Questions

**Q1. Are the prices in this catalog final?**
No. The live database price always overrides the catalogue price. Discounts and dynamic pricing mean the checkout price is the binding one.

**Q2. I bought the NovaTech Pro phone and opened the box. Can I return it if I just don't like it?**
No. Electronics are returnable for change of mind only if the seal is intact and the box is unopened. If opened, it is only returnable if defective or incorrect.

**Q3. Do the SoundVibe Wireless Earbuds have Active Noise Cancellation?**
Yes, the SoundVibe Wireless Earbuds feature ANC and Bluetooth 5.2.

**Q4. Can I return the SoundVibe earbuds if I try them and they don't fit?**
No. In-ear earphones are non-returnable once opened due to hygiene policies, unless they are defective. 

**Q5. Is the AquaPure filter cartridge covered by a 3-month warranty?**
It falls under the 3-month Home Essentials warranty, but because it is a consumable, the warranty only covers manufacturing defects out of the box, not the natural depletion of the filter.

**Q6. What's the difference between the StrideMax Pro and the StrideMax Canvas?**
The Pro is built for high-impact athletic running with a foam midsole, while the Canvas is a flat-soled sneaker for everyday casual wear.

**Q7. Is the AeroBreeze AC smart-enabled?**
Yes, it is Wi-Fi enabled.

**Q8. Does ShopSmart install the AeroBreeze AC?**
Installation services for large appliances are not defined (requires clarification). We recommend asking support for current live policies or arranging local installation.

**Q9. Will ShopSmart price-match if I find the ChefMate Mixer cheaper elsewhere?**
Price matching is not defined (requires clarification). The AI assistant cannot authorize a price match.

**Q10. How long is the warranty on UrbanWeave shirts?**
Fashion items have a 30-day warranty against stitching and fabric defects. 

**Q11. I want to buy the SleepHaven pillow. Can I return it?**
It has a 7-day return window, but it is flagged as a hygiene-sensitive item. It cannot be returned for change of mind if the vacuum seal is opened.

**Q12. What sizes are available for the UrbanWeave Men's Shirt?**
Stock and size availability must be checked in the live database. 

**Q13. Are the prices inclusive of shipping?**
No. Shipping fees depend on the total order value, your location (Standard, Express, Remote), and payment method (COD fee). See SS-FAQ-PAY-004.

**Q14. Can the AI guarantee a product will work with my existing devices?**
The AI can read the listed compatibility specs (e.g., standard RO systems for the AquaPure filter), but cannot guarantee universal compatibility outside of listed parameters.

**Q15. Where do I find the actual price I will be charged?**
The final, binding price is calculated at the checkout screen in the app or website and is printed on your official invoice.

## 8. Support and Escalation

| Level | Contact | First response | Target resolution |
|---|---|---|---|
| AI assistant (in-app chat) | 24x7 | Instant | n/a |
| Human chat (9:00–21:00 IST, all days) | In-app | 30 minutes in support hours | n/a |
| Email | support@shopsmart.example | 24 hours | 3 business days (complex: 7) |
| Level 2 Senior Support | Escalation from a ticket | 24 hours | 5 business days |
| Level 3 Grievance Officer (fictional role) | Written complaint | Acknowledge in 48 hours | 15 calendar days |

## 9. Limitations and Cases Needing Human Support

The AI assistant cannot override live database prices, authorize price matching, or override a non-returnable database flag. It must escalate if a customer demands a price match or requests installation services that are not explicitly documented. 

## 10. Security Note

ShopSmart staff and the AI assistant never ask for full card numbers, CVV, PINs, passwords or OTPs. Do not share them in chat, email or with anyone claiming to be from ShopSmart. 

## 11. Note on Interpretations and Clarifications

**Interpretations made in this document:**
- Earbuds and Pillows were specifically interpreted as hygiene-sensitive / non-returnable upon opening to align with standard Indian e-commerce norms and Section 2.5 of the MPF.
- The AquaPure filter was explicitly designated as a consumable to enforce the warranty exclusions in SS-POL-WAR-005.

**Newly marked requires clarification:** 
- Installation services for large appliances (like the AeroBreeze AC).
- Price-matching guarantees against competitors.