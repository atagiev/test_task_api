## Test Cases

| Test Case | Steps | Expected Result | Validation |
|-----------|-------|-----------------|------------|
| **Test different number of facts** | 1. Send a request to get a random number of facts. <br> 2. Verify the number of facts returned matches the requested number. <br> 3. Check that all facts are unique. | The number of facts returned should equal the requested number, and all facts should be unique. | 1. Use the `assert` statement to check the length of the facts list. <br> 2. Use `Counter` to ensure there are no duplicate facts. |
| **Test random fact type matches** | 1. Send a request to get a fact of a specific type (e.g., 'cat', 'dog', etc.). <br> 2. Verify the type of the fact returned matches the requested type. | The type of the fact returned should match the requested type. | Use the `assert` statement to compare the requested type with the obtained type. |

## Setup and Run Tests

To start, run the command `pip install -r requirements.txt` and then `pytest test_api.py`.
