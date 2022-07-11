import pytest

@pytest.mark.usefixtures("setup")
class TestTitles:
  def test_title(self):
    self.driver.get('https://www.mitchbounds.com')
    assert self.driver.title == "Home"

  def test_title_about(self):
    self.driver.get('https://www.mitchbounds.com/about.html')
    assert self.driver.title == "About"

  def test_title_projects(self):
    self.driver.get('https://www.mitchbounds.com/projects.html')
    assert self.driver.title == "Projects"
