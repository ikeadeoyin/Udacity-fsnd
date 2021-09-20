# TCP/IP
In this section, we'll look at the suite of communication protocols that is used to transfer data over the Internet. These communication protocols are most often referred to as **TCP/IP**, which is an abbreviation that refers to the two main protocols involved—**Transmission Control Protocol (TCP)** and **Internet Protocol (IP).**

<img src="img/../Lesson%202/img/img3.png">

# **Takeaways**
TCP/IP is a suite of communication protocols that is used to connect devices and transfer data over the Internet.

**TCP/IP uses:**

- **IP addresses**: An IP address identifies the location of a computer on a network.
- **Ports**: A port is a location on the recipient computer, where data is received.
While an IP address tells you where to find a particular computer, it doesn't tell you specifically where on that computer a particular connection should be made—that's what port numbers are for.

**Some port numbers you should know**:

- **Port 80**: The port number most commonly used for HTTP requests. For example, when a client makes a request to a web server, this request is usually sent through port 80.
- **Port 5432**: The port number used by most database systems; default port for Postgres.

# Connections and Sessions in TCP/IP

<img src="img/../Lesson%202/img/img4.png">

# **Takeaways**
- TCP/IP is connection-based, meaning all communications between parties are arranged over a connection. A connection is established before any data transmission begins.
- Over TCP/IP, we'll always need to establish a connection between clients and servers in order to enable communications. Moreover:
    - Deliveries over the connection are error-checked: if packets arrive damaged or lost, then they are resent (known as retransmission).
- Connecting starts a `session`. Ending the connection ends the session.
- In a database session, many `transactions` can occur during a given session. Each transaction does work to commit changes to the database (updating, inserting, or deleting records).
---
## **Aside: the UDP Protocol**
The internet also offers the UDP protocol. UDP stands for User Datagram Protocol. UDP is much simpler than TCP: hosts on the network send data (in units called datagrams) without any connections needing to be established.

## **TCP vs UDP**
If TCP is like building highways between houses before sending packages between them, then UDP is much like sending over a carrier pigeon from one house to another in order to deliver packages: you don't know whether the pigeon will head in the right way, drop your package along the way, or encounter an issue mid-travel. On the other hand, there is less overhead to use UDP than managing a connection over TCP / building a highway.

When speed is more important than reliability, especially when applications need to stream very small amounts of information quickly (smaller packages of information means less issues with reliability), then UDP is preferred. A lot of real time streaming applications, (e.g. live TV streaming, Voice over IP (VoIP)) prefer UDP over TCP. Since UDP does not need to retransmit lost datagrams, nor does it do any connection setup, there are fewer delays over UDP than TCP. TCP's continuous connection is more reliable but has more latency.