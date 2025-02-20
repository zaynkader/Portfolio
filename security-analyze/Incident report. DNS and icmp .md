# Cybersecurity Incident Report: DNS and ICMP Traffic Analysis

**Date:** 18-02-2025 
**Analyst:** Zayn

## 1. Summary of the Incident

This report analyzes a cybersecurity incident where users reported that they were unable to access the website **www.yummyrecipesforme.com**. The error message **"destination port unreachable"** was displayed when attempting to load the webpage. A network protocol analysis using **tcpdump** was performed to investigate the issue. The analysis revealed that **DNS requests sent via UDP port 53 were receiving ICMP "port unreachable" responses**.

This suggests that the DNS server **203.0.113.2** was either **down, misconfigured, or blocked**, preventing users from resolving domain names into IP addresses.

## 2. Technical Analysis

### 2.1. Network Traffic Logs (tcpdump Analysis)
- **First two log entries**: Outgoing DNS query from the user's computer to the DNS server requesting the IP address of `www.yummyrecipesforme.com`.
- **Third and fourth log entries**: ICMP response from the DNS server (`203.0.113.2`) indicating that UDP **port 53 was unreachable**.
- **Timestamps**: The first failure occurred at **1:24:32 PM**.
- **Source IP:** `192.51.100.15` (user's computer).
- **Destination IP:** `203.0.113.2` (DNS server).
- **Protocol Involved:** DNS over **UDP port 53**, followed by **ICMP error responses**.

### 2.2. Key Findings
- **The DNS server at `203.0.113.2` was not responding to queries.**
- **ICMP "port unreachable" errors indicate that the DNS service on UDP port 53 was unavailable.**
- **Multiple failed attempts confirm that this was not a temporary issue.**

## 3. Possible Causes of the Incident

1. **DNS Server Failure** – The server may have crashed or been shut down.
2. **Firewall Misconfiguration** – Firewall rules may be blocking DNS requests on **UDP port 53**.
3. **Network Routing Issues** – Incorrect routing may be preventing DNS queries from reaching the server.
4. **DNS Service Misconfiguration** – The DNS service may have been disabled or misconfigured.

## 4. Recommendations & Next Steps

To resolve this issue, the following troubleshooting steps should be taken:

1. **Check if the DNS server is operational**: Verify that the DNS service on `203.0.113.2` is running.
2. **Inspect firewall rules**: Ensure that **UDP port 53 is open** for DNS queries.
3. **Perform network connectivity tests**:
   - Use `ping 203.0.113.2` to check if the DNS server is reachable.
   - Use `traceroute 203.0.113.2` to analyze network routing.
4. **Examine DNS logs**: Look for errors or service disruptions.
5. **Restart or reconfigure the DNS service**: If necessary, restart the DNS server and verify settings.
6. **Implement backup DNS servers**: Redirect requests to an alternative DNS server to restore functionality while troubleshooting.

## 5. Security Considerations

- **Monitor DNS logs** for unauthorized changes or suspicious activity.
- **Harden firewall rules** to prevent unauthorized access to DNS servers.
- **Ensure redundancy** by using secondary DNS servers to avoid future outages.
- **Investigate potential cyber threats** if the DNS failure was caused by an attack (e.g., DoS attack on the DNS service).

## 6. Conclusion

This incident demonstrates the importance of **monitoring DNS traffic** and maintaining **network availability**. The issue was identified through **tcpdump analysis**, which showed **ICMP "port unreachable" errors** related to **UDP port 53**. The DNS failure prevented users from resolving domain names, causing a service outage. Immediate remediation steps should focus on **restoring DNS services, checking firewall settings, and implementing failover mechanisms** to prevent similar incidents in the future.

---

**Prepared by:** Zayn
**Role:** Cybersecurity Analyst  
**Date:** 18-02-2025

This report is part of my **Cybersecurity Incident Response Portfolio** on GitHub. It demonstrates my ability to analyze network traffic, identify security issues, and document findings effectively.