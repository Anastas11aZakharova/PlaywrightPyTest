# PyTest + Playwright

## Latest test results
Available at https://anastas11azakharova.github.io/PlaywrightPyTest/

## summary
15 test cases for https://www.automationexercise.com/ website using PyTest & Playwright framework and PageObjectModel pattern

GitHub actions configured to: 
1. Run tests (taking screenshots at critical points) 
2. Generate Allure report and publish to GitHub Pages
3. Generate a notification in [Slack channel #ci-results](https://luxequalityinternship.slack.com/archives/C07L140N03Z) with test results

## requirements:
- Python 3
- Playwright
- PyTest
- Code editor (e.g. PyCharm)

## steps to install:
1. Clone repository
2. ```python -m pip install --upgrade pip ```
3. ``` pip install pipenv ```
4. ``` pipenv install ```
5. ``` playwright install ```

## steps to launch:
```
pytest --browser_name=firefox --alluredir=./reports --clean-alluredir
```
optionally, --headed can be added to view the run in the browser

additionally, you can define a subset of tests to be executed (defined with pytest.mark and in pytest,ini)
e.g.:

```
pytest -m cart
```

## steps to generate report
```
allure serve reports 
```
