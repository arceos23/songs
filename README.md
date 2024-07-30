# Additional Considerations for Production-Ready Software

## Data Ingestion

1. Improve the robustness of using Pandas to normalize the input data. Considerations include ensuring consistency of column attributes, handling missing data, etc.
2. Explore automating the data ingestion process. Depending on how often the data source updates its song data, a data pipeline can utilize stream or batch processing to obtain new data and update the backend.
3. Utilize a database to store data persistently, which can improve the user experience by storing song ratings across sessions and establishing a foundation to build upon for other features. Properly using a relational database such as Postgres will also help ensure data consistency through constraints, keys, etc.
4. Consider getting data from multiple sources to improve the song catalog locally and globally

## API

1. Explore security considerations such as setting appropriate security headers
2. Consider using fuzzy matching to identify the title of a song that a user wants to update.

## CI/CD

1. Implement automated testing by using a CI/CD tool like GitHub Actions
2. Add integration tests to test the entire data pipeline and API
3. Automate deployments

## Optimizations

1. Perform load testing to identify bottlenecks
2. Consider high-impact improvements to latency and availability, especially if the service will operate globally: database indexes on common queries, CDN for static data, caching for hot data, geographically dispersed database replication, etc.

## Other features

1. Extend the rating system to accommodate multiple users, allowing for more features like an average rating for a song. Note that a normalized relational database would require additional tables to track users and songs that users liked: a many-to-many relationship.
2. Authentication and authorization to track users and their capabilities
