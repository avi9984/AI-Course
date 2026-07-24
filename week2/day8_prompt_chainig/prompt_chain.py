from groq import Groq
import os;
from pathlib import Path;
from dotenv import load_dotenv
from time import sleep

load_dotenv();

my_api_key=os.getenv("GROK_API_KEY");


if not my_api_key:
    raise ValueError("API key not found");

client=Groq(api_key=my_api_key);

model="llama-3.3-70b-versatile";

JD="""
Enterprise Bot is the leading provider of GenAI, Conversational AI, and automation software, headquartered in Zurich, Switzerland. Our intelligent virtual assistants and automation tools help organizations improve efficiency, reduce costs, and deliver exceptional customer experiences across industries such as banking, insurance, and logistics. Our mission is to become the world’s #1 AI-driven automation software provider within the next five years.


We work with leading companies such as the SIX Group (Swiss Stock Exchange), SWICA, Generali, and others to enhance customer interactions and automate business processes using our cutting-edge Conversational AI technology.


Our global team includes more than 70 highly skilled professionals from diverse backgrounds.


We foster an open, progressive company culture with state-of-the-art technology and flat hierarchies. At Enterprise Bot, you’ll experience a unique blend of passion, purpose, challenge, and fun.


Tasks
We are looking for a Senior Node.js Backend Engineer with 3–5 years of hands-on experience building scalable, high-performance backend systems. In this role, you will architect and develop robust APIs, design efficient database structures, and contribute to AI-powered and agent-based systems.


You will work on modern backend architectures that power intelligent applications, including AI integrations, LLM-driven workflows, streaming systems, and real-time services. This role requires strong ownership, system design thinking, and a passion for building secure, production-grade solutions.


You will collaborate closely with cross-functional teams to deliver scalable, reliable, and innovative software aligned with industry best practices.


Key Responsibilities:


Backend Development:



Design, develop, and maintain scalable server-side applications using Node.js.

Leverage frameworks such as Express.js and Koa for efficient API and application development.


Database Management:



Work extensively with MongoDB for schema design, indexing, and optimising query performance.

Utilize SQL-based databases when needed to meet project requirements.


API Development & Integration:



Build secure, efficient, and reusable RESTful and/or GraphQL APIs to facilitate seamless communication between systems.

Implement authentication systems using frameworks like OAuth, JWT, and others to ensure robust access control.


Security & Data Protection:



Implement security and data protection best practices in APIs, data flows, and database design.

Ensure systems are designed to protect sensitive user and organizational data.


Troubleshooting & Support:



Identify, debug, and resolve production issues to ensure a seamless user experience.

Monitor performance and scalability, addressing bottlenecks as they arise.


Collaboration & Documentation:



Collaborate with front-end developers, designers, and other team members to integrate front-end elements with server-side logic.

Document code, APIs, and database schemas to maintain clarity and facilitate knowledge sharing.


Requirements
Education:



Bachelor’s degree in Computer Science, Information Technology, or a related field.


Experience:



3-5 years of professional experience in backend development using Node.js and MongoDB.

Proficiency in SQL-based databases (e.g., MySQL, PostgreSQL) in addition to MongoDB.


Technical Skills:


Strong proficiency in JavaScript (ES6+) and asynchronous programming:



Deep understanding of modern JavaScript features, including promises, async/await, modules, closures, and event-driven patterns.

Comfortable handling concurrency, non-blocking I/O, and performance optimization in Node.js environments.


Experience with Express.js and Koa:



Ability to design and build scalable APIs, implement middleware, manage routing, structure applications cleanly, and handle validation and error management effectively.


Hands-on experience in database schema design, query optimization, and indexing:



Experience designing efficient schemas, optimizing queries, analyzing execution plans, and implementing indexing strategies to ensure performance and scalability.


Familiarity with authentication and authorization systems, including OAuth and JWT:



Experience implementing secure authentication flows, token-based authentication, role-based access control, and understanding common web security best practices.


Proven ability to diagnose and resolve production issues:



Comfortable debugging live systems, analyzing logs and metrics, identifying root causes, and deploying fixes with minimal disruption.


Experience with media streaming systems:



Familiarity with real-time audio/video streaming concepts, streaming protocols, low-latency architectures, or handling high-throughput media pipelines


Experience with voice systems:



Exposure to voice processing workflows such as speech-to-text, text-to-speech, VoIP integrations, or real-time communication systems.


Experience working with AI systems:



Integration of machine learning models or LLM APIs, handling inference workflows, prompt orchestration, or building AI-powered backend services.


Experience building agent-based systems:



Designing autonomous or semi-autonomous agents, tool orchestration, workflow automation, state management for multi-step reasoning, or event-driven intelligent systems.


Security & Best Practices:



Knowledge of security best practices for APIs and backend systems, including data protection, encryption, and secure API design.


Testing & Debugging:



Strong understanding of testing frameworks such as Jest, Mocha, or Chai for unit and integration testing.


Version Control & Deployment:



Proficiency in Git for source control and collaboration.

Experience with CI/CD pipelines, cloud platforms (AWS, Azure, or GCP), and containerization tools (Docker/Kubernetes) is a plus.


Preferred Skills:



Familiarity with microservices architecture and event-driven systems.

Experience working with Agile/Scrum methodologies.

Exposure to caching mechanisms such as Redis.


Benefits

Be part of a rapidly growing company at the forefront of AI automation and conversational AI solutions used by leading global enterprises.

Shape solutions that make a measurable impact for Fortune 500 clients and leading European enterprises.

A culture comprised of diverse, global teams who have a passion for collaboration, creativity, and excellence in client service

A competitive salary and scope for further advancement.

A great environment that promotes open feedback and a flat hierarchy, working at Enterprise Bot is a refreshing mix of purpose, challenge, and fun.
"""

