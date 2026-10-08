# Farmer Conekt

## 1. Platform Overview

Farmer Conekt is a digital platform designed to streamline agricultural trade by minimizing intermediaries and connecting all stakeholders within a single integrated system. The platform brings together farmers, buyers, and transporters to enable efficient, transparent, and reliable transactions.

## 2. Problem & Context

- Agriculture employs over 65% of Rwanda’s population and contributes approximately 25% to GDP.  
- Farmers face limited access to reliable markets and buyers.  
- Post-harvest losses for perishable goods range between 20–40%.  
- Middlemen dominate pricing, reducing farmers’ profits.  
- Seasonal overproduction leads to price drops and food wastage.  
- Lack of coordination and transparency creates inefficiencies in the supply chain.  

## 3. Solution

- Farmers create accounts and list their products on the platform.  
- Customers browse available products and place orders online.  
- Payments are securely processed through Flutterwave.  
- Farmers receive order notifications and prepare goods for delivery or pickup.  
- Transporters handle logistics between farmers and customers.  
- Farmers are provided with planting plans to reduce surplus and improve production planning.  

## 4. Key Features

- User accounts for farmers, buyers, and transporters with dashboards  
- Product listing, browsing, ordering, and order tracking system  
- Secure online payments via Flutterwave with automated notifications  
- Logistics coordination for delivery and pickup through transporters  
- Smart tools, including planting plans and surplus prediction to improve production and reduce waste  

## 5. Technology Stack

- Frontend: HTML, CSS, Vanilla JavaScript
- Backend: Python with Flask  
- Database: MySQL  
- Authentication: Password-based authentication  
- Payments: Flutterwave API  
- Deployment: Ubuntu servers  
- Version Control: Git & GitHub  

## 6. Repository Structure & Installation

```farmers_conekt/
├── README.md
├── requirements.txt
├── set_up.sh
├── .gitignore
│
├── api/
│   ├── index.py
│   ├── config.py             
│   ├── __init__.py             
│   │
│   ├── database/
│   │   ├── db.py             
│   │   ├── schema.sql         
│   │   └── seed_data.sql     
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── analytics_routes.py
│   │   ├── auth_routes.py
│   │   ├── buyer_routes.py
│   │   ├── farmer_routes.py
│   │   ├── payment_routes.py
│   │   ├── planting_routes.py
│   │   └── transporter_routes.py
│   │
│   ├── middleware/             
│   │   ├── __init__.py
│   │   └── role_required.py
│   │
│   ├── uploads/
│   │   └── crop_images/        
│   │
│   ├── tests/                 
│   └── env/             
│
├── frontend/
│   ├── index.html            
│   ├── farmer.html             
│   ├── transporter.html        
│   │
│   ├── pages/
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── admin-dashboard.html
│   │   ├── transporter.html    
│   │   └── 404.html
│   │
│   ├── scripts/
│   │   ├── 404-handler.js
│   │   ├── buyer.js
│   │   ├── filters.js
│   │   ├── login.js
│   │   ├── product.js
│   │   ├── session.js
│   │   └── transporter.js
│   │
│   ├── styles/
│   │   ├── main.css
│   │   ├── buyer.css
│   │   └── login.css
│   │
│   └── assets/               
│       ├── images/
│       └── icons/
│
├── data/
│   ├── district.json
│   └── locations.json
│
└── architectural_diagrams/
    └── class_diagram.jpg
```
installation, goes by cloning the repository
and 
```
git clone https://github.com/ishami-i/farmers_conekt
bash ./set_up.sh
```
### 7. User Experience
-------------------

* Farmers can create accounts, upload products, and manage orders through an intuitive dashboard.  
* Buyers can browse products, search, place orders, and make payments seamlessly.  
* Transporters receive delivery requests and manage logistics efficiently.  
* The platform provides a clean and responsive interface for both mobile and web users.  

---

### 8. Data & Security
-------------------

* User authentication and authorization ensure that only registered users can access the platform.  
* Role-based access control is implemented for farmers, buyers, and transporters.  
* Secure payment processing is handled through Flutterwave with encrypted transactions.  
* Sensitive user data is protected using encryption and secure storage practices.  
* Input validation and sanitization are applied to prevent vulnerabilities such as SQL injection and XSS.  
* Secure communication is enforced using HTTPS for all data exchanges.

---

### 9. Demo Links
-------------------
* For the demo video, check this link: https://youtu.be/2O-4wheTZtc
* For the Demo website: https://farmers-conekt.ineza.tech/
---

### 10. Team
--------

* Ishami Irené — https://github.com/ishami-i  
* Kevin Ineza — https://github.com/inezakevin23  
* Dedine Mukabucyana — https://github.com/Dedine-Mukabucyana  
* Milliam Mukamukiza — https://github.com/mmukamukiza21  
* Nganji Jospin — https://github.com/Nganji1  
