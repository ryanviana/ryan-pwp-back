#!/usr/bin/env python3
import requests
import json
import time
import sys

# Base URL for the API
BASE_URL = "http://localhost:3003"  # Assuming default NestJS port

# Increase timeout and retry settings for requests
requests_timeout = 10
max_retries = 3


# Check if server is reachable
def check_server_connection():
    """Check if the server is reachable"""
    print("Checking connection to server...")
    try:
        response = requests.get(f"{BASE_URL}", timeout=requests_timeout)
        if response.status_code == 200:
            print(f"Server is up and running at {BASE_URL}")
            return True
        else:
            print(f"Server returned status code: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to server: {str(e)}")
        return False


# Add retry functionality for API calls
def make_api_request(method, url, json=None, timeout=requests_timeout):
    """Make an API request with retries"""
    for attempt in range(max_retries):
        try:
            if method.lower() == "get":
                response = requests.get(url, timeout=timeout)
            elif method.lower() == "post":
                response = requests.post(url, json=json, timeout=timeout)
            elif method.lower() == "delete":
                response = requests.delete(url, timeout=timeout)
            else:
                raise ValueError(f"Unsupported method: {method}")

            return response
        except requests.exceptions.RequestException as e:
            if attempt < max_retries - 1:
                wait_time = 2**attempt  # Exponential backoff
                print(f"Request failed. Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                raise e


# Full blog post data
blog_posts = [
    {
        "slug": "blockchain-in-healthcare",
        "title": "Revolutionizing Healthcare with Blockchain Technology",
        "date": "2024-05-15",
        "excerpt": "Exploring how blockchain technology is transforming the healthcare industry by improving data security, patient privacy, and medical record management.",
        "coverImage": "/blog-placeholder-1.jpg",
        "readingTime": "5 min read",
        "tags": ["Blockchain", "Healthcare", "Technology"],
        "content": """
# Revolutionizing Healthcare with Blockchain Technology

Healthcare is one of the industries that stands to benefit most from blockchain technology. With its ability to securely store and share sensitive data, blockchain can address many of the challenges facing healthcare today.

## Enhancing Data Security and Privacy

One of the most significant advantages of blockchain in healthcare is improved security. Patient data stored on a blockchain is encrypted and can only be accessed by authorized parties with the correct private keys. This ensures that sensitive medical information remains private and protected from unauthorized access or data breaches.

## Streamlining Medical Record Management

Medical records stored on a blockchain can be accessed across different healthcare providers, eliminating the need for patients to carry physical copies of their records or fill out redundant paperwork. This seamless sharing of information can lead to better coordination of care and reduced administrative costs.

## Smart Contracts for Insurance Claims

Smart contracts on blockchain platforms can automate insurance claims processing, making it faster and more efficient. These self-executing contracts can verify policy terms, validate claims, and trigger payments automatically when predefined conditions are met, reducing the need for manual intervention and minimizing disputes.

## Challenges and Future Directions

Despite its potential, blockchain adoption in healthcare faces challenges such as regulatory compliance, integration with existing systems, and the need for standardization. However, as the technology matures and these issues are addressed, blockchain is poised to become an integral part of the healthcare ecosystem.

In conclusion, blockchain technology offers promising solutions to many of the challenges in healthcare, from data security to efficient record-keeping and claims processing. As healthcare organizations continue to explore and implement blockchain solutions, we can expect to see significant improvements in the quality, accessibility, and cost-effectiveness of healthcare services.
        """,
        "relatedPosts": [
            {
                "slug": "web3-development-guide",
                "title": "A Comprehensive Guide to Web3 Development",
                "coverImage": "/blog-placeholder-2.jpg",
            },
            {
                "slug": "defi-explained",
                "title": "DeFi Explained: Understanding Decentralized Finance",
                "coverImage": "/blog-placeholder-3.jpg",
            },
        ],
    },
    {
        "slug": "web3-development-guide",
        "title": "A Comprehensive Guide to Web3 Development",
        "date": "2024-04-23",
        "excerpt": "A beginner-friendly introduction to Web3 development, covering essential tools, frameworks, and best practices for building decentralized applications.",
        "coverImage": "/blog-placeholder-2.jpg",
        "readingTime": "8 min read",
        "tags": ["Web3", "Blockchain", "Development", "Tutorial"],
        "content": """
# A Comprehensive Guide to Web3 Development

Web3 represents the next evolution of the internet, moving from centralized platforms to decentralized, user-owned networks and applications. This guide will help you get started with Web3 development.

## Understanding Web3 Fundamentals

At its core, Web3 is built on blockchain technology, enabling trustless transactions and interactions without intermediaries. Key concepts include decentralization, cryptographic security, and token economics. Familiarizing yourself with these fundamentals is essential before diving into development.

## Essential Tools for Web3 Development

Several tools have emerged as standards in the Web3 development ecosystem:

- **Ethereum Development Environment**: Tools like Hardhat, Truffle, and Foundry provide frameworks for developing, testing, and deploying smart contracts.
- **Web3.js and Ethers.js**: JavaScript libraries that allow interaction with the Ethereum blockchain.
- **IPFS**: A distributed system for storing and accessing files, websites, applications, and data.
- **MetaMask**: A crypto wallet and gateway to blockchain apps, essential for testing your applications.

## Building Your First Decentralized Application (dApp)

A typical dApp consists of:

1. **Smart Contracts**: Written in Solidity (for Ethereum) or other blockchain-specific languages, these are the backend of your application.
2. **Frontend Interface**: Usually built with React, Next.js, or other modern JavaScript frameworks.
3. **Web3 Integration**: Using libraries like Web3.js or Ethers.js to connect your frontend to the blockchain.

## Best Practices and Considerations

- **Security First**: Smart contracts are immutable once deployed, so security is paramount. Consider audit services and follow established patterns.
- **Gas Optimization**: Efficient code reduces transaction costs for users.
- **User Experience**: Bridge the gap between traditional web applications and blockchain technology with intuitive interfaces.
- **Testing**: Thoroughly test your applications in test networks before mainnet deployment.

## The Future of Web3 Development

The Web3 ecosystem is rapidly evolving, with new chains, scaling solutions, and interoperability protocols emerging regularly. Staying informed and adaptable is key to success in this exciting field.

Whether you're building the next NFT marketplace, a DeFi protocol, or a decentralized social network, the principles and tools outlined in this guide will provide a solid foundation for your Web3 development journey.
        """,
        "relatedPosts": [
            {
                "slug": "blockchain-in-healthcare",
                "title": "Revolutionizing Healthcare with Blockchain Technology",
                "coverImage": "/blog-placeholder-1.jpg",
            },
            {
                "slug": "defi-explained",
                "title": "DeFi Explained: Understanding Decentralized Finance",
                "coverImage": "/blog-placeholder-3.jpg",
            },
        ],
    },
    {
        "slug": "defi-explained",
        "title": "DeFi Explained: Understanding Decentralized Finance",
        "date": "2024-03-10",
        "excerpt": "Breaking down the complex world of Decentralized Finance (DeFi), its key protocols, potential benefits, and the risks involved for investors and developers.",
        "coverImage": "/blog-placeholder-3.jpg",
        "readingTime": "6 min read",
        "tags": ["DeFi", "Blockchain", "Finance", "Cryptocurrency"],
        "content": """
# DeFi Explained: Understanding Decentralized Finance

Decentralized Finance, or DeFi, has emerged as one of the most promising applications of blockchain technology, aiming to recreate and improve traditional financial systems using decentralized networks.

## What is DeFi?

DeFi refers to a ecosystem of financial applications built on blockchain networks that eliminate the need for traditional intermediaries like banks and brokerages. Instead, smart contracts automatically execute transactions based on predefined conditions, creating an open, permissionless financial system accessible to anyone with an internet connection.

## Key Components of the DeFi Ecosystem

### 1. Lending and Borrowing Platforms

Platforms like Aave and Compound allow users to lend their crypto assets to earn interest or borrow against their holdings. Unlike traditional banking, these transactions occur peer-to-peer, without a central authority.

### 2. Decentralized Exchanges (DEXs)

DEXs like Uniswap and SushiSwap enable direct trading between users without a central exchange holding the funds. They use automated market makers (AMMs) to determine prices based on mathematical formulas.

### 3. Stablecoins

These are cryptocurrencies designed to maintain a stable value, often pegged to a fiat currency like the US dollar. Examples include DAI and USDC, which provide stability in the volatile crypto market.

### 4. Yield Farming

This involves strategies to maximize returns by leveraging various DeFi protocols, often by providing liquidity to different platforms in exchange for rewards.

## Benefits and Risks

### Benefits:
- Financial inclusion for the unbanked
- Transparency and auditability
- Reduced costs through automation
- Composability allowing for innovation

### Risks:
- Smart contract vulnerabilities
- Market volatility
- Regulatory uncertainty
- Complexity for new users

## The Future of DeFi

As the space matures, we can expect improved user interfaces, better regulatory clarity, and increased institutional adoption. The innovation in DeFi continues at a rapid pace, with new protocols and applications emerging regularly.

Whether you're a developer, investor, or simply curious about the future of finance, understanding DeFi is increasingly important in our digital world.
        """,
        "relatedPosts": [
            {
                "slug": "blockchain-in-healthcare",
                "title": "Revolutionizing Healthcare with Blockchain Technology",
                "coverImage": "/blog-placeholder-1.jpg",
            },
            {
                "slug": "web3-development-guide",
                "title": "A Comprehensive Guide to Web3 Development",
                "coverImage": "/blog-placeholder-2.jpg",
            },
        ],
    },
]

# Work experiences with all fields
work_experiences = [
    {
        "title": "Cofounder",
        "company": "Prisma Tech",
        "location": "São Carlos, São Paulo, Brazil",
        "startDate": "January 2024",
        "endDate": "Present",
        "description": [
            "Co-founded a technology startup focused on developing innovative software solutions",
            "Leading the development of AI-powered tools for the Brazilian market",
            "Recently pivoted from the education sector to building an AI-driven SDR solution",
            "Implementing integrations with WhatsApp and other communication channels",
        ],
    },
    {
        "title": "Software Development Intern",
        "company": "EloGroup",
        "location": "Remote",
        "startDate": "March 2022",
        "endDate": "December 2023",
        "description": [
            "Led backend development for a major application at the Secretary of Treasury of Ceará using Java Spring Boot and PostgreSQL",
            "Collaborated with multidisciplinary teams across business, data engineering, and technology",
            "Developed robust and scalable digital solutions for the government sector",
            "Implemented RESTful APIs and integrated with various data sources",
        ],
    },
    {
        "title": "Summer Internship",
        "company": "EloGroup",
        "location": "Remote",
        "startDate": "January 2022",
        "endDate": "February 2022",
        "description": [
            "Performed Business Process Transformation activities including mapping business processes and identifying pain points",
            "Used Microsoft Office tools and Bizagi for process modeling",
            "Received training in consulting skills like storytelling, efficient information extraction, and client communication practices",
        ],
    },
    {
        "title": "Team Manager",
        "company": "Centro Acadêmico Armando de Salles Oliveira - CAASO",
        "location": "São Carlos, São Paulo, Brazil",
        "startDate": "September 2021",
        "endDate": "March 2022",
        "description": [
            "Managed a five-person team at CAASO Idiomas, a non-profit language school",
            "Directed projects to improve class quality and increase student and teacher numbers",
            "Established a scholarship program offering 50-100% discounts for socioeconomically vulnerable individuals",
        ],
    },
    {
        "title": "Member",
        "company": "Centro Acadêmico Armando de Salles Oliveira - CAASO",
        "location": "São Carlos, São Paulo, Brazil",
        "startDate": "September 2020",
        "endDate": "September 2021",
        "description": [
            "Maintained operations of CAASO Idiomas as the only active member for a year",
            "Created advertising campaigns, managed student registrations, and handled financial transactions",
            "Developed automated solutions using Google Apps Script (JavaScript) to streamline repetitive tasks",
            "Integrated Google services like Sheets, Contacts, Docs, and Gmail to improve operational efficiency",
        ],
    },
    {
        "title": "Software Developer",
        "company": "VOICE Language School",
        "location": "Guaxupé, Minas Gerais, Brazil",
        "startDate": "February 2020",
        "endDate": "May 2020",
        "description": [
            "Developed an integrated solution between Google services using a cloud-based JavaScript platform",
            "Created a form-based data input system that fed into a spreadsheet database and triggered automatic functions",
            "Implemented management solutions for inventory, library, and student reporting using spreadsheets as the core",
            "Designed user interfaces and provided training for school employees on using the new system",
        ],
    },
]

# Achievements with all fields
achievements = [
    {
        "title": "1st Place | TRACTIAN HACKATHON - UFSCAR - SEMCOMP 2024",
        "organization": "Tractian",
        "date": "October 2024",
        "description": "Won 1st place at the TRACTIAN Hackathon by developing TracBot, an AI chatbot trained with industry-specific information designed to solve real challenges and foster innovation in the industrial sector.",
    },
    {
        "title": "Cartesi Online Hackathon | Prize Pool Winner",
        "organization": "Cartesi",
        "date": "March 2024",
        "description": "Our project 'The Prism' earned $1000 from the shared pool prize. The Prism is a personalized t-shirt marketplace using stable-diffusion models and Cartesi VM, combining AI with blockchain technology for a unique consumer experience in the Ethereum ecosystem.",
    },
    {
        "title": "ETH Samba Hackathon | Chainlink & Buidl Guidl Awards",
        "organization": "ETH Samba",
        "date": "March 2024",
        "description": "Won in both the Chainlink and Buidl Guidl categories at ETH Samba in Rio de Janeiro, receiving a total prize of $1500, demonstrating innovation and excellence in the blockchain space.",
    },
    {
        "title": "Starknet Winter Hackathon | Elite Runner-Up",
        "organization": "Starknet",
        "date": "February 2024",
        "description": "Our project 'Starknet MAC' was runner-up in the StarkWare Global Track, earning $500. Starknet MAC is a marketplace connecting advertisers with creators, enabling deals and cross-border payments using cryptocurrency within the StarkNet ecosystem.",
    },
    {
        "title": "1st Place | XRP Ledger Hackathon Brasil 2024",
        "organization": "Ripple",
        "date": "January 2024",
        "description": "Project 'XRP Overnight' won 1st place in the Finance category at the XRP Ledger Hackathon Brazil, securing a prize of $2,000. The event gathered Brazilian developers to work with XRP Ledger mainnet and EVM-Sidechain.",
    },
    {
        "title": "2nd Place | Hackathon Web3: National Treasury Tokenization 2023",
        "organization": "Tesouro Nacional",
        "date": "December 2023",
        "description": "Secured 2nd place with a prize of R$ 6,000. The project developed an innovative application for tokenized treasury bonds used for granting guarantees with titles as collateral, enabling interoperability among banks that custody these titles.",
    },
    {
        "title": "1st Place | Zencon Hackathon 2023",
        "organization": "Zencon",
        "date": "September 2023",
        "description": "Won 1st place at ZENCON with a $20,000 award in the ZENIQ Evolution category, developing an innovative blockchain application on the ZENIQ Smart Chain.",
    },
    {
        "title": "1st Place | Digital Bootcamp 2021",
        "organization": "EloGroup",
        "date": "October 2021",
        "description": "Participated in the Technology frame of EloGroup Digital Bootcamp, consuming over 40 hours of content on Cloud Native Development, Software Engineering, and RPA before solving a real case problem in a team.",
    },
]

# Education with all fields
education = [
    {
        "degree": "Computer Engineering",
        "institution": "Universidade de São Paulo",
        "startYear": "2020",
        "endYear": "2024",
    }
]

# Complete projects data with all fields
projects = [
    {
        "title": "E-commerce Platform",
        "description": "A full-stack e-commerce platform built with Next.js, Node.js, and MongoDB.",
        "fullDescription": "This e-commerce platform provides a seamless shopping experience with features like user authentication, product catalog, shopping cart, payment processing, and order management. The frontend is built with Next.js and styled with Tailwind CSS, while the backend uses Node.js with Express and MongoDB for data storage.",
        "image": "/project-placeholder-1.jpg",
        "tags": ["Next.js", "Node.js", "MongoDB", "Tailwind CSS"],
        "slug": "ecommerce-platform",
        "demoUrl": "https://example.com/demo",
        "githubUrl": "https://github.com/example/ecommerce",
        "features": [
            "User authentication and profile management",
            "Product catalog with search and filtering",
            "Shopping cart and checkout flow",
            "Payment processing integration",
            "Order history and tracking",
            "Admin dashboard for product management",
        ],
        "featured": True,
    },
    {
        "title": "Weather Dashboard",
        "description": "A weather dashboard app that displays current and forecasted weather using a third-party API.",
        "fullDescription": "This weather dashboard application allows users to search for any city and view current weather conditions as well as a 5-day forecast. It leverages the OpenWeatherMap API to fetch weather data and displays it in a user-friendly interface. The app includes features like location search, unit conversion, and weather visualization using charts.",
        "image": "/project-placeholder-2.jpg",
        "tags": ["React", "Weather API", "Chart.js", "CSS Modules"],
        "slug": "weather-dashboard",
        "demoUrl": "https://example.com/weather",
        "githubUrl": "https://github.com/example/weather",
        "features": [
            "City search with autocomplete",
            "Current weather conditions display",
            "5-day weather forecast",
            "Temperature, humidity, and wind speed charts",
            "Unit conversion (Celsius/Fahrenheit)",
            "Location-based weather detection",
        ],
        "featured": True,
    },
    {
        "title": "Task Management App",
        "description": "A task management application with drag-and-drop functionality and user authentication.",
        "fullDescription": "This task management application helps users organize their work with features like task creation, categorization, priority setting, and due date tracking. The app includes a drag-and-drop interface for easy task organization across different status columns. User authentication ensures that each user has access to only their tasks, and real-time updates are implemented using Firebase.",
        "image": "/project-placeholder-3.jpg",
        "tags": ["TypeScript", "React", "Firebase", "Redux"],
        "slug": "task-management-app",
        "demoUrl": "https://example.com/tasks",
        "githubUrl": "https://github.com/example/tasks",
        "features": [
            "User authentication and account management",
            "Task creation with title, description, priority, and due date",
            "Drag-and-drop interface for status updates",
            "Categorization and tagging of tasks",
            "Task filtering and search functionality",
            "Due date notifications and reminders",
        ],
        "featured": True,
    },
    {
        "title": "Fitness Tracking App",
        "description": "A fitness tracking application that allows users to record and analyze their workouts.",
        "fullDescription": "This fitness tracking app enables users to record various types of workouts, track their progress over time, and set fitness goals. The app provides visualizations of workout data, allowing users to see improvements and identify areas for growth. Features include workout logging, progress tracking, goal setting, and social sharing.",
        "image": "/project-placeholder-4.jpg",
        "tags": ["React Native", "TypeScript", "Firebase", "Chart.js"],
        "slug": "fitness-tracking-app",
        "githubUrl": "https://github.com/example/fitness",
        "features": [
            "Workout logging with exercise details",
            "Progress tracking over time",
            "Goal setting and achievement tracking",
            "Data visualization with charts and graphs",
            "Social sharing of achievements",
            "Workout recommendations based on history",
        ],
        "featured": False,
    },
    {
        "title": "Recipe Sharing Platform",
        "description": "A platform for food enthusiasts to discover, share, and save recipes.",
        "fullDescription": "This recipe sharing platform allows users to discover new recipes, share their own creations, and build a collection of favorites. The platform includes features like recipe search, categorization by cuisine and dietary preferences, ingredient-based search, and social sharing. Users can create profiles, follow other cooks, and save recipes to their personal collections.",
        "image": "/project-placeholder-5.jpg",
        "tags": ["Vue.js", "Node.js", "MongoDB", "Vuetify"],
        "slug": "recipe-sharing-platform",
        "demoUrl": "https://example.com/recipes",
        "githubUrl": "https://github.com/example/recipes",
        "features": [
            "Recipe creation with ingredients and instructions",
            "Recipe search by title, ingredients, or cuisine",
            "Filtering by dietary preferences and cooking time",
            "User profiles and collections",
            "Social features including likes and comments",
            "Meal planning and grocery list generation",
        ],
        "featured": False,
    },
    {
        "title": "Portfolio Website Template",
        "description": "A customizable portfolio website template for developers and designers.",
        "fullDescription": "This portfolio website template provides developers and designers with a professional, customizable platform to showcase their work. Built with Next.js and styled with Tailwind CSS, the template includes sections for projects, skills, experience, and contact information. It's designed to be easy to modify and deploy, with a focus on performance, accessibility, and SEO.",
        "image": "/project-placeholder-6.jpg",
        "tags": ["Next.js", "TypeScript", "Tailwind CSS", "Framer Motion"],
        "slug": "portfolio-website-template",
        "demoUrl": "https://example.com/portfolio",
        "githubUrl": "https://github.com/example/portfolio",
        "features": [
            "Responsive design for all device sizes",
            "Customizable sections for projects, skills, and experience",
            "Contact form with validation",
            "Dark mode support",
            "SEO optimization",
            "Performance-focused implementation",
            "Smooth page transitions and animations",
        ],
        "featured": False,
    },
]

# Skill categories with all fields
skill_categories = [
    {
        "name": "Programming Languages",
        "skills": ["Java", "JavaScript", "C", "TypeScript"],
    },
    {
        "name": "Backend",
        "skills": [
            "Spring Boot",
            "REST APIs",
            "PostgreSQL",
            "Microsoft SQL Server",
            "MVC",
        ],
    },
    {
        "name": "Development Tools",
        "skills": [
            "Git",
            "Microsoft Power Platform",
            "Microsoft Power Automate",
            "Google Apps Script",
        ],
    },
    {
        "name": "Methodologies",
        "skills": ["Scrum", "Agile"],
    },
    {
        "name": "Other Skills",
        "skills": [
            "Web Applications",
            "Chatbot Development",
            "Google Sheets",
            "English (B2 Level)",
        ],
    },
]

# Featured skills
featured_skills = [
    "Java",
    "Spring Boot",
    "JavaScript",
    "PostgreSQL",
    "REST APIs",
    "Git",
    "MVC",
    "Google Apps Script",
]

# API endpoint mapping
ENDPOINTS = {
    "blog": "/blog",
    "work_experience": "/experience/work",
    "achievements": "/experience/achievements",
    "education": "/experience/education",
    "projects": "/projects",
    "skill_categories": "/skills",
}


def delete_all_items(endpoint_name):
    """Delete all items from a specific collection"""
    endpoint = ENDPOINTS[endpoint_name]
    try:
        # Get all items first
        response = make_api_request("get", f"{BASE_URL}{endpoint}")
        if response.status_code != 200:
            print(f"Failed to get {endpoint_name} items: {response.status_code}")
            return False

        items = response.json()
        if not items:
            print(f"No {endpoint_name} items to delete")
            return True

        count = 0
        for item in items:
            item_id = item.get("_id")
            if not item_id:
                continue

            delete_response = make_api_request(
                "delete", f"{BASE_URL}{endpoint}/{item_id}"
            )
            if delete_response.status_code in [200, 204]:
                count += 1
            else:
                print(
                    f"Failed to delete {endpoint_name} item {item_id}: {delete_response.status_code}"
                )

            # Small delay to avoid overwhelming the server
            time.sleep(0.1)

        print(f"Deleted {count}/{len(items)} {endpoint_name} items")
        return True

    except Exception as e:
        print(f"Error deleting {endpoint_name} items: {str(e)}")
        return False


def post_items(endpoint_name, items):
    """Post items to a specific collection"""
    endpoint = ENDPOINTS[endpoint_name]
    try:
        success_count = 0
        for item in items:
            response = make_api_request("post", f"{BASE_URL}{endpoint}", json=item)

            if response.status_code in [200, 201]:
                success_count += 1
                name = item.get("title", item.get("name", item.get("degree", "Item")))
                print(f"Successfully added {endpoint_name}: {name}")
            else:
                name = item.get("title", item.get("name", item.get("degree", "Item")))
                print(
                    f"Failed to add {endpoint_name} '{name}': {response.status_code} - {response.text}"
                )

            # Small delay to avoid overwhelming the server
            time.sleep(0.2)

        print(f"Added {success_count}/{len(items)} {endpoint_name} items")
        return success_count

    except Exception as e:
        print(f"Error posting {endpoint_name} items: {str(e)}")
        return 0


def clear_and_reload_database():
    """Clear all collections and reload with fresh data"""
    print("Starting database cleanup and reload process...")

    # Check server connection first
    if not check_server_connection():
        print("Cannot connect to server. Please make sure the server is running.")
        sys.exit(1)

    # Step 1: Delete all existing items
    print("\n--- Clearing database ---")
    for endpoint in ENDPOINTS.keys():
        delete_all_items(endpoint)

    # Step 2: Post all fresh items
    print("\n--- Loading fresh data ---")
    post_items("blog", blog_posts)
    post_items("work_experience", work_experiences)
    post_items("achievements", achievements)
    post_items("education", education)
    post_items("projects", projects)
    post_items("skill_categories", skill_categories)

    print("\nDatabase cleanup and reload complete!")


if __name__ == "__main__":
    clear_and_reload_database()
