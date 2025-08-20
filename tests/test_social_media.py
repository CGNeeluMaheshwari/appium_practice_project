from utils.base_test import BaseTest


class TestSocialLinks(BaseTest):
    def test_social_links(self):
        """Scroll down and validate the Twitter, facebook and linkedin link at the bottom."""
        try:
            twitter_icon = self.scroll_to_element_by_accessibility_id("Twitter")
            assert twitter_icon.is_displayed(), "Twitter icon not visible after scroll"
            facebook_icon = self.scroll_to_element_by_accessibility_id("Facebook")
            assert facebook_icon.is_displayed(), "Facebook icon not visible after scroll"
            linkedin_icon = self.scroll_to_element_by_accessibility_id("LinkedIn")
            assert linkedin_icon.is_displayed(), "LinkedIn icon not visible after scroll"
        except Exception as e:
            self.driver.save_screenshot("social_link_not_found.png")
            raise e
