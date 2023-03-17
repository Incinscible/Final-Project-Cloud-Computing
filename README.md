# Final-Project-Cloud-Computing

This project demonstrates a simple Flask web application that connects to a MongoDB database using Docker containers. The application allows users to view and add football teams and players to the database.

### Prerequisites

Docker

Docker Compose

### Getting Started

To run the application, follow these steps:

  1) Clone the repository:

    git clone https://github.com/<username>/<repository>.git cd <repository>
2) Build the image:
```
docker build -t ligue1 .
```
3) Start the Docker containers:
  ```
  docker-compose up
  ```
4) Access the application at http://localhost:5000 in a web browser.

#### Usage

Click on the team to see the players in it.

#### Technologies Used

Flask: a micro web framework for Python
MongoDB: a document-oriented NoSQL database
Docker: a containerization platform
Docker Compose: a tool for defining and running multi-container Docker applications

Acknowledgments
This project was developed as part of a Cloud Computing course at ESILV MADE BY ROMAN GAIGNAULT and qg.

License
This project is licensed under the MIT License
