# Puddle Marketplace 

![Puddle Marketplace Frontpage]([url_to_your_image.png](https://drive.google.com/drive/u/0/folders/1WNj7P5wWFwQ_sxF0KckPn-0K2e3Hbg4T))

## Introduction
Puddle Marketplace is an online platform designed for buying and selling used or second-hand items. This simple documentation outlines the functionality, architecture, and technologies used to create this marketplace, which serves as a valuable addition to my portfolio. Built with a technology stack encompassing Python, Django, Tailwind CSS, JavaScript, HTML, Git, and GitHub, Puddle Marketplace offers users a seamless experience for discovering, listing, and interacting with items of interest.

## Apps

### Core
- The Core app acts as the foundation, providing a consistent layout across the entire website.
- The user interface includes a fixed navbar at the top, featuring a logo, title, and navigation buttons.
- Dynamic buttons are displayed based on user authentication status, facilitating actions like item addition, search, sign-up, log-in, inbox access, and profile management.
- A footer contains essential links like About, Contact, Privacy Policy, Terms Of Use, FAQ, and Product Listing Policy.
- Scroll-to-top button allows users to return to the page's beginning smoothly.
- Previous page button enables easy navigation backward.
- The index page showcases the latest items and incorporates advertisements using JavaScript-powered image rotation.
- Items are displayed in rows, and categories offer filterable options to explore specific item types.

### Profile
- The Profile app enables users to personalize their profiles, including adding avatars, locations, and bios.
- Users can delete their profiles, with automatic profile creation upon sign-up.
- Login and Logout functionalities are integrated using Django's authentication system.

### Dashboard
- The Dashboard app provides a dedicated space for users to manage their listed items.
- It displays all items owned by the logged-in user and allows for quick navigation to item details.

### Items
- The Items app hosts item-related models and the detail page layout.
- The detail page showcases key information such as images (with JavaScript-enabled enlarging), item name, price, seller details, and descriptions.
- User-specific options are dynamically displayed, offering edit and delete functions for owned items, or profile and contact options for other items.
- Item details also present related items from the same category.

### Conversation
- The Conversation app facilitates communication between users.
- Users can access their conversations through the inbox.
- Users can engage in ongoing discussions, with rich-text messaging via CKEditor.

## Tools, Frameworks, and Technologies Used
- **Python:** The primary programming language used for backend logic and scripting.
- **Django:** A powerful web framework that handles routing, authentication, and database interactions.
- **Tailwind CSS:** A user-friendly CSS framework aiding in consistent and responsive design.
- **JavaScript:** Used for dynamic behavior like scroll-to-top, image rotation, and interactive UI elements.
- **HTML:** The foundational markup language for constructing the website's structure.
- **Git & GitHub:** Version control system and collaborative platform for tracking and sharing code changes.

## Conclusion
Puddle Marketplace showcases my expertise in web development, utilizing a diverse tech stack to create a user-friendly online marketplace for buying and selling used items. The structure, features, and technologies implemented highlight my skills in Python, Django, Tailwind CSS, JavaScript, HTML, and effective version control with Git and GitHub and SQLite database.
