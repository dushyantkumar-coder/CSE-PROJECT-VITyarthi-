# Problem Statement: Flight Booking System Modernization

  * Project: Python Console Flight Booking System Prototype (Reference Code Provided)
  * Target Platform: Collaborative Development via GitHub

# Background

The attached Python code represents a minimal, single-file console application designed to demonstrate basic flight booking logic, including flight listing, search, cart management, and a simulated checkout process. This application currently serves as a functional proof-of-concept (PoC).

# The Problem

The current Flight Booking System prototype suffers from critical limitations that prevent its deployment and scale as a real-world service:

Lack of Data Persistence (Database): The flight data (flights dictionary) and user cart data (cart_flights, cart_prices) are stored entirely in memory. Every time the application is closed, all changes, bookings, and flight availability updates are lost.

No Multi-User Support: The application is designed for a single, local user experience. It cannot handle concurrent operations, separate user sessions, or manage state (e.g., booked seats) across multiple users, making it unusable as a commercial platform.

Inefficient Search and Logic: Functions like search_flights() rely on iterating through a hardcoded dictionary. This approach is unscalable and inefficient for a large volume of real-time flight data. Furthermore, the checkout() function does not actually deduct seats from the flights database, leading to overbooking issues.

Poor User Experience (UX): As a command-line interface (CLI) application, it is non-intuitive, lacks visual feedback, and cannot support complex inputs or rich media, limiting accessibility and usability.

The Collaboration Challenge (The Need for GitHub)

The existing single-file codebase provides no mechanism for simultaneous development, feature isolation, or quality assurance. Without a version control system and collaborative platform, any attempt to fix the above issues (e.g., adding a database, building a web UI) will lead to chaotic code integration, difficulty in tracking bugs, and no formal method for code review or release management.

# Goal

The primary goal is to transform the existing Python PoC into a modular, persistent, and scalable application.

* Key Objectives:

Implement Persistence: Integrate a persistent database solution (e.g., SQL or NoSQL) to store and manage flight inventory and booking records reliably.

Develop a Web Interface: Replace the CLI with a modern, responsive user interface (using a framework like Flask/Django or React/Angular) for enhanced UX.

Establish Scalable Architecture: Refactor the monolithic script into decoupled modules (e.g., data access layer, business logic layer, presentation layer) to support future feature expansion and maintenance.

Enable Collaboration and Auditing: Use GitHub for all development activities, including feature branching, pull requests for code review, and issue tracking to document and resolve bugs related to the new features.

# Success Criteria

A successful outcome will be a system where:

Flight and booking data persists after application closure.

Users can book flights, and the seat count is reliably decremented in the inventory.

A minimum viable product (MVP) web interface allows users to perform all existing functions (View, Search, Add to Cart, Checkout).

All development is managed through Git (version control) and hosted on GitHub, ensuring a clear history, traceability, and a robust environment for team collaboration.
