# 🌐 IoT Data Dashboard (Flask + Streamlit)

This project demonstrates a simple **real-time IoT data dashboard** built with **Flask** for the backend (to receive sensor data) and **Streamlit** for the frontend (to visualize and display the data). The data used in this example is simulated for the sake of testing but can be extended to work with actual IoT devices like **Raspberry Pi** or **ESP8266**.

---

## 🚀 Features

- **Flask** Backend to receive and store IoT data (e.g., temperature, humidity)
- **Streamlit** Frontend to visualize the data in real-time using interactive charts
- **Real-time updates**: The data is refreshed every 5 seconds
- Simple, scalable, and easy-to-deploy solution for IoT dashboards

---

## 🛠️ Automated Installation & Running

This repository includes a **setup script** that will install all dependencies and run both the Flask backend and the Streamlit frontend automatically.

### **1️⃣ Clone the Repository**

    ```bash
    git clone https://github.com/Gowthamx0117/iot-dashboard.git
    cd iot-dashboard

### **2️⃣ Install Dependencies**
  Make sure you have Python installed, then install the required packages:

    ```bash
    pip install flask streamlit pandas requests

### **3️⃣ Run the Flask Backend**
    ```bash
    python app.py
This will start the Flask server on http://127.0.0.1:5000

### **4️⃣ Run the Streamlit Dashboard**
    ```bash
    streamlit run dashboard.py
This will launch the Streamlit dashboard, where you can view the real-time IoT data

## 📜 Real-World Use Cases
## Why is this needed?
**Real-Time Monitoring:**
This solution allows you to monitor IoT data (e.g., temperature, humidity) in real time, which is critical in applications like smart homes, factories, and agriculture. For example, factory operators can monitor equipment health or temperature fluctuations that could lead to breakdowns.

**Data Integration:**
The project can scale to integrate with any number of IoT devices, storing and visualizing their data. Whether it's environmental monitoring, health data, or smart home sensors, the backend is designed to handle this in a flexible manner.

**Custom Dashboards:**
With Flask and Streamlit, you can quickly prototype dashboards tailored to your specific needs. There’s no need for complex setups or costly enterprise solutions.



