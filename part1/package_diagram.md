<img width="568" height="1015" alt="image" src="https://github.com/user-attachments/assets/86ba75a2-4d96-4dfc-a15e-a6e25c7011d5" />

## Explanatory Notes

### 1. Layers and Their Responsibilities

*   **Presentation Layer:**
    *   **Role:** This layer contains the `API`.
    *   **Responsibility:** It handles the communication with the outside world. It receives requests from the user (like asking to register an account or search for a place) and sends back the results. It does not do any heavy thinking; it just passes the requests to the next layer.

*   **Business Logic Layer:**
    *   **Role:** This layer contains the `Core Entities`.
    *   **Responsibility:** It contains all the main entities (`User`, `Place`, `Review`, `Amenity`) and the `HBnBFacade`. It processes the data, applies the rules (like checking if a rating is between 1 and 5), and prepares objects to be saved.

*   **Persistence Layer:**
    *   **Role:** This layer is responsible for saving and retrieving data.
    *   **Responsibility:** It uses a `RepositoryInterface` to define how data should be saved. Because we use an interface, our system can easily switch between saving data temporarily in memory (`InMemoryRepository`) for testing, or permanently in a database (`SQLRepository`) for the final product.

---

### 2. The Facade Pattern and Layer Communication

The **Facade Pattern** uses the `HBnBFacade` as a "manager" or "middleman" to make communication between layers much easier:

*   **Hiding Complexity:** The `API` in the Presentation Layer does not need to know how a `User` is created, how to link a `Review` to a `Place`, or how to connect to the database. It only needs to talk to the `HBnBFacade`.
*   **Single Point of Entry:** If the API wants to create a new place, it simply calls one easy command on the Facade (for example: `create_place()`). 
*   **Doing the Hard Work:** The Facade takes that simple command and does all the hard work behind the scenes. It creates the `Place` object, checks the rules, and tells the `RepositoryInterface` to save it.
*   **Why it helps:** This keeps our `API` code very clean and simple. If we change how things work inside the Business Logic, we don't have to rewrite the API, because the Facade handles the changes.
