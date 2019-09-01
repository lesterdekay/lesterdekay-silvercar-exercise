# Lester DeKay Silvercar Exercise 2
## Assignment: Review the documentation of the GitHub API at: https://developer.github.com/v3/
Imagine that you are on the team that has been tasked with implementing this specification.
### Part 1: Answer the following questions:
#### What concerns would you have from a testing perspective?
* The spec states that some attributes are computationally expensive for the API to provide so they are excluded from the summary. I have 2 concerns related to this:
Which endpoints contain attributes that are computationally expensive and will therefore not return all attributes in the summary?
How to test the effect of computationally expensive attributes on the system? (This particular concern is really part of the larger concern with load/performance testing.)
* I have a concern about knowing which fields are allowed to be null.
* The spec states that authorization affects the level of detail returned. Knowing which endpoint this is true for is a minor concern.
* The spec states that in some places requests that require auth return a 404 instead of a 403. Knowing which ones behave which way is a concern.
* The spec states that not all endpoints respect the per page parameter. Knowing which ones do is a concern.
* Developing a good way to test pagination is a concern.
* My greatest concern is with testing rate limiting. Testing the features of rate limiting as well as testing with rate limiting enabled in the system seem problematic without test hooks.
For automation purposes it seems likely to me that there would have to be a way to disable rate limiting to avoid false failures. Automation could easily exceed the stated limits for authenticated and unauthenticated calls.
It would also seem beneficial to add test hooks to modify limits as well as the reset time.
* Knowing which responses are supposed to return a Last-Modified header is a concern.
* JSON-P callback testing is a concern. Writing a test harness to validate the return value could be very complex.
* Generating test data to validate against is a concern.
#### How would you go about tackling the QA for this work?
I would start by working with the entire development team to generate development epics and stories. At that time I would bring up the need for any special test hooks and test data needed for validation. I would provide the team with my list of test cases for each and gather feedback from the team.
While developers are working on writing code to implement the story, I would work in writing automation code to validate the story, using a stubbed version of the api to do so. Ideally, the test data returned by the stubbed api would be the same as the test data returned by the server-side api implementation, so automation would already be validating the same set of data.
Depending on the pace of development and the pace of QA automation, some stories may need to be manually validated. If that were the case, I would create a QA automation ticket in a QA backlog board to ensure that the automation work is done when possible.
#### What sort of tests would be worth describing or worth automating?
The sort of tests that are worth describing or automating are tests that validate endpoint responses. Along the way, there may be some stories that are foundational that QA can assist the team with validating, but in the end they would be validated within the context of the greater feature.
Validating something like rate limit reset times may not be worth automating due to its effect on automation run times or difficulty in building test hooks for, but it would be worth manually testing the feature.
Any test that is repeatable and is a candidate for inclusion in a regression test set is worth automating.
#### What tools would you use?
While I have not used it, I have heard good things about swagger. For the purposes of this exercise, however, I will use the tools that I am familiar with, python and requests.
### Part 2: Stub implementation
Build a stub implementation of one endpoint and a test battery for that endpoint with the tech stack of your choice, and provide the URL of a public git repository that contains your implementation and tests.
Include documentation in your repository that contains your written answers to the questions above.
#### Running the tests
* Install required packages: pip install -r requirements.txt
* Run the tests: nosetests --verbosity=2
* The api endpoint stub implementations as well as methods to call the live implementation are in api/endpoints.py
* The tests are located in the tests.py file
* By default, the tests are set to test against the mock api implementation. Any test can be configured to test against the live endpoint by changing the call parameter to mock=False