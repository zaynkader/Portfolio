# 🛡️ Botium Toys Security Audit  

## **1️⃣ Scope & Goals**  
- **Scope:** The audit covers **all IT-managed assets, policies, and security controls**.  
- **Goals:** Identify **security gaps** and **compliance issues** and suggest improvements.  

## **2️⃣ Assets & Risk Assessment**  
### **Current IT Assets**  
- Employee devices: laptops, desktops, mobile phones  
- Internal network & data storage  
- Storefront & warehouse equipment  
- Security systems (firewall, antivirus)  

### **Identified Risks & Issues**  
🔴 **High-risk areas** (8/10 risk score):  
- No **encryption** for stored customer credit card data  
- No **Intrusion Detection System (IDS)**  
- Employees have **unrestricted access** to all data  
- No **disaster recovery plan**  

## **3️⃣ Security Controls Assessment**  
### ✅ **What is Implemented?**  
✔ Firewall with security rules  
✔ Antivirus software installed  

### ❌ **What is Missing?**  
❌ No **encryption** for customer data  
❌ No **centralized password management**  
❌ No **separation of duties** in data access  
❌ No **disaster recovery & backup plan**  

## **4️⃣ Recommendations for Improvement**  
🔹 **Encrypt customer data** to protect payment information  
🔹 **Deploy an IDS** to monitor for suspicious activity  
🔹 **Restrict employee access** using **Least Privilege**  
🔹 **Enforce stronger password policies**  
🔹 **Create a Disaster Recovery Plan** with **regular backups**  

## **5️⃣ Compliance Considerations**  
📌 **Regulations Botium Toys must comply with:**  
- **GDPR** (for EU customer data protection)  
- **PCI DSS** (for credit card transactions security)  

---
📌 **This audit was conducted as part of my cybersecurity training.** 🚀