RESUME="""
Avinash Kumar
+91 7652084062 | Mumbai,India| avinashkumar151199@gmail.com | linkedin.com/in/avi9984 | github.com/avi9984
Professional Summary
Backend Software Engineer with 4.2 years of experience specializing in building scalable systems using Node.js, TypeScript,
GraphQL, and PostgreSQL. Demonstrated expertise in REST APIs, event-driven architecture, and Salesforce CPQ
integrations, with a strong focus on cloud infrastructure using AWS and Azure. Proven track record in optimizing performance,
implementing automation, integrating AI, and ensuring system reliability across Web3, ERP, and CPQ domains.
Experience
Sigma Solve, Inc.
Software Engineer– Backend (Node.js, TypeScript, Next.js API Routes, PostgreSQL, Azure)
Jan 2025– Mar 2026
Pune, Remote
• Built scalable backend services using Node.js, TypeScript, and Next.js API Routes, integrating Salesforce CPQ for
complex multi-tier pricing workflows and automated quote generation at scale.
• Designed high-performance REST APIs for bulk Excel/CSV data processing, improving pricing efficiency by 30%+
engineered secure file pipelines via Azure Blob Storage with signed URLs.
• Automated workflows using pg cron and webhooks, reducing manual backend operations by 40%; implemented event-driven
architecture for real-time Salesforce CRM ↔ Supabase/PostgreSQL sync.
Biz Technologies IT Solutions
Node.js Backend Developer (Node.js, Express.js, MongoDB, Web3, IPFS, AWS, React)
Mar 2023– Dec 2024
Mumbai
• Architected full backend for a Web3 marketplace supporting NFT trading, virtual land ownership, and digital asset
transactions with smart contract integration on the blockchain.
• Developed decentralized REST APIs for scalable asset discovery, transaction processing, and ownership verification, inspired
by patterns from large-scale virtual ecosystems like Decentraland.
• Integrated IPFS with MongoDB for a hybrid storage layer– IPFS for immutable asset data, MongoDB for structured
metadata– and optimized queries to reduce API response time by 10–15%.
• Led end-to-end backend ownership of asset lifecycle including minting, transfers, rental logic, and marketplace transactions with
full blockchain and database consistency.
Red Roots India Pvt. Ltd
Node.js Backend Developer (Node.js, Express.js, PostgreSQL, GraphQL)
Apr 2022– Mar 2023
Mumbai
• Built and maintained scalable ERP backend systems using Node.js and PostgreSQL covering HR, sales, inventory, and
vendor operations for a mid-sized enterprise client.
• Developed an automated expense management module with multi-level approval workflows, reducing HR processing
workload by 20% and improving finance team visibility.
• Improved overall API performance by 20% through targeted query optimization, strategic indexing, and response caching,
resulting in faster page loads and better UX.
• Implemented role-based access control (RBAC) and secure JWT-based authentication, ensuring fine-grained authorization
across all ERP modules and protecting sensitive employee data.
Key Projects
Wildeck.com– CPQ Sync System
Node.Js, Next.js API Router, TypeScript, PostgreSQL, Supabase, Azure
• Engineered a 12-step Quote Sync Engine integrating Salesforce CPQ with Supabase, handling complex pricing rules, quote
versioning, and multi-system data reconciliation in real time; automated email notifications via Resend API for quote lifecycle
events and send the product price.
• Built webhook-based event architecture for automated sync and bulk Excel/CSV import pipelines with field
validation, mapping, and error handling to support large-scale pricing data operations.
Decentrawood– Web3 Marketplace & Game
Node.js, Express.js, MongoDB, Web3, IPFS, React, Unity
• Developed full backend for a decentralized NFT marketplace supporting buying, selling, and renting of virtual lands and
digital assets with on-chain transaction integrity and ownership transfer.
• Built game backend services for scoring, reward distribution, and real-time inventory management supporting concurrent
multi-user gameplay across a fully decentralized architecture.
Technical Skills
• Languages & Runtime: JavaScript (ES6+), TypeScript, Node.js, Next.js (API Routes)
• Backend Frameworks & APIs: Express.js, NestJS, GraphQL (Apollo Server), REST API Design, Webhooks, GraphQL API
• Databases: MongoDB(Mongoose Odm), PostgreSQL Supabase, Redis (caching), Query Optimization, Indexing
• Cloud & DevOps: AWS (EC2, IAM), Azure Blob Storage, Docker, Git, GitHub, Jest, Mocha
• Architecture & Concepts: Event-Driven Architecture, System Design, RBAC, Salesforce CPQ, Web3/IPFS, pg cron, JWT
Authentication, API Security
Education
B.Tech in Computer Science Engineering
Seth Vishambhar Nath Institute of Engineering & Technology, Uttar Pradesh, India
2016– 2020
Relevant Coursework: Data Structures & Algorithms, DBMS, Operating Systems, Computer Networks, OOP, Software
"""

