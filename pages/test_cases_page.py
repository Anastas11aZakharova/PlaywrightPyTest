from playwright.sync_api import Page, expect


class TestCases():
    def __init__(self, page: Page):
        self.page = page

        self.__test_cases_label = self.page.get_by_text(
            'Below is the list of test Cases for you to practice the Automation. Click on the scenario for detailed Test Steps:')

    def check_test_cases_label_is_visible(self) -> None:
        self.__test_cases_label.wait_for(state='visible')
        expect(self.__test_cases_label).to_be_visible()
