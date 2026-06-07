# 🔐 Secure Communication Framework

A cybersecurity-focused secure communication system built in Python to demonstrate modern cryptographic protocols, secure authentication mechanisms, message lifecycle management, and security monitoring.

## Features

### Cryptography

* AES-256-GCM Encryption
* ECDHE Key Exchange
* HKDF Key Derivation
* Ed25519 Digital Signatures
* Perfect Forward Secrecy (PFS)

### Authentication & Access Control

* Secure Password Hashing using bcrypt
* Brute Force Protection
* Temporary Account Blocking
* Secure Login Workflow

### Secure Messaging

* End-to-End Encryption
* Message Integrity Verification
* Self-Destructing Messages (TTL)
* Session Key Rotation

### Monitoring & Auditability

* Security Dashboard
* Audit Logging
* Authentication Event Tracking
* Session Monitoring
* Message Lifecycle Tracking

## Architecture

User Login
→ Authentication Layer
→ ECDHE Key Exchange
→ HKDF Key Derivation
→ AES-256-GCM Encryption
→ Ed25519 Signature Verification
→ Secure Message Relay
→ TTL-Based Message Management
→ Security Dashboard & Audit Logs

## Technologies Used

* Python
* Cryptography
* bcrypt
* Object-Oriented Programming

## Security Concepts Demonstrated

* Symmetric Encryption
* Asymmetric Cryptography
* Authenticated Encryption
* Perfect Forward Secrecy
* Secure Password Storage
* Rate Limiting
* Audit Logging
* Secure Session Management

## Project Objective

The goal of this project is to implement and understand the security mechanisms used in modern communication systems while providing practical experience in applied cryptography, secure system design, authentication, monitoring, and message protection.

## Installation

Clone the repository:

```bash
git clone https://github.com/kriti-1-9/Secure-Chat-Application-Cryptography-Based-Python-.git
```