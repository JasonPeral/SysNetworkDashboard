# SysNetworkDashboard

## **Purpose of the project**

- Create a personal Dashboard that will replicate applications like **Grafana** and **Splunk** for personal use
- This project will deepen our understanding on knowledge needed to defend and secure a network through analyzing system info, network traffic analysis and parsing sys logs

## **Technologies we will use**

**Log Parser**

- **Goal:** Write a script to parse system or application logs for suspicious activity (e.g., failed logins).
- **Tools/Tech:** Python (`re`, `pandas`) or Bash.
- **Features:** Highlight patterns like brute force attempts, unusual login locations, or privilege escalations.

**Process Monitor**

- **Goal:** Write a tool to monitor active processes for anomalies (e.g., unexpected memory usage or unsigned binaries).
- **Tools/Tech:** Python (`psutil`) or PowerShell.
- **Learning:** Process analysis and endpoint monitoring.

**~~Wireshark~~ || Suricata**  

- Initially thought to use Wireshark but getting real time data is harder as wireshark is more used to analyze packets that have already came in.
- Suricata is a live IDS and can handle high levels of network traffic. Also we can integrate this into python using devtools (we can parse suricata logs with python and use that information to send to our dashboard as it has information on events like DNS queries, hTTP requests and alerts.)

---

### **Frameworks and Tools Summary**

- **Backend**: Python (Flask or FastAPI), **Suricata**, **psutil**, **regex**, **pandas**
- **Frontend**: React.js or Vue.js, **WebSockets**, **Chart.js** or **Plotly**
- **Visualization**: Real-time charts, alerts, and log visualizations