def ask_llm(system_prompt, user_prompt):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
    response = client.chat.completions.create(model=model, messages=messages)
    return response.choices[0].message.content


# these are now top-level functions, not nested inside ask_llm
def step1_resume_extract():
    system_prompt = "You are a professional HR assistant. Extract the skills from the candidate's resume provided. Only return the skills, no other information. Do not invent any skills yourself. Just extract the skills as they are."
    user_prompt = f"Extract the skills from this resume:\n{RESUME}"
    return ask_llm(system_prompt, user_prompt)


def step2_JD_extract():
    system_prompt = "You are a professional HR assistant. Extract the key requirements from the Job Description provided."
    user_prompt = f"Extract the requirements from this Job Description:\n{JD}"
    return ask_llm(system_prompt, user_prompt)


def step3_match(jd, candidate):
    system_prompt = "You are a professional HR assistant. Match the skills extracted from the resume with the Job Description provided. Produce a final score between 0-100. Also produce a short verdict with 2-3 sentences on why the candidate is a good match or not."
    user_prompt = f"Compare and match the skills.\nJD:\n{jd}\nCandidate:\n{candidate}"
    return ask_llm(system_prompt, user_prompt)


# if __name__ == "__main__":
candidate = step1_resume_extract()
sleep(2)
jd = step2_JD_extract()
sleep(2)
score = step3_match(jd, candidate)   # order matches step3_match(jd, candidate)
print(score)