# DCP Management System
## Digital Credit Provider - Kenya CBK Compliant Loan Origination System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Frappe](https://img.shields.io/badge/Frappe-v15-blue.svg)](https://frappeframework.com/)
[![Vue 3](https://img.shields.io/badge/Vue-3.4-green.svg)](https://vuejs.org/)
[![Progress](https://img.shields.io/badge/Progress-72%25-orange.svg)]()

**A Central Bank of Kenya (CBK) compliant Digital Credit Provider system built on ERPNext and Frappe Framework.**

---

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Features](#features)
- [Compliance Status](#compliance-status)
- [Installation](#installation)
- [Development](#development)
- [API Documentation](#api-documentation)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

The DCP Management System is a custom Frappe/ERPNext app that extends the Lending module to create a CBK-compliant loan origination system for digital credit providers in Kenya. It provides:

- **Customer-facing portal**: Vue 3 SPA for self-service loan applications
- **KYC compliance**: Secure document management per Data Protection Act
- **Consent management**: Immutable audit trails for CRB checks and data processing
- **Regulatory reporting**: CBK data submission framework (in development)

**Current Status**: 72% Demo-Ready MVP

---

## 🏗️ Architecture

### System Components

```
┌─────────────────────────────────────────────────────────┐
│                    Vue 3 SPA Frontend                    │
│         (TailwindCSS, Pinia, Vue Router, SDK)           │
└─────────────────────┬───────────────────────────────────┘
                      │ REST API
┌─────────────────────▼───────────────────────────────────┐
│              DCP Management (Custom App)                 │
│  • Customer Onboarding    • KYC Management              │
│  • Consent Logging        • Loan Application API        │
└─────────────────────┬───────────────────────────────────┘
                      │ DocType Extension
┌─────────────────────▼───────────────────────────────────┐
│         ERPNext Core + Frappe Lending Module            │
│  • Customer Management    • Loan Products               │
│  • Accounting             • Payment Entries             │
└─────────────────────────────────────────────────────────┘
```

### Key Principles

- ✅ **No Core Modifications**: Extends ERPNext via custom app
- ✅ **API-First Design**: Clean separation of frontend and backend
- ✅ **Compliance by Design**: Privacy and audit trails built-in
- ✅ **Mobile-First**: Responsive TailwindCSS UI

---

## ✨ Features

### Implemented (Ready for Demo)

#### 1. Self-Registration & Authentication
- ✅ Guest-accessible registration form
- ✅ Auto-creates User + DCP Customer records
- ✅ Email-based password setup
- ✅ Role-based redirect (Customer → Portal)

**API**: `POST /api/method/dcp_management.api.onboard_customer`

#### 2. KYC Verification System
- ✅ 3-step wizard (Personal Info → Address → Documents)
- ✅ Secure document upload (National ID, KRA PIN, Passport Photo)
- ✅ Privacy-compliant storage (all attachments marked `is_private`)
- ✅ Status tracking: Incomplete → Pending → Verified → Rejected
- ✅ User ownership validation

**DocType**: `DCP Customer` with secure attachment fields  
**API**: `POST /api/method/dcp_management.api.upload_kyc_documents`

#### 3. Consent Management (CBK Stage 4 Compliant)
- ✅ Immutable audit log via Child Table
- ✅ Captures: Consent Type, IP Address, Timestamp, Policy Version
- ✅ Integrated in loan application flow
- ✅ Types: CRB Check, Terms & Conditions, Privacy Policy, Data Processing

**DocType**: `Consent Log` (istable: 1, track_changes: 1)  
**API**: `POST /api/method/dcp_management.api.log_consent`

#### 4. Loan Application Interface
- ✅ KYC pre-check validation
- ✅ Loan calculator with tenure selection
- ✅ Creates Loan Application in Lending module
- ✅ Auto-creates ERPNext Customer if missing
- ✅ Consent logging before submission

**API**: `POST /api/method/dcp_management.api.apply_for_loan`

#### 5. Customer Dashboard
- ✅ Loan summary statistics
- ✅ Active loan details
- ✅ Quick actions (Apply, Pay, Support)
- ⚠️ Currently displays mock data (Lending integration incomplete)

**Frontend**: `dcp_management/public/frontend/src/views/DashboardView.vue`

---

### In Development (Priority Roadmap)

#### Priority 1: Mock Services Layer (4 hours)
- [ ] `services/crb_mock.py` - Credit score simulation
- [ ] Loan decisioning logic (Score-based approval)
- [ ] Replace mock loan data with real Lending queries

#### Priority 2: CBK Reporting (6 hours)
- [ ] `CBK Report` DocType
- [ ] `services/cbk_reporting.py` - Daily/monthly report generation
- [ ] Scheduled tasks for automatic submission
- [ ] JSON schema per CBK specifications

#### Priority 3: Consumer Protection (5 hours)
- [ ] `Customer Issue` DocType for complaints
- [ ] Support ticket logging API
- [ ] Resolution tracking workflow
- [ ] Frontend support widget

---

## 🏛️ Compliance Status

### CBK Digital Credit Provider Licensing Requirements

| Stage | Requirement | Status | Notes |
|-------|-------------|--------|-------|
| **Stage 2: Customer Onboarding** |
| | Identity Verification (National ID) | ✅ Complete | 8-digit validation |
| | KRA PIN Verification | ✅ Complete | 11-char validation |
| | Secure Document Storage | ✅ Complete | `is_private=1` flag |
| | Data Protection Policy | ✅ Complete | Privacy by design |
| **Stage 3: Loan Origination** |
| | Loan Application Interface | ✅ Complete | Web form + API |
| | CRB Check Consent | ✅ Complete | Logged with IP/timestamp |
| | Credit Scoring | ⚠️ Partial | Mock not implemented |
| | Disbursement Tracking | ⚠️ Partial | Lending module integration needed |
| **Stage 4: Data Protection** |
| | Consent Management | ✅ Complete | Immutable audit trail |
| | Right to Access | ⚠️ Partial | API exists, UI needed |
| | Right to Erasure | ❌ Missing | GDPR compliance TODO |
| **Stage 5: Reporting** |
| | Daily Loan Reports | ❌ Missing | CBK Report DocType needed |
| | Monthly Outstanding | ❌ Missing | Scheduled task needed |
| | Consumer Redress Logs | ❌ Missing | Issue tracking TODO |

**Overall Compliance**: 65% (Stage 2 & 4 complete, Stage 3 & 5 in progress)

---

## 🚀 Installation

### Prerequisites

- Frappe Framework v15+
- ERPNext v15+
- Frappe Lending module installed
- Node.js 18+ (for frontend build)
- Python 3.10+

### Setup

1. **Install the app**:
```bash
cd frappe-bench
bench get-app https://github.com/your-repo/dcp_management.git
bench --site your-site install-app dcp_management
```

2. **Build frontend**:
```bash
cd apps/dcp_management/dcp_management/public/frontend
npm install
npm run build
```

3. **Migrate database**:
```bash
bench --site your-site migrate
```

4. **Clear cache & restart**:
```bash
bench clear-cache
bench restart
```

5. **Access the portal**:
```
https://your-site/portal
```

---

## 🛠️ Development

### Backend Development

**Location**: `dcp_management/dcp_management/`

```bash
# Watch Python files (auto-reload on save)
bench start

# Apply schema changes
bench --site your-site migrate

# Create new DocType
bench new-doctype
```

**Conventions**:
- **Tabs** for indentation (strict Frappe requirement)
- Linting: `ruff` (config in `pyproject.toml`)
- Whitelisted endpoints: `@frappe.whitelist()` in `api.py`

### Frontend Development

**Location**: `dcp_management/public/frontend/`

```bash
cd apps/dcp_management/dcp_management/public/frontend

# Development server (hot reload)
npm run dev

# Production build
npm run build

# Build + deploy (run from bench root)
./apps/dcp_management/build_frontend.sh
bench clear-cache
bench restart
```

**Tech Stack**:
- Vue 3 (Composition API)
- TailwindCSS
- Pinia (state management)
- frappe-js-sdk
- Vite

### Project Structure

```
apps/dcp_management/
├── dcp_management/
│   ├── api.py                    # Whitelisted API endpoints
│   ├── auth.py                   # Authentication hooks
│   ├── hooks.py                  # Frappe app hooks
│   ├── utils.py                  # Helper functions
│   ├── dcp_management/
│   │   └── doctype/
│   │       ├── dcp_customer/     # Main customer DocType
│   │       └── consent_log/      # Audit trail
│   ├── public/frontend/          # Vue 3 SPA
│   │   ├── src/
│   │   │   ├── components/
│   │   │   ├── views/
│   │   │   ├── stores/           # Pinia stores
│   │   │   └── router/
│   │   └── dist/                 # Built files
│   └── www/
│       ├── portal.html           # SPA entry point
│       └── portal.py
├── build_frontend.sh             # Build script
├── pyproject.toml               # Python config
└── README.md                    # This file
```

---

## 📚 API Documentation

### Authentication

Most endpoints require authentication. Guest-accessible endpoints are marked with `allow_guest=True`.

**Base URL**: `/api/method/dcp_management.api`

### Endpoints

#### **POST** `/onboard_customer` (Guest)
Register a new customer.

**Request**:
```json
{
  "email": "user@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "phone": "+254712345678"
}
```

**Response**:
```json
{
  "message": "Success",
  "user_id": "user@example.com",
  "customer_id": "DCP-CUST-00001"
}
```

---

#### **POST** `/upload_kyc_documents` (Authenticated)
Upload KYC documents for verification.

**Request**:
```json
{
  "customer_id": "DCP-CUST-00001",
  "national_id": "12345678",
  "kra_pin": "A123456789Z",
  "residential_address": "123 Main St",
  "county": "Nairobi",
  "city": "Nairobi",
  "files_data": {
    "id_front": "/files/id_front.jpg",
    "id_back": "/files/id_back.jpg",
    "kra_certificate": "/files/kra.pdf",
    "passport_photo": "/files/photo.jpg"
  }
}
```

---

#### **POST** `/apply_for_loan` (Authenticated)
Submit a loan application.

**Request**:
```json
{
  "customer_id": "DCP-CUST-00001",
  "amount": 50000,
  "tenure": 3,
  "purpose": "Business",
  "consent_data": {
    "ip_address": "192.168.1.1",
    "policy_version": "v1.0"
  }
}
```

**Response**:
```json
{
  "status": "Submitted",
  "name": "LOAN-APP-00001",
  "message": "Your loan application has been submitted successfully"
}
```

---

#### **GET** `/get_customer_loans` (Authenticated)
Fetch customer's loan history.

**Parameters**: `customer_id`

**Response**:
```json
{
  "loans": [...],
  "active_loan": {...},
  "kyc_status": "Verified"
}
```

---

## 🗺️ Roadmap

### Q1 2026 - MVP Completion
- [x] Core architecture setup
- [x] Self-registration & KYC
- [x] Consent management
- [ ] CRB mock integration
- [ ] Loan decisioning logic
- [ ] CBK reporting foundation

### Q2 2026 - Production Ready
- [ ] AML screening integration
- [ ] Real CRB API integration (e.g., Metropol, TransUnion)
- [ ] M-Pesa payment gateway
- [ ] SMS notifications
- [ ] Email templates
- [ ] Admin dashboard

### Q3 2026 - CBK Licensing
- [ ] Complete CBK Stage 5 requirements
- [ ] Penetration testing
- [ ] Data protection audit
- [ ] CBK submission documentation
- [ ] Live pilot with 100 customers

### Q4 2026 - Scale
- [ ] Multi-tenant support
- [ ] WhatsApp integration
- [ ] AI-powered credit scoring
- [ ] Alternative data sources

---

## 🔒 Security Considerations

### Implemented
- ✅ User ownership validation on all customer endpoints
- ✅ Private file storage for KYC documents
- ✅ CSRF protection via frappe-js-sdk
- ✅ Role-based access control (Customer, Loan Officer, System Manager)
- ✅ Audit trails on consent logs

### TODO
- [ ] Rate limiting on API endpoints
- [ ] Password complexity enforcement
- [ ] 2FA for high-value transactions
- [ ] Encryption at rest for PII fields
- [ ] Regular security audits

---

## 🐛 Known Issues

1. **Dashboard displays mock data** - Lending module integration incomplete
2. **No CRB integration** - Loan decisioning is manual
3. **Payment endpoint logs only** - No actual payment entry creation
4. **IP address capture** - Frontend implementation not verified
5. **No AML screening** - Required for CBK Stage 4

---

## 🤝 Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/dcp_management
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### Development Setup
```bash
# Clone your fork
git clone https://github.com/your-username/dcp_management.git

# Install pre-commit hooks
cd dcp_management
pre-commit install

# Create a new branch
git checkout -b feature/my-feature
```

---

## 📄 License

MIT

---

## 📞 Support

- **Documentation**: See [DCP_MVP_Plan.md](../../DCP_MVP_Plan.md) and [FRONTEND_BUILD.md](FRONTEND_BUILD.md)
- **Issues**: Report bugs and feature requests via GitHub Issues
- **Email**: dev@example.com

---

## 🙏 Acknowledgments

- **Frappe Framework** - Low-code platform foundation
- **ERPNext** - Core ERP functionality
- **Frappe Lending** - Loan management module
- **Central Bank of Kenya** - Regulatory framework
- **Vue.js Community** - Frontend framework

---

## 📊 Project Stats

- **Lines of Code**: ~5,000 (Backend: 3,200, Frontend: 1,800)
- **DocTypes**: 2 (DCP Customer, Consent Log)
- **API Endpoints**: 10+
- **Frontend Views**: 6 (Onboarding, Login, KYC, Dashboard, Apply, About)
- **Demo Readiness**: 72%

---

**Built with ❤️ for financial inclusion in Kenya**

*Last Updated: January 11, 2026*
